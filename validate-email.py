print("[&] Coded By Yousuf Shafi'i Muhammad Junior Programmer")

print("")

print("[-] Website muhammadabdirahman.wixsite.com/yousuf9963blog")


print("")

print("[!] legal disclaimer: Usage of this Program for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program")

print("")

print("I hope for you good future and i am willing that you will come high effort.")

print("")

import re

# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Define a function for
# for validating an Email
def check(email):

	# pass the regular expression
	# and the string into the fullmatch() method
	if(re.fullmatch(regex, email)):
		print("valid")

	else:
		print("false")

# Driver Code
if __name__ == '__main__':

	# Enter the email
	email = input("Enter Email:")

	# calling run function
	check(email)






	
