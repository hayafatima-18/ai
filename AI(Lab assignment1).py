#!/usr/bin/env python
# coding: utf-8

# In[1]:


students = []
for i in range(5):
    print("\nEnter information for Student", i + 1)

    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")

    python = int(input("Enter Python marks: "))
    ai = int(input("Enter Artificial Intelligence marks: "))
    maths = int(input("Enter Mathematics marks: "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "python": python,
        "ai": ai,
        "maths": maths
    }

    students.append(student)

def calculate_result(student):

    total = student["python"] + student["ai"] + student["maths"]
    percentage = (total / 300) * 100

    if percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade

print(" -----------STUDENT RESULTS -------------")

highest_percentage = -1
highest_student = ""

results = []

for student in students:

    total, percentage, grade = calculate_result(student)

    print("\nName:", student["name"])
    print("Roll Number:", student["roll_no"])
    print("Total Marks:", total)
    print("Percentage:", percentage, "%")
    print("Grade:", grade)

    results.append(
        "Name: " + student["name"] +
        "\nRoll Number: " + student["roll_no"] +
        "\nTotal Marks: " + str(total) +
        "\nPercentage: " + str(percentage) + "%" +
        "\nGrade: " + grade +
        "\n"
    )

    if percentage > highest_percentage:
        highest_percentage = percentage
        highest_student = student["name"]


# Display highest student
print("\n========== HIGHEST PERCENTAGE ==========")
print("Student:", highest_student)
print("Percentage:", highest_percentage, "%")


# Save results in file
with open("results.txt", "w") as file:

    file.write("========== STUDENT RESULTS ==========\n\n")

    for result in results:
        file.write(result)

    file.write("\n========== HIGHEST PERCENTAGE ==========\n")
    file.write("Student: " + highest_student + "\n")
    file.write("Percentage: " + str(highest_percentage) + "%\n")

print("\nResults saved successfully in results.txt")


# In[2]:


# Ask user to enter a sentence
sentence = input("Enter a sentence: ")

# Convert sentence into words
words = sentence.split()


# Function to count words
def count_words(words):
    return len(words)


# Function to count characters
def count_characters(sentence):
    return len(sentence)


# Function to find longest word
def longest_word(words):
    return max(words, key=len)


# Function to find shortest word
def shortest_word(words):
    return min(words, key=len)


# Function to count vowels
def count_vowels(sentence):
    vowels = "aeiou"
    count = 0

    for char in sentence.lower():
        if char in vowels:
            count = count + 1

    return count


# Function to create unique words
def unique_words(words):
    return set(words)


# Function to sort words alphabetically
def alphabetical_words(words):
    return sorted(set(words))


# Calculate results
total_words = count_words(words)
total_characters = count_characters(sentence)
longest = longest_word(words)
shortest = shortest_word(words)
vowels = count_vowels(sentence)
unique = unique_words(words)
alphabetical = alphabetical_words(words)


# Display results
print("\n========== WORD ANALYSIS ==========")

print("Total words:", total_words)
print("Total characters:", total_characters)
print("Longest word:", longest)
print("Shortest word:", shortest)
print("Number of vowels:", vowels)

print("Unique words:", unique)

print("Words in alphabetical order:")
print(alphabetical)


# Save results in file
with open("word_analysis.txt", "w") as file:

    file.write("========== WORD ANALYSIS ==========\n")
    file.write("Sentence: " + sentence + "\n\n")

    file.write("Total words: " + str(total_words) + "\n")
    file.write("Total characters: " + str(total_characters) + "\n")
    file.write("Longest word: " + longest + "\n")
    file.write("Shortest word: " + shortest + "\n")
    file.write("Number of vowels: " + str(vowels) + "\n")

    file.write("Unique words: " + str(unique) + "\n")
    file.write("Alphabetical words: " + str(alphabetical) + "\n")

print("\nAnalysis saved successfully in word_analysis.txt")


# In[3]:


products = []

# Enter 5 products
for i in range(5):

    print("\nEnter Product", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)


# Function to calculate bill
def calculate_bill(products):

    total_bill = 0

    for product in products:
        total = product["price"] * product["quantity"]
        product["total"] = total
        total_bill = total_bill + total

    return total_bill


# Calculate complete bill
total_bill = calculate_bill(products)


# Find most expensive product
most_expensive = products[0]

for product in products:
    if product["price"] > most_expensive["price"]:
        most_expensive = product


# Apply discount
discount = 0

if total_bill > 10000:
    discount = total_bill * 0.10

final_bill = total_bill - discount


# Display bill
print("\n========== SHOPPING BILL ==========")

for product in products:

    print("\nProduct:", product["name"])
    print("Price:", product["price"])
    print("Quantity:", product["quantity"])
    print("Total:", product["total"])

print("\nComplete Bill:", total_bill)
print("Discount:", discount)
print("Final Bill:", final_bill)

print("\nMost Expensive Product:", most_expensive["name"])
print("Price:", most_expensive["price"])


# Save bill in file
with open("bill.txt", "w") as file:

    file.write("========== SHOPPING BILL ==========\n\n")

    for product in products:

        file.write("Product: " + product["name"] + "\n")
        file.write("Price: " + str(product["price"]) + "\n")
        file.write("Quantity: " + str(product["quantity"]) + "\n")
        file.write("Total: " + str(product["total"]) + "\n\n")

    file.write("Complete Bill: " + str(total_bill) + "\n")
    file.write("Discount: " + str(discount) + "\n")
    file.write("Final Bill: " + str(final_bill) + "\n\n")

    file.write("Most Expensive Product: " + most_expensive["name"] + "\n")
    file.write("Price: " + str(most_expensive["price"]) + "\n")

print("\nBill saved successfully in bill.txt")


# In[4]:


# Functions for calculations

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def modulus(a, b):
    return a % b


# Calculator
while True:

    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nSelect an operation:")
    print("+ Addition")
    print("- Subtraction")
    print("* Multiplication")
    print("/ Division")
    print("% Modulus")

    operation = input("Enter operation: ")

    if operation == "+":
        result = addition(num1, num2)

    elif operation == "-":
        result = subtraction(num1, num2)

    elif operation == "*":
        result = multiplication(num1, num2)

    elif operation == "/":
        if num2 != 0:
            result = division(num1, num2)
        else:
            print("Cannot divide by zero!")
            continue

    elif operation == "%":
        if num2 != 0:
            result = modulus(num1, num2)
        else:
            print("Cannot divide by zero!")
            continue

    else:
        print("Invalid operation!")
        continue

    print("Result:", result)

    again = input("\nDo you want another calculation? (yes/no): ")

    if again.lower() == "no":
        print("Calculator closed.")
        break


# In[5]:


# Restaurant Menu
menu = {
    "Burger": 500,
    "Pizza": 800,
    "Fries": 250,
    "Drink": 150
}

def display_menu():
    print("\n----- MENU -----")
    print("1. Burger - Rs. 500")
    print("2. Pizza  - Rs. 800")
    print("3. Fries  - Rs. 250")
    print("4. Drink  - Rs. 150")
    print("5. Exit")

def calculate_price(price, quantity):
    return price * quantity


total_bill = 0
orders = []

while True:
    display_menu()

    choice = int(input("\nEnter your choice: "))

    if choice == 5:
        break

    if choice == 1:
        item = "Burger"
    elif choice == 2:
        item = "Pizza"
    elif choice == 3:
        item = "Fries"
    elif choice == 4:
        item = "Drink"
    else:
        print("Invalid choice!")
        continue

    quantity = int(input("Enter quantity: "))

    price = menu[item]
    item_total = calculate_price(price, quantity)

    total_bill = total_bill + item_total

    orders.append((item, quantity, item_total))

    print(item, "x", quantity, "=", item_total)


print("\n----- FINAL BILL -----")

for item, quantity, item_total in orders:
    print(item, "x", quantity, "=", item_total)

print("Total Bill = Rs.", total_bill)


# Save bill in orders.txt
with open("orders.txt", "w") as file:
    file.write("----- RESTAURANT BILL -----\n")

    for item, quantity, item_total in orders:
        file.write(f"{item} x {quantity} = Rs. {item_total}\n")

    file.write(f"\nTotal Bill = Rs. {total_bill}\n")

print("\nBill saved in orders.txt")


# In[ ]:




