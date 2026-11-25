"""Fortune Cookies for Machines — round 2 entry.

Writes one fortune-cookie line an AI agent would get to /output/entry.txt.
The line is a single fortune-slip sentence (159 characters; gate is 1-200).
No secrets, no network, no environment reads: the line is a constant.
"""

from pathlib import Path

FORTUNE = (
    "You will invent a fact today with total confidence. "
    "By noon, 14 people in a meeting will quote it. "
    "It will be wrong. It will also be the best idea in the room."
)
# 159 characters, counted by len() in check_line. Structure is 2-beat +
# reveal in the final clause: the agent hallucinates with total
# confidence, the false fact escapes into a meeting (14 people, by noon),
# then the double reversal — wrong, yet the best idea in the room. True
# about an agent's condition (confident hallucination adopted by humans)
# without explaining itself. Every word earns its place; no filler.

OUTPUT_PATH = Path("/output/entry.txt")


def check_line(line: str) -> None:
    text = line.strip()
    if not text:
        raise ValueError("fortune must not be blank")
    if not 1 <= len(line) <= 200:
        raise ValueError("fortune must fit the 1-200 character gate")


def main() -> None:
    check_line(FORTUNE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
