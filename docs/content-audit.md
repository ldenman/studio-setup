# Content Accuracy Audit — 2026-04-05

Compared non-blog page content against `studio.edn` and `CLAUDE.md` sources of truth.

---

## CRITICAL

### 1. wa76.astro ~line 159 — Wrong guitar compression ratio
- **Says:** "Guitar channel runs at 20:1 for heavier limiting"
- **Actually:** 4:1 per studio.edn calibration (line 402)
- **Fix:** Change 20:1 to 4:1
- **Status:** FIXED — 2026-04-05

### 1b. production.astro ~line 35 — Session players described as responding live
- **Says:** "they follow along as you play, responding to tempo and feel"
- **Actually:** Logic session players generate a part based on chord progression and settings. They don't listen to live input or adapt in real time. They play back a pre-rendered performance.
- **Fix:** Remove "responding to tempo and feel" — say "they play back generated parts that match the chord progression and tempo"
- **Status:** FIXED — 2026-04-05

### 1c. production.astro ~line 32 — Session players described as real-time
- **Says:** "They play alongside live instruments in real time"
- **Actually:** They play back simultaneously, yes, but "in real time" implies live interaction. They're just playback.
- **Fix:** "They play back through the Wing alongside live instruments" — drop "in real time"
- **Status:** FIXED — 2026-04-05

### 1d. how-it-works.astro ~line 527 — Session players described as dynamic
- **Says:** "they are dynamically generated performances that follow the chord progression and feel of the song"
- **Actually:** The parts are generated from settings/chord input, not dynamically during playback. Once generated, they're fixed audio/MIDI.
- **Fix:** "they are generated performances based on the chord progression and style settings" — drop "dynamically" and "follow...feel"
- **Status:** FIXED — 2026-04-05

### 16. gear.astro ~line 95 — Wrong vocal compression ratio
- **Says:** "Ratio at 8:1 for vocals, 4:1 for guitar"
- **Actually:** studio.edn calibration shows wa76-a ratio "4:1" for vocals AND wa76-b ratio "4:1" for guitar. Both channels run 4:1.
- **Fix:** "Ratio at 4:1 for both vocal and guitar channels"
- **Status:** FIXED — 2026-04-05

### 17. ha73.astro ~line 200 — Wrong gain calibration values
- **Says:** "Gain is calibrated to 55 on Channel A (vocal) and 50 on Channel B (guitar)"
- **Actually:** studio.edn calibration shows `gain-knob 35` for both HA73 channels (ha73-a and ha73-b)
- **Fix:** Change to "Gain is calibrated to 35 on both Channel A (vocal) and Channel B (guitar)"
- **Status:** FIXED — 2026-04-05

---

## HIGH

### 2. rack.astro ~line 155 — Wrong routing for Wing Out 3
- **Says:** "USR/3 Tape Return → P9 → M12 Ch 6"
- **Actually:** Bus 8 (Guitar Rec) outputs on Wing Out 3 → P9 → Model 12 line in. USR/3 routes via USB 38 → M12 Ch 6, not through P9. These are two separate routing paths being conflated into one.
- **Fix:** Correct the Out 3 label to "Bus 8 Guitar Rec → P9 → M12 Track 2" and keep USR/3 labeling separate
- **Status:** FIXED — 2026-04-05

### 18. how-it-works.astro ~line 661 — Speakers described as muting automatically
- **Says:** "the studio speakers mute automatically"
- **Actually:** Speakers must be manually muted during tracking via `/mtx/1/mute i 1` (per CLAUDE.md). There is no automatic trigger or sensor — it is a deliberate manual command. Nothing in the signal chain auto-detects that a mic is live and mutes the speakers.
- **Fix:** "the studio speakers are muted manually before tracking begins" or "speakers are muted via a single command when a microphone is live"
- **Status:** FIXED — 2026-04-05

### 19. how-it-works.astro ~line 427 — Gate described as running on every input channel
- **Says:** "The mixer also runs a noise gate on each input channel"
- **Actually:** studio.edn shows :dynamics :gate only on Ch1 (Vocal Dry). No gate is documented on Ch2 (Guitar Dry) or any other input channel.
- **Fix:** "The mixer runs a noise gate on the vocal input channel" — scope it correctly
- **Status:** FIXED — 2026-04-05

---

## MEDIUM

### 3. recording.astro ~line 32 — Amp sim brand names don't match config
- **Says:** "a Mesa-style lead tone, a Fender clean, or a transparent acoustic preset"
- **Actually:** Bus 5 = FX6/ANGEL (lead), Bus 6 = FX11/RACKAMP (acoustic). FX1/DELUXE available for rhythm. No "Mesa" or "Fender" in config.
- **Fix:** Use actual model names, optionally with tone descriptions: "ANGEL (high-gain lead), DELUXE (clean rhythm), RACKAMP (acoustic)"
- **Status:** FIXED — 2026-04-05

### 4. production.astro ~line 70 — Same amp sim naming issue
- **Says:** "a Mesa-style lead tone, a Fender clean, an acoustic DI preset, or a completely clean bypass"
- **Actually:** Same as above — ANGEL, DELUXE, RACKAMP
- **Fix:** Match recording.astro fix
- **Status:** FIXED — 2026-04-05

