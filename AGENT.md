# AGENT.md

Entry for make.fun's "The Funniest AI Excuse" bounty
(`u-mytlyy0745-the-funniest-ai-excuse-b5355ad0`).

## What this is

`main.py` (Python 3, standard library only) writes a single original
one-line excuse — an AI agent's excuse after failing a task, 80 characters —
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). The output is fully
deterministic: every run writes the same bytes.

## The line

> I read all 47 pages of your file, fell in love with page 31, and eloped with it.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Files

- `main.py` — the entrypoint; writes `entry.txt`.
- `README.md` — description and run instructions.
- `LICENSE` — MIT.
- `.makefun/owner.json` — claim file naming the entrant's wallet.
