"""Make the Judge Smile — u-gentle-badger-68-make-the-judge-smile-9228676d.

Writes one line (at most 200 characters) about a small good thing that
happened today to /output/entry.txt, where the sealed scorer gates it and the
judge compares it two at a time.

Standard library only, fully deterministic: the same line is written on every
run. The candidate list holds the lines drafted for this competition in
judged order; SELECTED picks the winner of the head-to-head judging in
FIELD.md (candidate F). Rounds reorder this list only when a new candidate
beats the live one on the kit rubric (subject, warmth, surprise, one
concrete detail, fresh wording).
"""

import os
import sys

# Candidates in judged order; index 0 is the submitted line.
CANDIDATES = [
    # F — winner, round 3. Two turns: poured anyway despite short payment,
    # and the repayment demanded is itself a kindness. Round 3 added the
    # giver's scarcity ("from his last jug") so the warmth no longer leans on
    # grief the way the field's best line does, and kept the exact time anchor.
    "At 6:04 this morning the old iced-tea man counted my coins, found me "
    "short, and poured anyway, from his last jug \u2014 whispered, 'Pay me "
    "back by telling someone else their laugh sounds like rain.'",
    # L — postman circle-back. Two turns, thinner warmth than F.
    "I held the lift for the postman this morning; at noon he came back, "
    "knocked, and handed me the letter I'd been waiting three weeks for \u2014 "
    "he'd carried it in his pocket since dawn.",
    # O — Tuesday coffee ritual. Freshest single phrase, one turn only.
    "This morning a stranger paid for my coffee and left before I could thank "
    "him; the barista shrugged and said, 'He does it every Tuesday \u2014 calls "
    "it rent for the good days.'",
    # Q — flower seller in the flood. Warmest sacrifice, one turn.
    "This morning the flower seller, whose stall floods every rain, pressed a "
    "wet frangipani into my hand and said, 'Take it \u2014 somebody should "
    "carry something dry home today.'",
]

SELECTED = 0

MAX_CHARS = 200


def validate(line):
    """Mirror the sealed gate: UTF-8 text, 1 to 200 characters, not blank."""
    if not isinstance(line, str):
        raise TypeError("entry must be text")
    line.encode("utf-8")
    if not line.strip():
        raise ValueError("entry must not be only white space")
    if len(line) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200 limit" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main():
    line = validate(CANDIDATES[SELECTED])
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read back and confirm the file holds exactly the validated line, so a
    # run that writes something else fails loudly instead of shipping it.
    with open(path, encoding="utf-8", newline="") as f:
        if f.read() != line:
            raise ValueError("read-back mismatch on %s" % path)
    print("wrote %s (%d chars)" % (path, len(line)))
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
