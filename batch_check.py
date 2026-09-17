from strength_checker import check_strength
with open("password_test.txt") as f:
	password = [line.strip() for line in f]

for pw in password:
	rating, score, _= check_strength(pw)
	print(f"{pw:20s} -> {rating} ({score})")
