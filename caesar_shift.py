def caesar_cipher(text, shift):
	'''Takes in text from the user and the number the user wants to shift the text too, returns the shifted text.'''
	if len(text) == 0:
		return ""
	character = text[0]
	character = ord(character)
	
	if character <= 126 - shift:
		character += shift

	# Terminating Case
	elif character <= 126:
		character = character - 126 + 31 + shift
	character = chr(character)
	
	return character + caesar_cipher(text[1:], shift)