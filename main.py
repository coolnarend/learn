# ========================================
# DAY 1 - PYTHON BASICS LEARNING FILE
# ========================================

print("=== Day 1: Python Basics ===\n")

# ----------------- VARIABLES -----------------
print("1. VARIABLES:")
name = "Narendra"
age = 40
salary = 50000.50
print(f"Name: {name}, Age: {age}, Salary: {salary}\n")
      
# ----------------- DATA TYPES -----------------
print("2. DATA TYPES:")

# String
greeting = "Hello, World!"
print(f"String: {greeting} → Type: {type(greeting)}")

# Integer
year = 2024
print(f"Integer: {year} → Type: {type(year)}")

# Float
pi = 3.14159
print(f"Float: {pi} → Type: {type(pi)}")

# Boolean
is_active = True
print(f"Boolean: {is_active} → Type: {type(is_active)}\n")

# List
fruits = ["apple", "banana", "cherry"]
print(f"List: {fruits} → Type: {type(fruits)}")

# Dictionary
person = {"name": "Alice", "age": 30}
print(f"Dictionary: {person} → Type: {type(person)}")

# ----------------- PRACTICE -----------------
# print("3. PRACTICE:")
# name = input("Enter Name: ")
# age = int(input("Enter Age: "))
# print(f"Hello {name}")
# print(f"Age = {age}")

# ----------------- EXERCISE -----------------
print("4. EXERCISE - Personal Profile App")

print("\n=== Personal Profile App ===")

# Get input from user
name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
city = input("Enter your City: ")
profession = input("Enter your Profession: ")

# Output Profile Summary
print("\n" + "="*40)
print("          PROFILE SUMMARY")
print("="*40)
print(f"Name          : {name}")
print(f"Age           : {age} years")
print(f"City          : {city}")
print(f"Profession    : {profession}")
print("="*40)

# Bonus message
if age < 18:
    print("You're young! Keep learning! 🚀")
elif age < 35:
    print("You're in your prime! 💪")
else:
    print("Your experience is valuable! 🌟")