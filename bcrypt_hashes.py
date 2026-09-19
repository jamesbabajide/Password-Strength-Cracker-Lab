import bcrypt

with open('password_test.txt') as f:
	passwords= [line.strip() for line in f if line.strip()]

with open('bcrypt_hashes.txt', 'w') as out:
	for pw in passwords:
		hashed =  bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
		print(f"{pw} -> {hashed.decode()}")
		out.write(hashed.decode() + '\n')


