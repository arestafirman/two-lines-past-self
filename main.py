"""Two Lines to Your Past Self — "14 March, Row Three, Red Coat".

Why this text: it names one concrete, dated moment (the last ten minutes
of the lecture on 14 March) and one literal, measurable consequence.
Staying means meeting the woman in the red coat in row three — the one
you marry. Leaving early costs exactly four years, eleven first dates,
and one very bad haircut spent trying to find her again. The second line
is the receipt: the price of the advice, counted out loud, so the first
line's warning lands instead of reading as vague wisdom.
"""

import os

ENTRY = (
    "Stay for the last ten minutes of the lecture on 14 March \u2014 "
    "the woman in the red coat in row three is the one you marry.\n"
    "Leave early and you spend four years, eleven first dates, "
    "and one very bad haircut trying to find her again."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
