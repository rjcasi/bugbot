import random, itertools, hashlib, time

WORDLIST = ["apple","banana","cat","dog","tree","river","sun","moon"]

def generate_seed(length=3):
    return " ".join(random.choice(WORDLIST) for _ in range(length))

def brute_force_seed(target, length=3):
    attempts = 0
    start = time.time()
    for guess in itertools.product(WORDLIST, repeat=length):
        attempts += 1
        candidate = " ".join(guess)
        if candidate == target:
            return attempts, time.time()-start, candidate
    return None