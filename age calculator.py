from datetime import datetime

def calculate_age(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def main():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        age = calculate_age(birthdate)
        print(f"You are {age} years old.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    main()
