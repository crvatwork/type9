import base64
import random
import scrypt
import sys


NORMAL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
CUSTOM = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def randomize_salt():
    return "".join(
        random.choices(
            CUSTOM,
            k=14
            )
        )


def generate_hash(salt, plain):
    h = scrypt.hash(
        plain,
        salt,
        N=16384,
        r=1,
        p=1,
        buflen=32
        )
    h = str(
        base64.b64encode(h)
        )[2:-1]
    return h.translate(
        str().maketrans(
            NORMAL,
            CUSTOM,
            "="
            )
        )

def main():
    if len(sys.argv) == 3 and len(sys.argv[1]) == 14:
        salt = sys.argv[1]
        plain = sys.argv[2]
    elif len(sys.argv) == 2:
        salt = randomize_salt()
        plain = sys.argv[1]
    else:
        sys.exit(
            "This program accepts either a salt and a plain-text password or a plain-text password."
            )

    h = generate_hash(salt, plain)
    print(f"$9${salt}${h}")
