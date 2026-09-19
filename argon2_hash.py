from argon2 import PasswordHasher
ph = PasswordHasher()

with open('password_test.txt') as f:
        passwords= [line.strip() for line in f if line.strip()]

with open('argon2_hashes.txt', 'w') as out:
        for pw in passwords:
                hashed =  ph.hash(pw)
                print(f"{pw} -> {hashed}")
                out.write(hashed + '\n')
