import random

HUGBOT_NAME = 'Henrietta'

boot_options = [True, False]
hugbot_actions = ['hug', 'wave', 'highfive']	
action_map = {
	'dance': "dancing like noBOTy is watching", 
	'sing': "singing better than yo mama", 
	'yoga': "breathing in and out. namBOTste."
	}

def get_name():
	return HUGBOT_NAME

def speak(message):
	print message


def hug():
	speak("**hug**")

def boot():
	# speak("Hello, my name is " + HUGBOT_NAME)
	bot_name = get_name()
	speak("Hello, my name is " + bot_name)

	speak("One moment. Booting up!")
	# my code
	return random.choice(boot_options)
	# code from class below
	#random_outcome = random.choice(boot_options)
	#return random_outcome

def wave():
	speak("**wave**")	

def highfive():
	speak("*****highfive*****")	

def perform_action(verb):
	name_returned = get_name()
	speak(name_returned + " " + action_map[verb])
	return
# perform_action(raw_input)		


def brain():
	booted_ok = boot()
	if booted_ok:
		while True:
			action = raw_input("What should Hugbot do? Dance, sing, or yoga?" + " ")
			if action not in action_map:
				speak(get_name() + " " "doesn't know how to" + " " + action + " " + "yet!")
			else: 
				perform_action(action)
				return
			# if action == 'sing':
			# 	perform_action('sing')	
			# 	return
			# if action == 'yoga':
			# 	perform_action('yoga')
			# 	return
	else:
		speak("Error in system boot up")				
				



brain()