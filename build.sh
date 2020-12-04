#!/usr/bin/env bash


DOCKERFILE=$(mktemp -p .)
SCRIPT=$(mktemp -p .)

cat <<EOF > $DOCKERFILE
FROM fedora:33
RUN dnf install -y python3-scrypt
COPY $SCRIPT /type9.py
RUN chmod +x /type9.py
ENTRYPOINT ["/type9.py"]
CMD ["/usr/bin/bash"]
EOF

cat <<\EOF > $SCRIPT
#!/usr/bin/env python3


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
    hash = scrypt.hash(
        plain,
        salt,
        N=16384,
        r=1,
        p=1,
        buflen=32
        )
    hash = str(
        base64.b64encode(hash)
        )[2:-1]
    return hash.translate(
        str().maketrans(
            NORMAL,
            CUSTOM,
            "="
            )
        )


if len(sys.argv) == 3 and len(sys.argv[1]) == 14:
    salt = sys.argv[1]
    plain = sys.argv[2]
elif len(sys.argv) == 2:
    salt = randomize_salt()
    plain = sys.argv[1]

hash = generate_hash(salt, plain)
print(f"$9${salt}${hash}")
EOF

podman build -t type9 -f $DOCKERFILE

rm $DOCKERFILE $SCRIPT
