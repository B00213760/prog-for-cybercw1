# Task 3 - IP Address Validator
# This program checks whether an IP address has a valid format

# Step 1 - Create a function to validate an IP address
def validate_ip(ip_address):

    # Step 2 - Remove unnecessary spaces from the IP address
    ip_address = ip_address.strip()
    
    # Step 3 - Check that the IP address contains exactly three dots
    if ip_address.count(".") != 3:
        return False
	# Step 4 - Split the IP address into its four octets
    octets = ip_address.split(".")
    # Step 5 - Check that the IP address contains exactly four octets
    if len(octets) != 4:
        return False
    # Step 6 - Check that each octet contains only numbers
    for octet in octets:
        if not octet.isdigit():
            return False
        # Step 7 - Check that each octet is between 0 and 255
        number = int(octet)
        if number < 0 or number > 255:
            return False
    # Step 8 - Return True if all validation checks have passed
    return True
# Step 9 - Ask the user to enter an IP address
user_ip = input("Enter an IP address: ")
# Step 10 - Check the IP address and display the result
if validate_ip(user_ip):
	print("Valid IP address")
else:
	print("Invalid IP address")