def caesar_cipher(text, shift):
	'''Takes in text from the user and the number the user wants to shift the text too, returns the shifted text.'''
	if len(text) == 0:
		return ""
	character = text[0]
	character = ord(character)
	shift = int(shift)
	if character <= asciiMax - shift:
		character += shift

	# Terminating Case
	elif character <= asciiMax:
		character = character - asciiMax + asciiMin + shift
	character = chr(character)
	
	return character + caesar_cipher(text[1:], shift)

# Created variables to represent ascii minimum and maximum
asciiMin = 31
asciiMax = 126