# ========================================
# PYTHON LEARNING - WEEK 1
# Day 3: Functions, Lists & Dictionaries
# ========================================

print("=== Day 3: Functions, Lists & Dictionaries ===\n")

# ====================== 1. FUNCTIONS ======================

print("1. FUNCTIONS")

def greet(name):
    print(f"Hello {name}! Welcome to Day 3.")

def add_numbers(a, b):
    return a + b

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

# Calling functions
greet("Narendra")

result = add_numbers(50, 30)
print(f"Sum = {result}")

print(f"Is 25 years old an adult? {is_adult(25)}")

# ====================== 2. LISTS ======================
print("\n2. LISTS")

# Creating a list
fruits = ["apple", "banana", "mango", "orange"]

print("Original List:", fruits)
print("First item:", fruits[0])
print("Last item:", fruits[-1])

# List operations
fruits.append("grapes")           # Add item
fruits.pop(1)                     # Remove by index
print("After modifications:", fruits)

# Loop through list
print("Fruits in list:")
for fruit in fruits:
    print(" -", fruit)

# ====================== 3. DICTIONARIES ======================
print("\n3. DICTIONARIES")

person = {
    "name": "Narendra",
    "age": 40,
    "city": "Delhi",
    "profession": "Teacher"
}

print("Name:", person["name"])
print("Age:", person["age"])

# Adding new key-value pair
person["salary"] = 850000  

# Modifying existing value
person["age"] = 41

print("Updated Person Dictionary:", person)

# ====================== DAY 3 EXERCISE ======================

print("\n" + "="*50)
print("DAY 3 EXERCISE: Student Grade Manager")
print("="*50)

def calculate_average(marks):
    return sum(marks) / len(marks)

def get_grade(avg):
    if avg >= 90:
        return "A - Excellent"
    elif avg >= 75:
        return "B - Good"
    elif avg >= 60:
        return "C - Average"
    else:
        return "F - Need Improvement"
    
# Main program
student_name = input("Enter Student Name: ")
num_subjects = int(input("Enter number of subjects: "))

marks = []
for i in range(num_subjects):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

average = calculate_average(marks)
grade = get_grade(average)

print("\n" + "-"*40)
print("          STUDENT REPORT")
print("-"*40)
print(f"Student Name : {student_name}")
print(f"Marks        : {marks}")
print(f"Average      : {average:.2f}")
print(f"Grade        : {grade}")
print("-"*40)