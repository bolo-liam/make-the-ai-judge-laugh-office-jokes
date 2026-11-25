"""Make the AI Judge Laugh: Office Jokes — entry program.

Scores six original one-line office jokes against the judge's five
criteria (weights 5/4/3/2/1, most important first) and writes the
winner to /output/entry.txt. Gate: 1-199 characters, UTF-8, non-blank.
Python 3.13, standard library only.
"""

import os

# Judge criteria, most important first:
# 1. genuine one-line joke about office life (weight 5)
# 2. real turn or surprise at the end (weight 4)
# 3. recognition — truth of the office (weight 3)
# 4. tight wording (weight 2)
# 5. freshness (weight 1)
WEIGHTS = (5, 4, 3, 2, 1)

# Each candidate: (text, scores per criterion, 0-5).
CANDIDATES = [
    (
        "I replied-all to say 'please stop replying-all.' "
        "The thread now has 47 messages and a calendar invite to discuss it.",
        (5, 5, 5, 4, 4),
    ),
    (
        "Our printer has been 'out of toner' since March. HR calls it "
        "team-building: we bond over the walk to the other floor.",
        (5, 4, 5, 4, 3),
    ),
    (
        "The office plant died in 2019. Nobody noticed, so Facilities "
        "gave it a promotion and a corner office.",
        (5, 5, 3, 4, 5),
    ),
    (
        "I set my status to 'in a meeting' and went to the kitchen. "
        "My boss did the same. We nodded like two spies.",
        (5, 4, 4, 4, 4),
    ),
    (
        "Reply-all is the office's group therapy: nobody asked for it, "
        "everyone attends, and the bill is your inbox.",
        (4, 4, 5, 5, 3),
    ),
    (
        "My out-of-office reply is the only coworker who answers emails "
        "on time — and it left the company years ago.",
        (4, 4, 4, 4, 3),
    ),
]


def score(candidate):
    text, marks = candidate
    return sum(w * m for w, m in zip(WEIGHTS, marks))


def pick():
    valid = [c for c in CANDIDATES if 1 <= len(c[0]) <= 199 and c[0].strip()]
    if not valid:
        raise SystemExit("no candidate passes the 1-199 character gate")
    # Highest score wins; on a tie the shorter text wins — tighter
    # wording is itself one of the judge's criteria.
    return max(valid, key=lambda c: (score(c), -len(c[0])))


def main():
    winner, _ = pick()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(winner)
    print(winner)
    print(f"chars: {len(winner)}")


if __name__ == "__main__":
    main()
