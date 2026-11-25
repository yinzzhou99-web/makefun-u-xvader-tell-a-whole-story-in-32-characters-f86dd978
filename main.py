"""Write the entry name for Tell a Whole Story in 32 Characters.

One Wi-Fi network name, 20 characters: a husband left for 5G. The
joke lands first (he left her for a network, not a person) and the
few words imply the whole story — a marriage that lost to the
internet speed. No input, no network, stdlib only.
"""

import os

NAME = "MyHusbandLeftMeFor5G"

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> None:
    # The gate allows 1-32 characters; the name is 20, so it passes
    # as written and no trimming or truncation is ever needed.
    os.makedirs(OUT_DIR, exist_ok=True)
    fd = os.open(OUT_PATH, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, (NAME + "\n").encode("utf-8"))
    finally:
        os.close(fd)


if __name__ == "__main__":
    main()
