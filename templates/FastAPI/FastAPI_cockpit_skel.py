from fastapi import FastAPI
from modules.entropy_utils import measure_entropy, bcrypt_hash, argon2_hash
from modules.wallet_utils import generate_seed, brute_force_seed
from modules.contract_utils import VulnerableContract, PatchedContract
from modules.mining_utils import mine_block
from modules.robotics_utils import forward_kinematics

app = FastAPI(title="BugBot Cockpit")

@app.get("/")
def index():
    return {"message": "Welcome to BugBot Cockpit (FastAPI)"}

@app.get("/entropy-arena")
def entropy_arena():
    lengths, md5_times, sha_times, md5_attempts, sha_attempts = measure_entropy()
    return {
        "lengths": lengths,
        "md5_times": md5_times,
        "sha_times": sha_times,
        "md5_attempts": md5_attempts,
        "sha_attempts": sha_attempts
    }

@app.get("/entropy-arena-advanced")
def entropy_arena_advanced(password: str = "hunter2"):
    return {
        "bcrypt": bcrypt_hash(password),
        "argon2": argon2_hash(password)
    }

@app.get("/wallet-arena")
def wallet_arena(length: int = 3):
    seed = generate_seed(length)
    attempts, runtime, found = brute_force_seed(seed, length)
    return {"seed": seed, "attempts": attempts, "runtime": runtime, "found": found}

@app.get("/contract-arena")
def contract_arena(attack: bool = True):
    vuln = VulnerableContract()
    patched = PatchedContract()
    if attack:
        vuln.withdraw(10, lambda amt, c: c.withdraw(10))
    return {"vulnerable_balance": vuln.balance, "patched_balance": patched.balance}

@app.get("/mining-arena")
def mining_arena(difficulty: int = 4):
    nonce, h, runtime = mine_block(difficulty)
    return {"nonce": nonce, "hash": h, "runtime": runtime}

@app.get("/robotics-arena")
def robotics_arena(theta1: float = 0.5, theta2: float = 0.5):
    x, y = forward_kinematics(theta1, theta2)
    return {"theta1": theta1, "theta2": theta2, "x": x, "y": y}