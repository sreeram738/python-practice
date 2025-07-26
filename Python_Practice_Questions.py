
# -------------------------------
# 🔢 Variables Practice Questions
# -------------------------------

# Q1. Assign your name and age to variables and print them
name = "Sreeram"
age = 25
print("Name:", name)
print("Age:", age)

# Q2. Assign values to two variables and swap them without using a third variable
a = 10
b = 20
print("Before Swap: a =", a, ", b =", b)
a, b = b, a
print("After Swap: a =", a, ", b =", b)


# -------------------------------
# ➕ Operators Practice Questions
# -------------------------------

# Q1. Take two numbers and print their sum, difference, product, and division
x = 15
y = 5
print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)
print("Division:", x / y)

# Q2. Take a number and check if it is even or odd using the modulus operator
num = 8
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")


# -------------------------------
# ⚖️ Conditions Practice Questions
# -------------------------------

# Q1. Take a number and print whether it’s positive, negative or zero
number = -3
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Q2. Take marks of a student and print their grade (A, B, C, Fail)
marks = 76
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


# -------------------------------
# 🔁 Loops Practice Questions
# -------------------------------

# Q1. Print numbers from 1 to 10 using a for loop
for i in range(1, 11):
    print(i)

# Q2. Print all even numbers from 1 to 20 using a while loop
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1


# -------------------------------
# 🧠 Combined Concept Questions
# -------------------------------

# Q1. Check if a number is Prime
number = 13
prime = True
if number <= 1:
    prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
if prime:
    print("Number is Prime")
else:
    print("Number is Not Prime")

# Q2. Build a simple calculator using input, operators, and if-elif-else
num1 = 8
num2 = 4
operator = '*'
if operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operator")

# Q3. Print the factorial of a number entered by the user using a loop
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)

# Q4. Create a number guessing game
import random
secret = random.randint(1, 50)
guess = int(input("Guess a number between 1 and 50: "))
while guess != secret:
    if guess > secret:
        print("Too High")
    else:
        print("Too Low")
    guess = int(input("Try again: "))
print("Congratulations! You guessed it right.")

# Q5. Swap two numbers without using third variable
a = 3
b = 7
print("Before Swap: a =", a, ", b =", b)
a, b = b, a
print("After Swap: a =", a, ", b =", b)
