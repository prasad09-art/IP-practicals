age = input(" Enter your age:")
marks = input ("Enter your marks:")

# display original types
print("\nbefore conversion:")
print(" Age:",age,"Type:", type(age))
print("Marks:",marks,"Type:" type(marks))

# Type conversion(casting)
age = int (age)
marks = float (marks)

# performing arithmetic operation
future_age = age+5
total_marks=marks+10
print("\nAfter conversion:")
print("Age (int):",age)
print("marks (float
