#! python3
## mobileNumRecog.py - finds mobile numbers in a string input 
## and displays them accordingly
## mobile numbers must be in the format ddd-ddd-dddd for this
## program to work

#defining the main function
def isphoneNum(arg):

    #first check - total length of mobile number should be 12 including
    # the character '-'
    if len(arg) != 12:
        return False

    #first three characters shoud be integers
    for i in range(0,3):
        if not arg[i].isdecimal():
            return False

    #second check - presence of special character '-' after first three
    # digits of the number
    if arg[3] != '-':
        return False

    #further check for number digits
    for i in range(4,7):
        if not arg[i].isdecimal():
            return False

    # check for special character
    if arg[7] != '-':
        return False

    #check for number digits
    for i in range(8,12):
        if not arg[i].isdecimal():
            return False
    return True

# Testing statements used previously to verify code
# print(isphoneNum('905-922-5292'))
# print(isphoneNum('9059225292'))

# Input statement where d = digit
print('Enter the data to check for mobile numbers in the format ddd-ddd-dddd')
message = input()

# looping through data to check for mobile numbers
for i in range(len(message)):
    chunk = message[i:i + 12]
    if isphoneNum(chunk):
        print('Phone number found: ', chunk)
print('That was all')