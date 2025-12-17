import hashlib
import bcrypt
import random
import string

def random_password(length=6):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def simulate_hash_cracking():
    password = random_password()
    
    # Weak hash (MD5)
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    md5_attempts = brute_force(password, "md5")
    
    # Strong hash (bcrypt)
    bcrypt_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    bcrypt_attempts = brute_force(password, "bcrypt", bcrypt_hash)
    
    return {
        "MD5": md5_attempts,
        "bcrypt": bcrypt_attempts
    }

def brute_force(password, algo, bcrypt_hash=None):
    attempts = []
    charset = string.ascii_lowercase
    guess_count = 0
    
    for guess in charset:
        guess_count += 1
        if algo == "md5":
            if hashlib.md5(guess.encode()).hexdigest() == hashlib.md5(password.encode()).hexdigest():
                attempts.append(guess_count)
                break
        elif algo == "bcrypt":
            if bcrypt.checkpw(password.encode(), bcrypt_hash):
                attempts.append(guess_count)
                break
        attempts.append(guess_count)
    return attempts