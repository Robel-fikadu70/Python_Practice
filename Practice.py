# 1. Write a program that asks the user for two numbers and prints their sum, difference, product, and quotient.

print("Enter two numbers:")
num1 = float(input("num1: "))
num2 = float(input("num2: "))
summ = num1 + num2
dif = num1 - num2
mul = num1*num2
if num2!=0:
    div = num1/num2
else:
    div = "undefined"
print(f"sum: {summ}")
print(f"difference: {dif}")
print(f"product: {mul}")
print(f"quotient: {div}")

# 2. Write a program that checks whether a given number is even or odd.
num = float(input("enter a number: "))
if num%2 == 0:
    print("even")
else:
    print("odd")

# 3. Write a program that checks if a number is prime.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# 4. Write a program that takes a string and returns it reversed
def reverse_string(s):
    return s[::-1]
user_input = input("Enter a string: ")
reversed_string = reverse_string(user_input)
print(f"Reversed string: {reversed_string}")

# 5. Write a program that counts the number of vowels in a given string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

user_input = input("Enter a string: ")
vowel_count = count_vowels(user_input)
print(f"Number of vowels in the string: {vowel_count}")

# 6. Write a program that removes duplicate elements from a list.
def remove_duplicates(input_list):
    return list(set(input_list))

user_input = input("Enter a list of elements (separated by spaces): ")
input_list = user_input.split()
unique_list = remove_duplicates(input_list)
print(f"List after removing duplicates: {unique_list}")

# 7. Write a program that finds the maximum and minimum values in a list
def find_max_min(input_list):
    if not input_list:
        return None, None
    max_value = max(input_list)
    min_value = min(input_list)
    return max_value, min_value


user_input = input("Enter a list of numbers (separated by spaces): ")
input_list = list(map(float, user_input.split()))
max_value, min_value = find_max_min(input_list)

if max_value is not None and min_value is not None:
    print(f"Maximum value: {max_value}")
    print(f"Minimum value: {min_value}")
else:
    print("The list is empty.")

# 8. Write a program that generates and prints a random number between 1 and 100
import random
def generate_random_number():
    return random.randint(1, 100)
random_number = generate_random_number()
print(f"Random number between 1 and 100: {random_number}")

# 9. Write a program that calculates simple interest given principal, rate, and time
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in %): "))
time = float(input("Enter the time period (in years): "))

simple_interest = calculate_simple_interest(principal, rate, time)
print(f"Simple Interest: {simple_interest}")

# 10. Write a program that converts a temperature from Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"Temperature in Fahrenheit: {fahrenheit}")

# 11. Write a program that counts the number of words in a given sentence
def count_words(sentence):
    words = sentence.split()
    return len(words)

user_input = input("Enter a sentence: ")

word_count = count_words(user_input)
print(f"Number of words in the sentence: {word_count}")

# 12. Write a program that finds and prints the length of a list.
def find_length(input_list):
    return len(input_list)

user_input = input("Enter a list of elements (separated by spaces): ")
input_list = user_input.split()
length_of_list = find_length(input_list)
print(f"Length of the list: {length_of_list}")

# 13. Write a program that calculates the sum of the digits of a given number
def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

user_input = int(input("Enter a number: "))
digit_sum = sum_of_digits(user_input)

print(f"Sum of the digits: {digit_sum}")

# 14. Write a program that creates a dictionary from two lists: one for keys and one for values.
def create_dictionary(keys, values):
    return dict(zip(keys, values))

keys_input = input("Enter keys separated by spaces: ")
values_input = input("Enter values separated by spaces: ")

keys = keys_input.split()
values = values_input.split()

result_dict = create_dictionary(keys, values)

print("Resulting Dictionary:", result_dict)

# 15. Write a program that merges two dictionaries into one.
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5}

result_dict = merge_dictionaries(dict1, dict2)

print("Merged Dictionary:", result_dict)

# 16. Write a program that checks if two strings are anagrams of each other.
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

# 17. Write a program that calculates the area of a circle given its radius.
import math

def calculate_area(radius):
    return math.pi * (radius ** 2)

radius = float(input("Enter the radius of the circle: "))
area = calculate_area(radius)

print(f"The area of the circle with radius {radius} is: {area:.2f}")

# 18. Write a function that prints the multiplication table of a given number.
def print_multiplication_table(number, up_to=10):
    print(f"Multiplication Table for {number}:")
    for i in range(1, up_to + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

number = int(input("Enter a number to print its multiplication table: "))

print_multiplication_table(number)

# 19. Write a program that finds and prints common elements in two lists.
def find_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)

    print("Common elements:", list(common_elements))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

find_common_elements(list1, list2)

#20. Write a program that counts and displays the frequency of each element in a list
from collections import Counter

def count_element_frequency(elements):
    frequency = Counter(elements)

    for element, count in frequency.items():
        print(f"{element}: {count}")

elements = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

count_element_frequency(elements)





