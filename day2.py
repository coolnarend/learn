# ========================================
# Day 2
# ========================================

print("=== DAY 2: Operators, Conditions & Loops ===\n")

# ----------------- 1. OPERATORS -----------------
print("1. ARITHMETIC OPERATORS:")
a = 10
b = 3

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} // {b} = {a//b} (floor division)")
print(f"{a} % {b} = {a%b} (modulo)")
print(f"{a} ** {b} = {a**b} (power)\n")

# ----------------- 2. CONDITIONAL STATEMENTS -----------------
print("2. IF-ELIF-ELSE:")

while True:
    try:
        score = int(input("Enter score (0-100): "))
        if 0 <= score <= 100:
            break
        print("Invalid score. Please enter a value between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D\n")

print()

# ----------------- 3. LOOPS -----------------

print("3. LOOPS:")

print("For Loop Example:")
for i in range(5):           # 0 to 4
    print(f"Count: {i}")

print("\nWhile Loop Example:")
count = 0
while count < 3:             # 0 to 2
    print(f"While count: {count}")
    count += 1

# ----------------- PRACTICE -----------------
print("\n=== PRACTICE TIME ===")

# Practice 1: Even or Odd Checker
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# ----------------- EXERCISE - Day 2 -----------------
print("\n=== DAY 2 EXERCISE: Simple Calculator + Grade System ===")

print("Choose an option:")
print("1. Simple Calculator")
print("2. Grade Calculator")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")
    
    if op == "+":
        print(f"Result: {num1 + num2}")
    elif op == "-":
        print(f"Result: {num1 - num2}")
    elif op == "*":
        print(f"Result: {num1 * num2}")
    elif op == "/":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid operator!")

elif choice == "2":
    marks = int(input("Enter your marks (0-100): "))
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    else:
        print("Grade: F")
else:
    print("Invalid choice!")