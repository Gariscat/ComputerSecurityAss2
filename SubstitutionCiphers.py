from typing import Any, Tuple
import matplotlib.pyplot as plt
from pprint import pprint

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = ALPHABET.lower()

with open('sub-cipher.txt', 'r') as f:
    cipher = f.read()


def update(d: dict, k: Any):
    if k in d.keys():
        d[k] += 1
    else:
        d[k] = 1


m = dict()
def replace(txt: str, mapping: Tuple[str, str]):
    for x, y in zip(mapping[0], mapping[1]):
        m[x] = y
    ret = []
    for c in txt:
        ret.append(m[c].lower() if c in m.keys() else c)
    return ''.join(ret)


count = {1: dict(), 2: dict(), 3: dict()}
for i in range(len(cipher)):
    for j in (1, 2, 3):
        if i + j < len(cipher) and ' ' not in cipher[i:i + j]:
            update(count[j], cipher[i:i + j])

for j in (1, 2, 3):
    counter = sorted(count[j].items(), key=lambda t: -t[1])
    x = [_[0] for _ in counter]
    y = [_[1] for _ in counter]
    """plt.figure(figsize=(len(x), 4))
    plt.bar(x, y)
    plt.show()
    plt.close()"""
    print(counter)

pprint(cipher)

# VJ - th
# JG - he
cipher = replace(cipher, ('VJG', 'the'))
pprint(cipher)

# Observe words "Ct" and "C". We can determine "C" is either "A" or "I".
# Observe that there are a large number of "CPK". It is very likely that "CPK" is "AND".
# Also we notice the word "thCt". Then, we could almost surely assert "C" is "A".
cipher = replace(cipher, ('CPK', 'and'))
pprint(cipher)

# Observe "Ot" and "Ontended". We know "O" is "i".
cipher = replace(cipher, ('O', 'i'))
pprint(cipher)

# Observe "Ean". We know "E" is "c".
cipher = replace(cipher, ('E', 'c'))
pprint(cipher)

# Observe "intQ". We know "Q" is "o".
cipher = replace(cipher, ('Q', 'o'))
pprint(cipher)

# Observe "eHHicient" and "oTdeT". We know "H" is "f" and "T" is "r".
cipher = replace(cipher, ('HT', 'fr'))
pprint(cipher)

# "thoDUandU" implies D-u and U-s
cipher = replace(cipher, ('DU', 'us'))
pprint(cipher)

# "techniSues" implies S-q
cipher = replace(cipher, ('S', 'q'))
pprint(cipher)

# "aYare" and "Yas" imply Y-w
cipher = replace(cipher, ('Y', 'w'))
pprint(cipher)

# "ciRhers" and "reciRient" imply R-p
cipher = replace(cipher, ('R', 'p'))
pprint(cipher)

# "Aears" and "theA" imply A-y
cipher = replace(cipher, ('A', 'y'))
pprint(cipher)

# "inforFation" and "FotiXated" imply F-m and X-v
cipher = replace(cipher, ('FX', 'mv'))
pprint(cipher)

# "aNN" and "rivaN" imply N-l
cipher = replace(cipher, ('N', 'l'))
pprint(cipher)

# "fallinI" and "revealinI" imply I-g

cipher = replace(cipher, ('I', 'g'))
pprint(cipher)

"""for X in ALPHABET:
    if X not in m.keys():
        print(X)
for x in alphabet:
    if x not in m.values():
        print(x)"""

# "Ween" and "Wetraying" imply W-b
# "Bings" is likely to be "kings" based on contextual information
cipher = replace(cipher, ('W', 'b'))
cipher = replace(cipher, ('B', 'k'))
pprint(cipher)

for ch in cipher:
    assert ch == ch.lower()
# Decoding finished

for ch in ALPHABET:
    if ch not in m.keys():
        m[ch] = '_'

print('Decoder is as follows.')
print(m)
print(cipher)