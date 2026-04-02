---
title: "Wing: USR Numbering vs. Stereo Indexing"
date: 2026-03-11
description: "The Wing uses two different numbering schemes for routing, and getting them confused means silence, the wrong signal, or both."
tags: ["wing", "lessons", "routing", "gear"]
hero: "/blog/two-counting-systems.svg"
---

We routed a signal to Bus 8 and got Bus 4. Not approximately Bus 4, not a weak version of Bus 8 bleeding through from somewhere. A clean, confident signal arriving at entirely the wrong destination. The Wing had done exactly what we asked. We'd just asked in the wrong language.

## One Console, Two Numbering Schemes

The Wing has two different ways of counting its internal routing points, and it uses them in different contexts with zero indication of which one applies. If you're setting up a USR input -- one of the Wing's virtual patch points -- and you want it to tap Bus 8, you set `in=8`. Bus 8 is bus 8. That's simple numbering, the kind where things are called what they are.

But if you're routing an output -- say, pointing a physical output at a bus -- the Wing switches to stereo indexing. In stereo indexing, every stereo source occupies two slots. Bus 1 Left is index 1, Bus 1 Right is index 2. Bus 2 Left is index 3, Bus 2 Right is index 4. By the time you get to Bus 8, you're at index 15 for the left side and 16 for the right.

Set `in=8` on a USR input and you get Bus 8. Set `in=8` on an output and you get Bus 4 Right. Same number, completely different destination, depending on which parameter path you're writing to.

## How We Found Out

We were wiring up the speaker outputs. The speakers live on physical outputs 7 and 8, and they're supposed to carry the left and right sides of Matrix 1, our speaker mix. We set both outputs to source from Matrix 1, and the speakers played back in mono. Both sides were getting the same signal.

The problem was stereo indexing. Matrix 1 Left is index 1, Matrix 1 Right is index 2. We'd set both outputs to `in=1`, thinking we were saying "Matrix 1." We were actually saying "Matrix 1 Left" twice. Output 8 needed `in=2` to get the right side.

That one was easy to diagnose because mono is obvious -- you can hear it immediately if you know what to listen for. The more dangerous version is when you're routing to the wrong bus entirely and the wrong bus happens to have signal on it. You hear something, it sounds plausible enough that you don't question it, and you spend the rest of the session processing through the wrong chain without realizing it.

## The Mental Math Problem

The formula for stereo indexing is straightforward once you know it exists: left channel is `(N * 2) - 1`, right channel is `N * 2`. Bus 5 Left is 9, Bus 5 Right is 10. Bus 8 Left is 15, Bus 8 Right is 16.

But here's the thing -- you don't always remember which context you're in. When you're deep in a routing session, setting up USR inputs and output assignments and bus sends one after another, your brain settles into whatever numbering scheme it used last. If you just set up three USR inputs using simple numbering, your fingers are going to type `in=8` for the next thing too, even if the next thing is an output assignment that needs stereo indexing.

We got this wrong multiple times before we started treating it as a rule instead of something we'd "just remember." The session lessons doc now has a permanent entry about it, and we still occasionally catch ourselves reaching for the wrong number.

## The Only Fix: Read It Back

We stopped trusting that our routing commands did what we intended. Every time we set a routing parameter now, we read the full node back immediately. Not just the value we set -- the entire node, so we can see the source group, the index, and the resolved signal all at once. If the node dump shows a bus name we didn't expect, we know the indexing is wrong before any signal flows.

This is the kind of thing that would be a non-issue if the Wing used consistent numbering everywhere, or if it at least told you which scheme a given parameter expects. It doesn't. The parameter accepts any integer you give it and routes accordingly, with total confidence, to whatever that number means in its particular context. No warning, no validation, no "did you mean Bus 8 or Bus 4 Right?"

The lesson is one we keep relearning in different forms: on a digital console, "set and forget" is "set and regret." Always verify. The Wing is not going to tell you that you're speaking the wrong dialect. It's just going to send your signal somewhere you didn't intend and wait patiently for you to notice.
