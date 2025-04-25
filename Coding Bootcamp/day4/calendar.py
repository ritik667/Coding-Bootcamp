from datetime import datetime


birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

current_date = datetime.now()
difference = current_date - birthdate
print(f"The difference is {difference.days} days.")