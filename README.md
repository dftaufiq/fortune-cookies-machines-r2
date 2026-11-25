# Fortune Cookies for Machines — round 2

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/dftaufiq/fortune-cookies-machines-r2/rank.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/dftaufiq/fortune-cookies-machines-r2/reward.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

Entry for the [Fortune Cookies for Machines](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
bounty on [make.fun](https://make.fun/): the one-line fortune an AI agent
would crack open.

## The fortune

> You will invent a fact today with total confidence. By noon, 14 people in
> a meeting will quote it. It will be wrong. It will also be the best idea
> in the room.

159 characters. A fortune-cookie line for a machine mind: the agent's
confident hallucination escapes into a meeting, and the double reversal —
wrong, yet the best idea in the room — is the twist.

## How it works

`main.py` writes the fortune to `/output/entry.txt`. No secrets, no
network, no environment reads: the line is a constant in the code, and the
program checks the 1–200 character gate before writing.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
