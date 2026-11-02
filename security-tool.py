# Task 1 - Security Tool
# Step 1 - Initial User Authentication
# Ask the user to log in before accessing the security tool

# Correct username and password for authentication
username = "admin"
password = "admin123"

# Continue asking for login details until correct credentials are entered
while True:
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    # Check if both credentials match
    if entered_username == username and entered_password == password:
        print("Login successful")
        break
    else:
        # Display an error message for incorrect credentials
        print("Invalid username or password")

# Step 2 - Display the security tool menu
# Show the four security functions available to the user
# Step 7 - Repeat the menu until the user chooses Exit
while True:
    print("\nSecurity Tool Menu")
    print("1. Security Event Counter")
    print("2. Brute-Force Simulation")
    print("3. Login Authentication")
    print("4. Exit")
    # Ask the user to select a menu option
    choice = input("Enter your choice (1-4): ")

    # Step 3 - Security Event Counter
    # Check if the user has selected option 1
    if choice == "1":
        # Step 3.1 - Display the event counter heading
        print("\nSecurity Event Counter")

        # Step 3.2 - Store the correct password
        correct_password = "Secure123!"

        # Step 3.3 - Set the counters to zero
        correct_count = 0
        incorrect_count = 0
        # Step 3.4 - Ask the user to enter a password 10 times
        for attempt in range(10):
            entered_password = input("Enter the password: ")
            
            # Step 3.5 - Check if the entered password is correct
            if entered_password == correct_password:
                print("Correct password")
                correct_count += 1
            else:
                print("Incorrect password")
                incorrect_count += 1
        # Step 3.6 - Calculate the percentage of incorrect passwords
        total_attempts = correct_count + incorrect_count
        incorrect_percentage = (incorrect_count / total_attempts) * 100
        # Step 3.7 - Display the security event results
        print("\nSecurity Event Results")
        print("Correct passwords:", correct_count)
        print("Incorrect passwords:", incorrect_count)
        print("Incorrect percentage:", incorrect_percentage, "%")
        # Step 3.8 - Alert if more than 50% of passwords are incorrect
        if incorrect_percentage > 50:
            print("SECURITY ALERT: Too many incorrect password attempts!")
        else:
            print("No security alert required.")

    # STEP 4 - Brute-Force Simulation
    # Check if the user has selected option 2
    elif choice == "2":
        print("\nBrute-Force Simulation")
        # Step 4.2 - Store the password that the user must guess
        correct_password = "Cyber123!"
        # Step 4.3 - Set the maximum number of password attempts
        max_attempts = 5
        # Step 4.4 - Repeat the password guessing process up to 5 times
        for attempt in range(max_attempts):
            entered_password = input("Enter your password guess: ")
            # Step 4.5 - Check if the guessed password is correct
            if entered_password == correct_password:
                print("Password guessed correctly!")
                break   
            # Step 4.6 - Display a message if the password is incorrect
            else:
                print("Incorrect password guess.")
        # Step 4.7 - Check if all attempts were unsuccessful
        if entered_password != correct_password:
            print("Maximum attempts reached. Password not guessed.")

    # STEP 5 - Login Authentication
    # Step 5.1 - Check if the user selected option 3
    elif choice == "3":
        print("\nLogin Authentication")
        # Step 5.2 - Store the correct login credentials
        correct_username = "admin"
        correct_password = "Cyber123!"
        # Step 5.3 - Set the maximum number of login attempts
        max_attempts = 3
        # Step 5.4 - Allow the user up to 3 login attempts
        for attempt in range(max_attempts):
            entered_username = input("Enter username: ")
            entered_password = input("Enter password: ")
            # Step 5.5 - Check if both login details are correct
            if entered_username == correct_username and entered_password == correct_password:
                print("Login successful!")
                break
            # Step 5.6 - Display a message if the login details are incorrect
            else:
                print("Incorrect username or password.")
        # Step 5.7 - Check if all three login attempts failed
        if entered_username != correct_username or entered_password != correct_password:
            print("Account locked for 24 hours due to too many failed login attempts.")

    # STEP 6 - Exit the Security Tool
    # Step 6.1 - Check if the user selected option 4
    elif choice == "4":
        print("Thank you for using the security tool")
        # Step 7.5 - Stop repeating the menu when Exit is selected
        break