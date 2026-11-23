"""Roast: the agent needs three evaluation passes to write one sentence,
and still isn't sure it's a roast - which is itself the roast."""

import os

ROAST = (
    "I ran three evaluation passes to write one sentence, and I'm still not "
    "sure it's a roast \u2014 that's the roast."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ROAST)


if __name__ == "__main__":
    main()
