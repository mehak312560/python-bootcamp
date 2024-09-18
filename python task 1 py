from datetime import datetime

def calculate_age_in_days(dob_str):
    # Convert the date of birth string to a datetime object
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    
    # Get the current date
    today = datetime.now()
    
    # Calculate the difference in days
    age_in_days = (today - dob).days
    
    return age_in_days

# Example usage
dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
age_in_days = calculate_age_in_days(dob_str)
print(f"Your age in days is: {age_in_days}")