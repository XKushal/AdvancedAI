def choose_action(current_temperature, target_temperature):
	tolerance = 1

	if current_temperature < target_temperature - tolerance:
		return "TURN_HEAT_ON"
	elif current_temperature > target_temperature + tolerance:
		return "TURN_AC_ON"
	else:
		return "DO_NOTHING"

def main():
	current_temperature = float(input("current_temperature: "))
	target_temperature = float(input("target_temperature: "))

	action = choose_action(current_temperature, target_temperature)

	print(f"Current temperature: {current_temperature}")
	print(f"Target temperature: {target_temperature}")
	print(f"Agent action: {action}")

if __name__ == '__main__':
	main()

