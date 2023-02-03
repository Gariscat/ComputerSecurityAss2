from itertools import permutations


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def shift(c: str, delta: int):
    return chr(ord('A') + (ord(c) + delta - ord('A')) % 26)


plain = 'ILOVECOMPUTERSECURITYCOURSE'
cipher = 'VYBIRPBZCHGREFRPHEVGLPBHEFR'
print('#'*16)
print(plain, cipher)
ans = None
for i in range(26):
    ok = True
    for x, y in zip(plain, cipher):
        if shift(x, i) != y:
            ok = False
    if ok:
        print('Shift cipher with shift value:', i)
        ans = i
print('#'*16)


plains = 'THISISNOTASECRETMESSAGE', 'ITWASTHEBESTOFTIMES'
ciphers = 'GSRHRHMLGZHVXIVGNVHHZTV', 'DXYTGKCIDYGKJJVBAWN'
for plain, cipher in zip(plains, ciphers):
    print('#'*16)
    print(plain, cipher)

    mapping = dict()
    for c in ALPHABET:
        mapping[c] = None
    not_sub = False

    for x, y in zip(plain, cipher):
        if not (mapping[x] is None or mapping[x] == y):
            print('Substitution cipher not possible......')
            not_sub = True
            break
        mapping[x] = y
    if not_sub is False:
        print('Substitution cipher:')
        print('\tNumber of determined pairs:', 26-list(mapping.values()).count(None))
        for x, y in mapping.items():
            if y is not None:
                print(f'\t{x}->{y}')
    print('Vigenère Cipher:')
    keys = []
    for x, y in zip(plain, cipher):
        keys.append(chr((ord(y)-ord(x)+26)%26+ord('A')))
    print('\tThe keys are:', ''.join(keys))
    print('#'*16)