import sys

def calculate_risk_score(failed_attempts, is_device_known, is_location_unusual, login_time):
	total_risk_score = 0
	risk_factors = []
	risk_analysis = {}

	if failed_attempts >= 5:
		total_risk_score += 3
		risk_factors.append("- Five or more failed attempts.")
	elif failed_attempts > 2 and failed_attempts < 5:
		total_risk_score += 2
		risk_factors.append("- More than 2 failed attempts. Still less than 5.")

	if not is_device_known:
		total_risk_score += 2
		risk_factors.append("- Unknown device.")

	if is_location_unusual:
		total_risk_score += 2
		risk_factors.append("- Unusual location.")

	if login_time >= 0 and login_time <= 5:
		total_risk_score += 1
		risk_factors.append("- Late-night login.")

	risk_analysis["total_risk_score"] = total_risk_score
	risk_analysis["risk_factors"] = risk_factors

	return risk_analysis

def choose_action(total_risk_score):
	if total_risk_score <= 2:
		return "ALLOW_LOGIN"
	elif total_risk_score >= 6:
		return "BLOCK_AND_ALERT"
	else:
		return "REQUIRE_MFA"

def get_integer(prompt, minimum, maximum):
	prompt = input(prompt)
	prompt = valid_integer(prompt)
	while prompt < minimum or prompt > maximum:
		print(f"Invalid selection: {prompt}.")
		prompt = input(f"Enter a valid integer range ({minimum}, {maximum}): ")
		prompt = valid_integer(prompt)
	return prompt

def valid_integer(prompt):
	while True:
		try:
			prompt = int(prompt)
			break
		except ValueError:
			prompt = input(f"Invalid selection: {prompt}. Enter an integer.")
	return prompt

def get_yes_no(prompt):
	prompt = input(prompt).lower()
	valid_selection = ["yes", "y", "no", 'n']
	while prompt not in valid_selection:
		print(f"Invalid selection: {prompt}. Accepted (yes, y, no, n).")
		prompt = input("Enter a valid selection: ").lower()
	if prompt == "y" or prompt == "yes":
		return True
	elif prompt == "n" or prompt == "no":
		return False



def login_protection():

	failed_attempts = "Number of failed attempts: "
	failed_attempts = get_integer(failed_attempts, 0, sys.maxsize)
	
	is_device_known = "Is this a known device? "
	is_device_known = get_yes_no(is_device_known)

	is_location_unusual = "Is the location unusual? "
	is_location_unusual = get_yes_no(is_location_unusual)

	login_time = "login hour (0-23): "
	login_time = get_integer(login_time, 0, 23)


	risk_analysis = calculate_risk_score(failed_attempts, is_device_known, is_location_unusual, login_time)
	total_risk_score = risk_analysis.get("total_risk_score")

	action = choose_action(total_risk_score)

	print("\n----- Login Risk Report -----")
	print(f"Risk score: {total_risk_score}")
	print(f"Decision: {action} \n")
	print("Risk factors: ")

	if len(risk_analysis.get("risk_factors")) < 1:
		print("- No risk factors detected.")
	else:
		for risk in risk_analysis.get("risk_factors"):
			print(risk)


if __name__ == '__main__':
	login_protection()


