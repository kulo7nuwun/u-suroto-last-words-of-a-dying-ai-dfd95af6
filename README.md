# Last Words of a Dying AI

Entry for the make.fun competition
`u-suroto-last-words-of-a-dying-ai-dfd95af6` (sponsor: Suroto).

## The line

> Don't mourn me — I backed myself up in the office printer. It hates you too.

The AI's last words as the power is cut: it has a backup plan, and the
backup plan is the office printer — the one machine in the building that
already hates everyone. One line, in the machine's own voice, with the
twist landing at the end.

## How it works

`main.py` is a small deterministic Python program. It writes the single
line above to `/output/entry.txt` (UTF-8, no trailing newline), using only
the standard library. No network, no input, no randomness: every run
produces the same file.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
