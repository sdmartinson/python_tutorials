# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# casting data fields
# First = float(input('First:  '))
# Second = int(input('Second: '))
# sum = First + Second
# print('Sum: ' + str(sum))

# strings
# course = 'Python for Beginners'
# print(course.find('y')) # find instance of character
# print(course.replace('for', '4')) # replace character
# print('Python' in course) # find string

# arithmetic operators
# print(10+3) print(10-3) print(10*3) print(10/3) print(10//3) print(10**3)
# x = 10
# x += 3


# if statements
# temperature = 7

# if temperature > 30:
#     print('It''s Hot')
# elif temperature > 20:
#     print('Nice')
# elif temperature > 10:
#     print('Brrr')
# else:
#     print('ReallyBrr')
# print('Complete')


# weight converter
# weight = int(input('Weight: '))
# measure = input('(K)g or (L)bs: ')

# if measure.upper() == 'L':
#     print('Weight in Kg: ' + str(weight * 0.45))
# else:
#     print('Weight in Lbs: ' + str(weight / 0.45))


# while loops
# i = 1
# while i <= 10:
#     print(i * '*')
#     i = i + 1


# lists
# names = ['John', 'Bob', 'Steve', 'Sam', 'Mary']
# names[0] = 'Jon'
# print(names[0:3])


# list methods
# numbers = [1, 2, 3, 4, 5]
# numbers.insert(0, 6)
# numbers.remove(3)
# print(numbers)
# print(1 in numbers)
# print(len(numbers))


# for loops
# numbers = [1, 2, 3, 4, 5]
# for item in numbers:
#    print(item)


# the range() function
# for number in range(5, 10, 2):
#    print(number)


# tuples
# numbers = (1, 2, 3)
# numbers.index(3)


# Guessing Game
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You Won!')
#         break
# else:
#     print('You Lose :(')


# Car Game
# command = ''
# started = False
#
# while True:
#     command = input('> ').lower()
#     if command == 'start':
#         if started:
#             print('Already Started')
#         else:
#             started = True
#         print('Car Started')
#     elif command == 'stop':
#         if not started:
#             print('Already Stopped')
#         else:
#             started = False
#         print('Car Stopped')
#     elif command == 'help':
#         print('''
# start = start car
# stop = stop car
# quit = quit''')
#     elif command == 'quit':
#         break
#     else:
#         print('what??')


# For Loops
# for item in 'Python':
#     print(item)

# for item in range(3,13,2):
#     print(item)

# calculate cost of items in shop
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f'Total: {total}')


# Nested Loops
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

# numbers = [5, 2, 5, 2, 2]
# for exes in numbers:
#     output = ''
#     for count in range(exes):
#         output += 'x'
#     print(output)

# numbers = [1, 1, 1, 1, 5]
# for exes in numbers:
#     output = ''
#     for count in range(exes):
#         output += 'x'
#     print(output)


# Lists
# find_max = [3, 6, 2, 8, 4, 10]
# max = find_max[0]
# for number in find_max:
#     if number > max:
#         max = number
# print(max)


# 2D Lists
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)


# List Methods
# numbers = [5, 2, 1, 5, 7, 4]
# numbers.insert(0, 10)
# numbers.remove(5)
# numbers.append(20)
# numbers.clear()
# numbers.pop()
# numbers.index(5)
# print(numbers)
# print(50 in numbers)
# print(numbers.count(5))
# numbers.sort()
# numbers.reverse()
# print(numbers)
# Remove duplicates in a list
# dupes = [1, 2, 2, 5, 7, 9, 11, 11, 17, 19]
# uniques = []
# for dupes in dupes:
#     if dupes not in uniques:
#         uniques.append(dupes)
# print(uniques)


# Unpacking
# coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# x, y, z = coordinates
# print(x, y)


# Dictionaries = store key value pairs
# phone = input('Phone: ')
# digits = {
#     '1': 'One',
#     '2': 'Two',
#     '3': 'Three',
#     '4': 'Four',
#     '5': 'Five',
#     '6': 'Six',
#     '7': 'Seven',
#     '8': 'Eight',
#     '9': 'Nine',
#     '0': 'Zero',
# }
# output = ''
# for ch in phone:
#     output += digits.get(ch, '!') + ' '
# print(output)


# Emoji Converter -- usage of Dictionaries
# message = input('>')
# words = message.split(' ')
# emojis = {
#     ":)" : ">:)",
#     ":(" : ">:("
# }
# output = ''
# for word in words:
#     output += emojis.get(word, word) + ' '
# print(output)


# functions
# def greet_user(first_name,last_name):
#     print (f'Hi {first_name} {last_name}')
#     print ('Welcome')


# print('Start')
# greet_user(first_name='John',last_name='Smith')
# calc_cost(total=50, shipping=5, discount=0.1) # keyword arguments. comes after positional arguments
# print('Finish')


# return statement
# def square(number):
#     return number * number


# creating a reusable function
# def emoji_convert(message):
#     words = message.split(' ')
#     emojis = {
#         ":)" : ">:)",
#         ":<" : ">:<"
#     }
#     output = ''
#     for word in words:
#         output += emojis.get(word, word) + ' '
#     return output


# message = input('>')
# print(emoji_convert(message))


# Exceptions error messages
# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income/age
#     print(age)
# except ZeroDivisionError:
#     print('Cannot be 0')
# except ValueError:
#     print('Not a Number')


# Classes
