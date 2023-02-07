from typing import List, Tuple, Any
import nltk
from itertools import product
from tqdm import tqdm
from trie import Trie
"""
import enchant
D = enchant.Dict("en_US")
"""
nltk.download('words')


A = [int(x, 16) for x in 'e9 3a e9 c5 fc 73 55 d5'.split()]
B = [int(x, 16) for x in 'f4 3a fe c7 e1 68 4a df'.split()]


Corpus = nltk.corpus.words.words()


def from_corpus(corpus: Any, capitalize: bool = False):
    ret = [s for s in corpus if len(s) == 8]
    if capitalize:
        for i in range(len(ret)):
            ret.append((ret[i].capitalize()))
    print('number of 8-character words:', len(ret))
    return ret
    # print('examples:', candidates)


candidates = from_corpus(Corpus)


def check(a: str, b: str):
    a_id = [ord(_) for _ in a]
    b_id = [ord(_) for _ in b]

    for x, y, z, w in zip(a_id, b_id, A, B):
        if x ^ z ^ y ^ w != 0:
            return False

    return True


if __name__ == '__main__':
    t = Trie()
    for word in candidates:
        t.insert(word)

    lower_alpha_asciis = [ord(x) for x in 'abcdefghijklmnopqrstuvwxyz']
    upper_alpha_asciis = [ord(x) for x in 'abcdefghijklmnopqrstuvwxyz'.upper()]

    cnt = 1
    cp = []
    for i in range(8):
        cp.append([])
        num_pairs = 0
        for x, y in product(lower_alpha_asciis, lower_alpha_asciis):
            if i == 0 and chr(y) in ['x', 'z']:
                continue

            if x ^ A[i] == y ^ B[i]:
                num_pairs += 1
                cp[i].append((chr(x), chr(y)))
        print(f'{i}:', cp[i])
        cnt *= num_pairs

    print(cnt)
    # exit()
    ans = None
    for a, b, c, d, e, f, g, h in tqdm(product(cp[0], cp[1], cp[2], cp[3], cp[4], cp[5], cp[6], cp[7]), total=cnt):
        x = a[0] + b[0] + c[0] + d[0] + e[0] + f[0] + g[0] + h[0]
        y = a[1] + b[1] + c[1] + d[1] + e[1] + f[1] + g[1] + h[1]

        # print(x, y)

        # if D.check(x) and D.check(y):
        if len(t.query(x)) and len(t.query(y)):
            print(x, y)
            ans = [x, y]
            break
    if ans:
        print('decrypted')
        keys = []
        for i in range(8):
            k1 = A[i] ^ ord(ans[0][i])
            k2 = B[i] ^ ord(ans[1][i])
            assert k1 == k2
            keys.append(k1)
        print('keys:', keys)
        """"""