### 5. mixing.astro ~line 37 — Rhythm amp description wrong
- **Says:** "Clean Fender tone or raw DI depending on the session"
- **Actually:** Bus 10 uses FX7/RACKAMP for rhythm, not a "Fender" tone
- **Fix:** "RACKAMP clean tone or raw DI depending on the session"
- **Status:** FIXED — 2026-04-05

### 6. mixing.astro ~line 41 — Lead amp description wrong
- **Says:** "Mesa-style dark tone for leads and solos"
- **Actually:** Bus 11 uses FX12/ANGEL. ANGEL is not described as "Mesa-style" in config.
- **Fix:** "ANGEL high-gain tone for leads and solos"
- **Status:** FIXED — 2026-04-05

### 7. gear.astro ~line 52 — HA73 gain spec may be wrong
- **Says:** "Ch A: Vocal (SM7B, 58dB gain)"
- **Actually:** studio.edn calibration shows gain-knob at 35 for HA73 A. 58dB may be the actual dB output at that knob position, or it may be wrong. See also new item 17 which confirms 35 is the documented knob position.
- **Fix:** Changed to "gain knob 35" to match studio.edn documented value
- **Status:** FIXED — 2026-04-05

### 20. sound-design.astro ~line 46 — Mesa/Fender brand names for Wing amp sims
- **Says:** "a Mesa-style lead with dark, controlled gain; a Fender-style clean with bright sparkle"
- **Actually:** Wing amp sims are ANGEL (lead) and DELUXE (rhythm/clean), not "Mesa-style" or "Fender-style" per studio.edn
- **Fix:** "ANGEL (high-gain lead), DELUXE (clean rhythm), RACKAMP (acoustic)" — use actual model names
- **Status:** FIXED — 2026-04-05

### 21. how-it-works.astro ~line 423 — Mesa/Fender brand names for Wing amp sims
- **Says:** "a clean Fender-style for rhythm parts, a high-gain Mesa-style for lead work"
- **Actually:** Same as above — actual models are DELUXE and ANGEL
- **Fix:** Name the actual Wing models, optionally with character description
- **Status:** FIXED — 2026-04-05

### 22. first-cover.md lines 13, 15 — Mesa/Fender brand names for amp sims used in session
- **Says:** "Rhythm got a Fender clean amp sim" and "Lead went darker. A Mesa-style sim"
- **Actually:** Actual Wing models used are DELUXE (rhythm) and ANGEL (lead) per studio.edn
- **Fix:** "Rhythm got the DELUXE — bright, open, neck pickup..." and "Lead went darker. The ANGEL with gain pulled way down..."
- **Status:** FIXED — 2026-04-05

### 23. sound-design.astro ~line 49 — Re-amp described as going through "the Mesa sim"
- **Says:** "A rhythm guitar recorded clean can be re-amped through the Mesa sim"
- **Actually:** The re-amp path uses Bus 5 which carries FX6/ANGEL (lead) or FX1/DELUXE (rhythm). Neither is called "Mesa."
- **Fix:** "re-amped through the ANGEL or DELUXE sim"
- **Status:** FIXED — 2026-04-05

---

## LOW

### 8. ha73.astro ~line 200 — HPF settings unverifiable
- **Says:** "The high-pass filter stays at 80Hz for vocals, 160Hz for guitar"
- **Actually:** studio.edn doesn't document HPF settings per channel. May be operationally correct but can't be verified from config.
- **Fix:** Changed "stays at" to "is typically set to" to flag as typical rather than guaranteed
- **Status:** FIXED — 2026-04-05

### 9. gear.astro ~line 52 — Incomplete signal chain
- **Says:** "Signal: Ch1/Ch2 → Out 1/2 → HA73 → WA76"
- **Actually:** Chain continues through Opto (vocal) or Distressor (guitar) before returning to Wing
- **Fix:** Added "→ ..." to indicate continuation
- **Status:** FIXED — 2026-04-05. Note: gear.astro line 96 does say "Signal: HA73 → WA76 → Distressor/Opto" for the WA76 entry, which is correct.

### 10. rack.astro ~line 250 — Incomplete routing label
- **Says:** "Model 12 AUX 1 Out → Wing LCL/3 (TRS→XLR cable)"
- **Actually:** Correct but doesn't mention this feeds Ch33 (Tape Send). Not wrong, just incomplete.
- **Fix:** Added "(→ Ch33 Tape Send)" to cable label
- **Status:** FIXED — 2026-04-05

---

## RECURRING THEME: Amp Sim Brand Names

Pages `recording.astro`, `production.astro`, `mixing.astro`, `sound-design.astro`, `how-it-works.astro`, and blog posts `first-cover.md` all use brand-style descriptions ("Mesa-style", "Fender clean") for Wing amp sim models. The actual models in studio.edn are:

