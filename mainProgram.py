import caesar_shift

text = input("Dear wonderful user, please enter a string: ")

x = input("Then, please enter a shift number: ")

print("Your shifter string is : {}".format(caesar_shift.caesar_shift(text, x)))