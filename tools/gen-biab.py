#!/usr/bin/env python3
"""
Generate Band-in-a-Box SG1 files from a chord progression.

Usage:
    python3 tools/gen-biab.py --title "Knockin On Heavens Door" --key G \
        --chords "G D Am Am G D C C" --output ~/Desktop/khod.sg1

Chord format: space-separated, e.g. "G D Am Am G D C C"
Supported qualities: major (default), m (minor)
Examples: G, Am, Dm, C, D, Em

The SG1 format packs chords into two 6-slot blocks separated by style markers.
Block 1 = bars 1-6, Block 2 = bars 7-12. BIAB loops at the user-set end bar.
For an 8-bar loop (G D Am Am | G D C C), set loop end to bar 8 in BIAB.
"""

import os
import sys
import argparse

# Root note encoding: 1-indexed chromatic (C=1, C#=2, D=3, ..., G=8, ..., A=10, B=12)
ROOTS = {
    'C': 1, 'C#': 2, 'Db': 2,
    'D': 3, 'D#': 4, 'Eb': 4,
    'E': 5,
    'F': 6, 'F#': 7, 'Gb': 7,
    'G': 8, 'G#': 9, 'Ab': 9,
    'A': 10, 'A#': 11, 'Bb': 11,
    'B': 12,
}

# Key encoding: 51 - (sharps * 2), or 51 + (flats * 2)
KEYS = {
    'Cb': 63, 'Gb': 61, 'Db': 59, 'Ab': 57, 'Eb': 55, 'Bb': 53, 'F': 51,
    'C': 51, 'G': 49, 'D': 47, 'A': 45, 'E': 43, 'B': 41, 'F#': 39, 'C#': 37,
}

EMPTY = bytes([0xFF, 0x00])

# Major/minor flag byte. LSB=1 → major, LSB=0 → minor.
# Using 0x03 (major) and 0x02 (minor) to match Untitled 2's style encoding.
FLAG_MAJOR = 0x03
FLAG_MINOR = 0x02


def parse_chord(s):
    """Parse a chord string like 'G', 'Am', 'Dm', 'C#m' into 3 bytes."""
    s = s.strip()
    if not s:
        return None
    # Check for minor
    if s.endswith('m') and not s.endswith('#m') and len(s) > 1:
        note = s[:-1]
        flag = FLAG_MINOR
    elif 'm' in s and s.index('m') > 0:
        # e.g. C#m, Bbm
        idx = s.index('m')
        note = s[:idx]
        flag = FLAG_MINOR
    else:
        note = s
        flag = FLAG_MAJOR

    if note not in ROOTS:
        raise ValueError(f"Unknown note: {note!r} in chord {s!r}")
    return bytes([flag, ROOTS[note], 0x00])


def build_block(chords, separator):
    """
    Build a chord block:
      - Up to 6 chord entries (3 bytes each)
      - Remaining slots filled with EMPTY (2 bytes) to reach 6 slots
      - 3 fixed EMPTY footer entries
      - 3-byte separator

    Total data before separator:
      full block (6 chords): 6*3 + 3*2 = 24 bytes
      partial block (N chords): N*3 + (6-N)*2 + 3*2 bytes
    """
    if len(chords) > 6:
        raise ValueError(f"Block can hold max 6 chords, got {len(chords)}")
    data = b''.join(chords)
    data += EMPTY * (6 - len(chords))   # pad chord slots to 6
    data += EMPTY * 3                   # fixed footer
    data += separator
    return data


def load_template(path):
    """Load and parse the SG1 template file, return (template_bytes, offsets_dict)."""
    with open(path, 'rb') as f:
        tmpl = bytearray(f.read())

    assert tmpl[0] == 0x49, "Not a valid SG1 file (missing 0x49 magic)"
    title_len       = tmpl[1]
    settings_off    = 2 + title_len + 1   # after magic + len + title + null
    chord_off       = settings_off + 14   # settings block is always 14 bytes

    # Block 1: 6 chords*3 + 3 empties*2 = 24 bytes, then 3-byte separator
    b1_sep_off      = chord_off + 24
    b2_chord_off    = b1_sep_off + 3
    b2_sep_off      = b2_chord_off + 24
    rest_off        = b2_sep_off + 3

    return tmpl, {
        'settings_off': settings_off,
        'chord_off':    chord_off,
        'b1_sep':       bytes(tmpl[b1_sep_off : b1_sep_off + 3]),
        'b2_sep':       bytes(tmpl[b2_sep_off : b2_sep_off + 3]),
        'rest_off':     rest_off,
    }


def generate(title, key, chords, template_path, output_path):
    tmpl, offs = load_template(template_path)

    # Settings: clone template, update key byte
    settings = bytearray(tmpl[offs['settings_off'] : offs['settings_off'] + 14])
    if key not in KEYS:
        raise ValueError(f"Unknown key: {key!r}. Choose from: {', '.join(KEYS)}")
    settings[0] = KEYS[key]

    # Parse all chords
    encoded = [parse_chord(c) for c in chords]
    if len(encoded) > 12:
        print(f"Warning: {len(encoded)} chords provided; only first 12 will be used (6 per block).")
        encoded = encoded[:12]

    # Pad to at least 12 chords by cycling the progression
    while len(encoded) < 12:
        encoded.extend(encoded[:12 - len(encoded)])

    block1 = build_block(encoded[0:6], offs['b1_sep'])
    block2 = build_block(encoded[6:12], offs['b2_sep'])

    # Assemble
    rest    = bytes(tmpl[offs['rest_off']:])
    title_b = title.encode('ascii')
    header  = bytes([0x49, len(title_b)]) + title_b + bytes([0x00])
    output  = header + bytes(settings) + block1 + block2 + rest

    with open(output_path, 'wb') as f:
        f.write(output)

    print(f"Written: {output_path}  ({len(output)} bytes)")
    print(f"Key: {key}  (0x{KEYS[key]:02x})")
    print(f"Chords written:")
    names = chords if len(chords) >= 12 else (chords * 3)[:12]
    for i, (c, b) in enumerate(zip(names[:12], encoded[:12])):
        blk = "block1" if i < 6 else "block2"
        print(f"  bar {i+1:2d} [{blk}] {c:6s}  → {b.hex()}")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--title',    default="Knockin On Heavens Door",
                   help="Song title (ASCII, default: Knockin On Heavens Door)")
    p.add_argument('--key',      default="G",
                   help="Key signature (default: G)")
    p.add_argument('--chords',   default="G D Am Am G D C C",
                   help="Space-separated chord progression (default: G D Am Am G D C C)")
    p.add_argument('--output',   default=os.path.expanduser("~/Desktop/knockin-on-heavens-door.sg1"),
                   help="Output SG1 file path")
    p.add_argument('--template', default=os.path.expanduser("~/Desktop/Untitled 2 .SG1"),
                   help="Template SG1 file to clone structure from")
    args = p.parse_args()

    chords = args.chords.split()
    output = os.path.expanduser(args.output)
    template = os.path.expanduser(args.template)

    generate(args.title, args.key, chords, template, output)


if __name__ == '__main__':
    main()
