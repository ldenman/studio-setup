# Blog Post Backlog

Untold stories mined from session-lessons.md, CLAUDE.md, calibration.md, workflows.md, advanced.md, EFFECTS-REFERENCE.md, AUTOMATION-IDEAS.md, README.md, and git history. Ranked by reader interest.

## Top 10

1. **"The Tape Emulation That Evolved Four Times"** — In one week, tape moved from channel inserts to recording bus to hardware aux loop to software plugin, each migration triggered by a different failure.

3. **"The Wing's Silent Theft"** — Assigning an FX slot to a new channel silently removes it from wherever it was before — no warning, just a hole in your signal chain.

4. **"Why the Mute Button Lies"** — On most consoles, pre-fader sends survive a mute. On the Wing, muting kills everything — and it took a silent recording path to teach us.

5. **"Negative Bar Numbers"** — Press play on the tape machine and the DAW jumps to bar -9, because of a 1970s SMPTE convention nobody remembers.

6. **"Separate Paths"** — Recording and monitoring shared a signal path — until we realized that meant choosing between hearing the amp sim and having a clean recording.

7. **"The Virtual Patchbay Nobody Sees"** — 24 invisible patch points inside the mixer that saved the studio from a routing dead end when USB outputs rejected direct channel routing.

8. **"The Stereo Collapse"** — Condensers sounded great in mono. The Model 12 return was dead center. Both were supposed to be stereo — until the Wing's default mono mode quietly collapsed them.

9. **"Mixing as a Performance"** — Every time you push a fader, the stereo track is rolling — so mixing isn't editing, it's playing the console like an instrument.

10. **"Phantom Power and the Patchbay"** — Condenser mics need 48 volts. The patchbay can't carry it. The one exception to "everything through the patchbay."

## Wing Quirks

- **FX slot theft** — An FX slot can only live on one insert at a time. Assigning it elsewhere silently removes it. Orphaned insert shows $stat=N/A.
- **Two channels on the same USB input** — Wing silently drops the signal on the second channel.
- **USR in numbering vs stereo indexing** — Different numbering schemes for different parameter paths. Got this wrong multiple times.
- **Stereo mode defaults to mono** — Must explicitly set mode=ST or stereo sources collapse to center.
- **Speaker output was mono** — Out 7 and Out 8 both set to in=1 (MX1 L). Stereo indexing error.
- **Send levels keep getting reset** — Ch26 send to Bus 10 needs +10dB but keeps resetting during other routing changes.
- **Buses on Main leak through solo** — Soloing a channel doesn't isolate you from buses assigned to Main.
- **Sidechain routing can't be set via OSC/wapi** — Always reverts to SELF. Must use touchscreen.
- **FX16 won't load** — Possible DSP limit when many FX are active.
- **Wing outputs reject CH group for high channel numbers** — Must use USR as intermediary.
- **Display name rule** — Channel display always shows the input source name. You can't override it with /ch/N/name.
- **Monitor section can't be accessed via wapi** — Only oscsend or touchscreen.

## Architecture Decisions

- **Amp sim goes after outboard, not before** — If you want outboard-only recordings with amp sim in monitoring, the amp sim must be on the monitoring bus.
- **One amp sim per track type, separate buses** — Don't switch a shared bus; add a new bus for rhythm vs lead.
- **Recording captures gate + outboard + de-esser, nothing else** — A deliberate minimal recording philosophy.
- **Guitar analog recording via Wing Out 3** — Chose analog over digital for the guitar recording path to the Model 12.
- **Speakers on the patchbay for source switching** — Break the normal with Model 12 mains for feedback-safe playback monitoring.

## Gear Character

- **HA73 channel variance** — Channels A and B have different output characteristics at identical knob positions.
- **The five Wing amp sims** — RACKAMP, UKROCK, ANGEL, JAZZC, DELUXE. Each a different character.
- **Fairchild 670 emulation (F670)** — Available on the Wing but not yet used.
- **Console emulations** — EVEN (Neve), SOUL (SSL), VINTAGE, BUS, MASTER. Available but unexplored.
- **T-RackS emulating a Tascam 388** — The irony of a Tascam tape plugin alongside a Tascam hardware unit.

## Workflow & Philosophy

- **Re-amping workflow** — Processing a dry track through the chain after the fact. Solo, route, capture.
- **Transport sync: Model 12 as master** — The tape machine owns the timeline. Logic slaves.
- **Zero friction philosophy in practice** — Everything permanently wired, normalled, always ready.
- **Logic's Software Monitoring must be OFF** — Zero latency monitoring; the Wing handles everything.
- **Vocal doubler on MX2 post-insert** — Affects both live and playback. Intentional design choice.
- **Sub octaver on bass** — FX4/SUB/MID pushing bass into midrange for guitar-friendly presence.

## Sound Design

- **Creative EQ presets** — Telephone voice, radio voice, lo-fi guitar, Nashville scoop.
- **Parallel compression via mix knob** — Wing dynamics have a built-in mix control. No extra routing.
- **Processing order is configurable** — Gate, EQ, Dynamics, Insert can be reordered per channel.
- **Phase alignment with channel delay** — Adding 1-3ms to dry channel to align with outboard return.
- **All-pass filter for phase rotation** — AP1/AP2 models for fixing phase at specific frequencies.
- **Shimmer reverb** — Ethereal octave-up reverb, available but unused.

## Automation Ideas (Not Yet Built)

- **Pre-take checklist script** — Catches problems before they become wasted takes.
- **Take logger** — Subscribe to Wing events, log every fader move and mute. Session history as data.
- **Dim on stop** — Auto-dim monitors when DAW stops. Prevents blasting yourself between takes.
- **Reference toggle** — A/B your mix against a reference with level matching. One command. ✅ Written: `reference-track-ab.md`
- **FX automation via Python** — Ramping reverb over 8 bars at 30fps. Real-time parameter control.
- **MIDI scene control for setlists** — Trigger Wing scenes from scripts.

## Meta / Building the Studio

- **Interactive rack room visualization** — Building an SVG rack with hover-to-trace signal chains.
- **Cable routing lesson** — Long cables along rack rails, left for vocal, right for guitar.
- **The website itself** — Astro static site built alongside the studio.
- **Harrison Mixbus 10** — Listed in README but never mentioned elsewhere. A second DAW?
- **Mastering section TBD** — Using outboard for master bus processing. Not yet explored.
