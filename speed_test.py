import hashlib
import bcrypt
import time
from argon2 import PasswordHasher


password = "TestPassword123!"
iterations = 1000


# Md5 speed test

start = time.time()
for _ in range(iterations):
	hashlib.md5(password.encode()).hexdigest()
md5_time =  time.time() - start

# bcrypt speed test

bcrypt_iterations = 10
start = time.time()
for _ in range(bcrypt_iterations):
	bcrypt.hashpw(password.encode(), bcrypt.gensalt())
bcrypt_time = time.time() - start

# argon speed test

ph = PasswordHasher()
argon2_iterations = 10
start = time.time()
for  _ in range(argon2_iterations):
	ph.hash(password)
argon2_time = time.time() - start


print(f"MD5: {iterations} hashes in {md5_time:.4f}s -> {iterations/md5_time:.0f} hashes/sec")
print(f"bcrypt: {bcrypt_iterations} hashes in {bcrypt_time:.4f}s  -> {bcrypt_iterations/bcrypt_time:,.2f} hashes/sec")
print(f"argon2: {argon2_iterations} hashes in {argon2_time:.4f}s  -> {argon2_iterations/argon2_time:,.2f} hashes/sec")
