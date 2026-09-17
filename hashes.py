import hashlib
with open('password_test.txt') as f:
	for pw in f:
		pw = pw.strip()
		print(hashlib.md5(pw.encode()).hexdigest())
