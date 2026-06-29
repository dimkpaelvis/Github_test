import pandas as pd

def sign_up():
    print("User Information Form")

    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    age = input("Enter your age: ")
    postcode = input("Enter your postcode: ")
    password = input("Enter your password: ")

    user_data = {
        "First Name": [firstName],
        "Last Name": [lastName],
        "Age": [age],
        "Postcode": [postcode],
        "Password": [password]
    }

    df = pd.DataFrame(user_data)

    with open("user_data.csv", "a") as file:
        df.to_csv(file, index=False, header=file.tell()==0)
        status = "User data saved successfully to user_data.csv"

    print(status)

def login():
    print("Login Form")

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password match any entry in the CSV file
    with open("user_data.csv", "r") as file:
        df = pd.read_csv(file)
        if username in df['First Name'].values and password in df['Password'].values:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password.")
            print("Please try again or sign up if you don't have an account.")
            print("1. Try Again")
            print("2. Sign Up")
            choice = input("Enter your choice (1/2): ")
            if choice == '1':
                login()
            elif choice == '2':
                sign_up()

def main():
    while True:
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            login()
        elif choice == '2':
            sign_up()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()