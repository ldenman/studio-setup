# Website Overview

## What This Site Is

A studio website for Lake's Studio — the kind of site you'd find for any professional recording space. It tells visitors what the studio is, what it offers, and what makes it unique. It also doubles as a working reference for anyone using the studio (including Lake).

Think of studios like Blackbird, Electric Lady, or even smaller project studios that have a web presence. They all share the same bones: a sense of the room, the gear list, the philosophy, and a way to get in touch. This site does that, plus it goes deeper into the technical side because the studio is also a personal workspace where that detail matters.

## Current State

The site is a single `index.html` — self-contained, no framework, no build step. Dark theme, responsive. It currently functions as an internal technical reference with seven sections:

1. **Overview** — stat cards (channels, outboard, tracks, FX slots) and a brief description
2. **Signal Flow** — visual diagrams of the guitar and vocal chains
3. **Channels** — visual channel strip layout for all 16 Wing channels
4. **Patchbay** — grid showing all patchbay point assignments
5. **Gear** — expandable cards with specs for each piece of outboard
6. **Effects** — tabbed, searchable catalog of every effect across Wing, outboard, and software
7. **Quick Ref** — BPM calculator, color map, common OSC commands

Interactive features: BPM delay calculator, effects search/filter, scroll-spy nav.

## What's Missing

The site reads like documentation. It doesn't read like a studio. There's no personality, no sense of what it's like to work there, no indication of what the studio is for or who it's for. A visitor landing on the page sees channel numbers and OSC commands — not a place where music gets made.

Specifically:

- **No hero/landing section** — no first impression, no vibe
- **No studio identity** — no description of the space, the philosophy in human terms, or the kind of work done here
- **No photos or visual media** — gear photos, room shots, session shots
- **No services/offerings framing** — what can someone do here? Recording, mixing, production?
- **No "about" narrative** — who runs it, what's the approach, what's the sound
- **No contact or booking** — no way to reach out
- **The gear section is specs-only** — no context for why each piece was chosen or what it brings to the sound
- **The technical reference sections are great but buried** — they should feel like a bonus deep-dive, not the main event

## Site Goals

### 1. First Impression — The Studio Has a Vibe
When someone lands on the site, they should immediately get a feel for the space. A hero section with a strong visual (photo or stylized graphic), the studio name, a one-liner, and a sense of aesthetic. The dark theme already works well for this — lean into it.

### 2. Studio Identity — What This Place Is
A concise section that communicates:
- What kind of studio this is (recording + mixing, hybrid analog/digital)
- The philosophy (zero friction, always ready, outboard-first signal chains)
- What makes it different (normalled patchbay, OSC-automated Wing Rack, dry multitrack capture with analog monitoring)
- The kind of music/work it's suited for (singer-songwriter, guitar-driven, production with session players)

### 3. Services / What You Can Do Here
Frame the studio's capabilities as offerings, not just a channel list:
- **Recording** — track live instruments through real outboard gear (Neve preamp, 1176, LA-2A) while monitoring with low-latency effects. Everything captured dry for maximum flexibility.
- **Production** — Logic Pro session players (bass, keyboard, synth, drums) routed through the Wing alongside live instruments. Build full arrangements.
- **Mixing** — hybrid analog/digital mixing with outboard processing, Wing channel strip emulations (Neve, SSL), and a deep effects catalog.
- **Sound Design** — 16 FX slots, guitar amp sims, modulation, pitch shifting, creative chains.

### 4. The Gear — With Context
Keep the detailed specs (they're excellent), but lead with storytelling:
- **Why this gear?** Each piece was chosen for a reason — the HA73 for Neve warmth, the 1176 for fast transient control, the Opto for smooth vocal compression, the Distressor for versatility.
- **How it's wired** — the patchbay and signal flow sections already do this well, but frame them as "here's how the studio works" rather than raw technical diagrams.
- **The console** — the Wing Rack deserves its own moment. 48 channels, 16 FX slots with classic emulations, OSC automation. It's the brain of the studio.

### 5. The Signal Chain — A Feature, Not a Diagram
The signal flow section is one of the best parts of the site. Make it more prominent:
- Position it as a selling point: "Your guitar goes through a real Neve preamp and 1176 compressor before it hits the recorder."
- Keep the visual diagrams — they're clean and effective.
- Add brief annotations about what each stage does to the sound.

### 6. Effects & Software — The Deep Dive
The effects catalog is comprehensive and well-organized. Keep it as-is but:
- Frame it as "what's available" rather than a raw lookup table
- The recipes section is gold — surface it more prominently as "sounds we can get"
- Consider grouping by use case (vocal sounds, guitar tones, mix bus, creative/experimental) in addition to the current technical grouping

### 7. Technical Reference — For Studio Users
The BPM calculator, OSC commands, and color map are useful tools for anyone working in the studio. Keep them, but position them as a utility section rather than a main navigation item. Maybe rename to "Studio Tools" or "Engineer's Reference."

### 8. Contact / Get In Touch
Even if it's minimal — an email, a form, a link. The site needs a way for someone to say "I want to record here."

## Design Direction

- **Keep the dark theme** — it's clean, professional, and fits the studio aesthetic
- **Keep it as a single HTML file** — the simplicity is a feature, not a limitation
- **Add imagery** — even placeholder sections for photos. The site needs visual warmth.
- **Improve the hierarchy** — hero → identity → offerings → gear → signal flow → effects → tools → contact
- **Keep the interactive features** — BPM calculator, effects search, expandable gear cards. They're good.
- **Mobile-first mindset** — someone might pull this up on their phone while in the studio

## Section Order (Proposed)

1. **Hero** — name, tagline, hero image/visual, immediate vibe
2. **About / The Studio** — philosophy, approach, what makes it unique
3. **What We Do** — recording, production, mixing, sound design (services framing)
4. **The Gear** — outboard rack, console, recorder, software — with context and character
5. **Signal Flow** — how everything is wired, the default chains, the patchbay
6. **Sounds** — recipes, effect presets, "what we can get" — pulled from the current recipes tab
7. **Effects Catalog** — the full searchable reference (for the deep-divers)
8. **Studio Tools** — BPM calculator, color map, OSC reference
9. **Contact** — get in touch

## Non-Goals

- No blog, no news feed, no dynamic content that needs updating
- No user accounts or booking system (a simple contact method is enough)
- No framework, no build step, no dependencies — keep it vanilla HTML/CSS/JS
- No e-commerce or payment processing
- This is not a portfolio site (no past client list or session credits unless Lake wants that later)
