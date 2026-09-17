import re

def check_strength(password):
	score = 0
	feedback = []

	#Length check
	if len(password) >= 12:
		score += 2
	elif len(password) >= 8:
		score += 1
	else:
	    feedback.append(" Password too short; use at lease 12 characters")

	# Password character Check
	if re.search(r'[a-z]', password):
		score  += 1
	else:
	    feedback.append("Add lowercase letters")
	if re.search(r'\d', password):
		score += 1
	else: 
	     feedback.append("Please add numbers")
	if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
		score += 1
	else:
	    feedback.append("Please add special characters")

	#Check for common words
	common_words = ['123', 'password', 'qwerty', 'abc', 'letmein', 'pa$$w0rd']
	if any(p in password.lower() for p in  common_words):
		score -= 2
		feedback.append("Please avoid common words")


	#Check for repeated  character
	if re.search(r'(.)\1{2,}', password):
		score -= 1
		feedback.append("Please avoid repeated characters like aaa, 111")

	#Password Ratings
	rating = "Weak"
	if score >= 6:
		rating = "Strong"
	elif score >= 3:
		rating = "Moderate"
	return rating, score, feedback


if __name__ == "__main__":
	pw = input("Enter a password to Check: ")
	rating, score, feedback = check_strength(pw)
	print(f"\nRating: {rating} (score: {score})")
	if feedback:
		print("Suggestions:")
		for f in feedback:
			print(f" - {f}")

