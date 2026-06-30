def sum_of_numbers(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

num=input("Enter numbers")
for i in num:
    print(i)


n=int(input("Enter numbers"))
even_numbers = []
for i in range(n):
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        even_numbers.append(number)
print("Even numbers:", even_numbers)


def print_word_lengths(words):
    for word in words:
        print(f"The length of '{word}' is {len(word)}")




n = int(input("Enter the number of words: "))
words = []
for i in range(n):
    word = input("Enter a word: ")
    print(f"The length of '{word}' is {len(word)}")





def calculate_average(numbers):
    total = 0
    count = len(numbers)
    for x in numbers:
        total += x
    average = total / count 
    return average