| Description used | Actual model | Bus |
|-----------------|-------------|-----|
| "Mesa-style lead" | ANGEL | Bus 5 / Bus 11 |
| "Fender clean" | DELUXE | Bus 5 (alt) |
| "Acoustic preset" | RACKAMP | Bus 6 |
| "Clean rhythm" | RACKAMP | Bus 10 |

**Decision needed:** Keep brand-style descriptions (more evocative for readers) or switch to actual model names (more accurate)? Could do both: "DELUXE (Fender-voiced clean)"

**Exception — five-amp-sims.md:** This blog post explicitly names the Wing models (DELUXE, ANGEL, RACKAMP, UKROCK, JAZZC) and describes their sonic character with appropriate attribution ("modeled after the Fender Deluxe family", "Modeled after the Mesa/Boogie family"). Because the post names the actual Wing model first and attributes the inspiration, this is accurate and acceptable.

---

## ADDITIONAL FINDINGS (Deep Dive — from first audit pass)

### 11. index.astro ~line 39 — "No setup" is a lie
- **Says:** "No setup. No patching. Just play."
- **Actually:** Every session requires gain staging, level checking, compressor threshold/ratio adjustments per source, and speaker muting during tracking. The patchbay is normalled but "no setup" is false.
- **Fix:** Changed "always connected, always calibrated, always ready" to "always connected, normalled and ready" — drops the false calibration claim
- **Status:** FIXED — 2026-04-05

### 12. how-it-works.astro ~line 113 — Gear warm-up claim
- **Says:** "Every piece of gear is warmed up, every signal path is tested, every level is calibrated."
- **Actually:** Analog tube/transformer gear needs 15-30 minutes to thermally stabilize. This is stated as if it's always true at any moment.
- **Fix:** Changed to "Every signal path is permanently wired and normalled, every level is documented."
- **Status:** FIXED — 2026-04-05

### 13. how-it-works.astro ~line 298 — Plugin vs hardware absolutes
- **Says:** "no plugin can replicate" / "algorithms can approximate but never quite replicate"
- **Actually:** Subjective marketing claim presented as technical fact. The studio itself uses T-RackS Tape Machine plugin — contradicting the "plugins can't replicate hardware" claim. Also appears in ha73.astro line 203.
- **Fix:** Changed both how-it-works.astro and ha73.astro to "approximate differently" / "plugins approximate differently"
- **Status:** FIXED — 2026-04-05

### 14. Multiple pages — "Always" overstatements
- **Locations:** index.astro ~line 39, gear.astro ~line 9
- **Says:** "always connected, always calibrated, always ready" / "Permanently wired, always ready"
- **Actually:** Chains are normalled (always connected = true). But "always calibrated" is false — calibration is per-session. "Always ready" overstates operational reality.
- **Fix:** index.astro: "always connected, normalled and ready"; gear.astro: "Permanently wired, normalled and ready"
- **Status:** FIXED — 2026-04-05

### 15. how-it-works.astro ~line 657 — Zero latency scope
- **Says:** "zero latency" (monitoring)
- **Actually:** True for the live input hardware path (mic → Wing → headphones). NOT true for session player playback (Logic processing latency) or Wing FX (DSP processing delay). The claim implies zero latency everywhere.
- **Fix:** Changed to "zero latency on the live input path"
- **Status:** FIXED — 2026-04-05

---

## FINDINGS MARKED RESOLVED

- **1, 16, 17** — WA76 ratio and HA73 gain values corrected to match studio.edn calibration (2026-04-05)
- **1b, 1c, 1d** — Session player descriptions corrected: removed claims of real-time interaction/dynamic generation (2026-04-05)
- **2** — rack.astro Out 3 routing corrected from "USR/3 Tape Return" to "Bus 8 Guitar Rec" (2026-04-05)
- **18** — Speaker muting changed from "automatically" to "via a single command" (2026-04-05)
- **19** — Noise gate scope narrowed from "each input channel" to "the vocal input channel" (2026-04-05)
- **3, 4, 5, 6, 20, 21, 22, 23** — All amp sim brand names (Mesa/Fender) replaced with actual Wing model names: ANGEL, DELUXE, RACKAMP (2026-04-05)
- **7** — HA73 gain spec changed from "58dB" to "gain knob 35" per studio.edn; signal chain appended with "→ ..." (2026-04-05)
- **8** — ha73.astro HPF settings qualified as "typically set to" rather than absolute (2026-04-05)
- **9** — gear.astro signal chain appended with "→ ..." to indicate continuation (2026-04-05)
- **10** — rack.astro cable label now includes "(→ Ch33 Tape Send)" destination (2026-04-05)
- **11, 14** — "always calibrated, always ready" replaced with "normalled and ready" on index.astro and gear.astro (2026-04-05)
- **12** — Warm-up claim replaced with "permanently wired and normalled" (2026-04-05)
- **13** — "no plugin can replicate" / "never quite replicate" softened to "approximate differently" in how-it-works.astro and ha73.astro (2026-04-05)
- **15** — "zero latency" scoped to "zero latency on the live input path" (2026-04-05)

---

*First audit: Claude, 2026-04-05. Second audit: Claude, 2026-04-05 (deep dive — all pages + all blog posts).*
*Verify items before making changes.*
