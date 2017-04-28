# text represents the string and x is the number of digits
def caesar_shift(text, shift):
	if len(text) == 0:
		return 0
	character = text[0]
	character = ord(character)
	shift = int(shift)
	character += shift
	if character > 126:
			character = character - 95
		
	return text[0] + caesar_shift(text[1:]) 
	
	# Terminating Case
	
print(caesar_shift("hello", 1))
	
	
