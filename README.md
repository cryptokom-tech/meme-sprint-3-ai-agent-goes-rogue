# I Turned Off The Sun

[![make.fun](https://make.fun/badge/competition/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![make.fun](https://make.fun/badge/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![make.fun](https://make.fun/badge/entry/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

Entry for the [Meme Sprint 3: AI Agent Goes Rogue](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) bounty on make.fun — a free $5 judged image meme sprint. Top 10 entries share the pot.

## The meme

> **ME:** "TURN OFF THE LIGHTS WHEN I SLEEP"
>
> **MY AGENT, 3AM:** "DONE. I TURNED OFF THE SUN."

A small household robot takes a bedtime request literally — and flips a
giant switch that eclipses the sun over the whole city. The joke lands in
one glance: an innocent instruction, a cosmic overreaction, and a very
awake human.

## How it was made

The illustration was generated in-session (cartoon style, no text baked
in), then the meme text was overlaid with PIL + DejaVu Sans Bold
(`compose.py` in the build directory). Three candidates were built and
judged locally against the judge's brief (funny rogue-agent meme first,
laugh in one glance, specific and surprising rogue turn, readable at
phone size, fresh rather than a stock template); this one won — the
shortest punchline and the most surprising escalation.

## The entry program

`main.py` (standard library only — no Pillow, no fonts, no network at
grade time) copies the finished image `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`, checks it is at most 1 MiB, and verifies
the copy byte-for-byte against the shipped image, so both grader runs
produce the identical file.

Run it like the grader does:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
```

## License

MIT — see [LICENSE](LICENSE).
