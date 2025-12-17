import hashlib
import itertools
import string
import time
import bcrypt
import argon2

def bcrypt_hash(password: str) -> str:
    """Hash a password with bcrypt (slow by design)."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

def argon2_hash(password: str) -> str:
    """Hash a password with Argon2 (memory-hard)."""
    ph = argon2.PasswordHasher()
    return ph.hash(password)

def brute_force_runtime(password, algo="md5"):
    charset = string.ascii_lowercase
    attempts = 0
    start = time.time()
    
    target = hashlib.md5(password.encode()).hexdigest() if algo == "md5" else hashlib.sha256(password.encode()).hexdigest()
    
    for guess in itertools.product(charset, repeat=len(password)):
        attempts += 1
        candidate = "".join(guess).encode()
        h = hashlib.md5(candidate).hexdigest() if algo == "md5" else hashlib.sha256(candidate).hexdigest()
        if h == target:
            end = time.time()
            return attempts, end - start
    return attempts, time.time() - start

def measure_entropy():
    lengths = [3, 4, 5]
    md5_times, sha_times, md5_attempts, sha_attempts = [], [], [], []
    
    for L in lengths:
        pwd = "a" * L
        attempts_md5, time_md5 = brute_force_runtime(pwd, "md5")
        attempts_sha, time_sha = brute_force_runtime(pwd, "sha256")
        md5_times.append(time_md5)
        sha_times.append(time_sha)
        md5_attempts.append(attempts_md5)
        sha_attempts.append(attempts_sha)
    
    return lengths, md5_times, sha_times, md5_attempts, sha_attempts