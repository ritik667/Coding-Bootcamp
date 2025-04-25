student_info = {
    4 :{'name':'Ritikesh Sharma', 'age': 20, 'gender': 'Male'},
    5 :{'name':'Rahul', 'age': 22, 'gender': 'Male'},
    7 :{'name':'Shubhash', 'age': 24, 'gender': 'Male'},
    56 :{'name':'Rajnish Kumar Soni', 'age': 25, 'gender': 'Male'},
}

print("-" * 54)
print("| {:<2} | {:<20} | {:<10} | {:<10} |".format("ID", "Name", "Age", "Gender"))
print("-" * 54)
for id, info in student_info.items():
    print("| {:<2} | {:<20} | {:<10} | {:<10} |".format(id, info['name'], info['age'], info['gender']))
print("-" * 54)