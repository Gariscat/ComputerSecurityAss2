from typing import List, Tuple, Any
# import enchant
# D = enchant.Dict("en_US")


def xor(msg, pad):
    """Encrypts message `msg' using Ben's One-time-pad with feedback
    algorithm"""
    assert len(msg) == len(pad)
    result = []
    for i in range(len(msg)):
        c = msg[i] ^ pad[i]
        result.append(c)
    return result


A = [int(x, 16) for x in 'e9 3a e9 c5 fc 73 55 d5'.split()]
B = [int(x, 16) for x in 'f4 3a fe c7 e1 68 4a df'.split()]


alpha_asciis = [ord(x) for x in 'abcdefghijklmnop'+'abcdefghijklmnop'.upper()]
print(alpha_asciis)
with open('words_alpha.txt', 'r') as f:
    corpus = f.readlines()
    corpus = [s[:-1] for s in corpus]  # strip the '\n' suffix
    print('number of words:', len(corpus))
    candidates = [s for s in corpus if len(s) == 8]
    for i in range(len(candidates)):
        candidates.append((candidates[i].capitalize()))
    print('number of 8-character words:', len(candidates))
    # print('examples:', candidates)


def valid(y: int):
    return y in alpha_asciis or y+32 in alpha_asciis


def checkword(w: str):
    return w in candidates
    # return D.check(w)


def exclude(words: List[str], dec: Any):
    for d in dec:
        ds = ''.join(d)
        for word in words:
            if word in ds:
                return True
    return False


def search(cur_step: int, tot_step: int, ciphers: Any, keys: List[int], dec: Any):
    """if sum(['y' in ''.join(d) for d in dec]):
        return False
    if sum(['v' in ''.join(d) for d in dec]):
        return False
    if sum(['x' in ''.join(d) for d in dec]):
        return False
    if sum(['z' in ''.join(d) for d in dec]):
        return False"""
    # print(keys)
    if exclude(['pp', 'mj', 'mk'], dec):
        return False
    if cur_step == tot_step:
        words = [''.join(d) for d in dec]
        print(words)
        ok = True
        for word in words:
            if checkword(word) is False:
                ok = False
                break
        if ok:
            return True
        else:
            return False

    for x in range(128):
        all_is_alpha = sum([valid(cipher[cur_step] ^ x) for cipher in ciphers]) == len(ciphers)
        if all_is_alpha:
            ans.append(x)
            for d, cipher in zip(dec, ciphers):
                d.append(chr(cipher[cur_step] ^ x))

            found = search(cur_step+1, tot_step, ciphers, ans, dec)
            if found:
                return found
            else:
                ans.pop(-1)
                for d in dec:
                    d.pop(-1)
    return False


if __name__ == '__main__':
    ans = []
    decrypted = [[], []]
    search(0, 8, (A, B), ans, decrypted)