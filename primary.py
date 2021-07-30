# name: Lyric Marner
# date: July 27,2021

# -------------------- Section 1 ------------------------- #
# ------------------ List Creation ----------------------- #

print('# -------------------- Section 1 ------------------------- #')
print('Creating an Empty List' '\n')
# 1. Creating an Empty List
# --------------------------------------------------------
# Instructions
#   1. Create empty lists using the following methods.
#       a. via List Displays
#       b. via the list() function.
#   2. Print the lists.
#
# WRITE CODE BELOW
list1 = []
print(list1)

print()

list1 = list()
print(list1)

print('\n' 'Creating a Pre-Populated List' '\n')
# 2. Creating a Pre-Populated List
# ------------------------------------------------------------
# Instructions
#   1. Create the following pre-populated lists:
#       a. A list filled with 5 integers.
#       b. A list filled with 5 floats.
#       c. A list filled with 3 boolean values (True / False)
#       d. A list of three animals
#       e. A list with of 3 objects, that are all different data types.
#       f. Convert the string of the name of a star to a list via the list() function.
#   2. Print the lists.
#
#   1.a has been done for you.
#
# WRITE CODE BELOW
integers = [1, 15, -4, -26, 34]
floats = [9.7, 6.0, 4.5, 3.14, 11.9]
a = float(input('a = '))
b = float(input('b = '))
booleans = ['a == b |', a == b, 'a != b |', a != b]
animals = ['cow','parrot','lizard']
objects = ['panda', 12, -9.0]
string = list('star')

print(integers)
print(floats)
print(booleans)
print(animals)
print(objects)
print(string)

# -------------------- Section 2 ------------------------- #
# ---------------- List Modification --------------------- #
print('\n' '# -------------------- Section 2 ------------------------- #')
print('Accessing and Modifying a List' '\n')
# 1. Accessing and Modifying a List
# ------------------------------------------------------------
# Instructions
#   1. Modify the lists created in Section 1, Part 2:
#       a. Integers --> Replace the item at position 2 with a new number.
#       b. Floats --> Replace the item at position 4 with a new number.
#       c. Booleans --> Replace the item at position 0 with itself negated. (not)
#       d. Animals --> Replace one of the animals with a new animal.
#       e. Objects --> Replace one of the items within the list with a new one.
#   2. Print the lists.
#
#   1.a has been done for you.
#
# WRITE CODE BELOW
integers[2] = 44
floats[4] = 99
booleans[0] = 'a !== b |'
animals[1] = 'zebra' 
objects[2] = 'love' 

print(integers)
print(floats)
print(booleans)
print(animals)
print(objects)
print()

print('\n' 'Append, Insert, and Remove' '\n')
# 2. Accessing and Modifying a List
# ------------------------------------------------------------
# Instructions
#   1. Modify the lists created in Section 1, Part 2:
#       a. Integers --> Append a new number to the list.
#       b. Floats --> Append a new float to the list.
#       c. Booleans --> Remove one of the items from the list
#       d. Animals --> Insert a new animal at the beginning of the list.
#       e. Objects --> Insert a new object at the middle of the list.
#   2. Print the lists.
#
#   1.a has been done for you.
#
# WRITE CODE BELOW
integers.append(25)
floats.append(7.7)
booleans.remove(a == b)
objects.insert(1, 'hello')

print(integers)
print(floats)
print(booleans)
print(objects)

print('\n' 'List Concatenation' '\n')
# 3. List Concatenation
# ------------------------------------------------------------
#
# Lists like Strings can Concatenate with other Lists using the + operator. They can also be duplicated by
#   multiplying the list.
#
# Instructions
#   1. Modify the lists created in Section 1, Part 2:
#       a. Concatenate the lists holding the integers and floats together, and save the result to a new variable.
#       d. Duplicate the list holding animals 3 times, and save the result to a new variable.
#   2. Print the new lists.
#
#   Examples are below for reference
#
# WRITE CODE BELOW
example_concatenation = [1, 2, 3] + ['cat', 'dog']
example_duplication = ['cat'] * 5
print(
    '\n'
    f'example_concatenation | {example_concatenation}' '\n'
    f'example_duplication | {example_duplication}' '\n'
)
nums = [1, 15, -4, -26, 34] + [9.7, 6.0, 4.5, 3.14, 11.9]

many_animals = ['cow','parrot','lizard'] * 3

print(nums)
print(many_animals)
# -------------------- Section 3 ------------------------- #
# --------------------- Looping -------------------------- #
print('\n' '# -------------------- Section 3 ------------------------- #')
print('Looping' '\n')
# 1. Looping
# ------------------------------------------------------------
# Instructions
#   1. Create a loop that prints out the contents of the two of the lists you have already created, using the
#       methods below.
#       a. via in range()
#       b. via direct access
#
#   An example has been shown below:
#
# WRITE CODE BELOW
for i in range(len(many_animals)):
    print(many_animals[i]) 
print()

for item in nums:
    print(item)

# -------------------- Section 4 ------------------------- #
# ------------------ Comprehension ----------------------- #
print('\n' '# -------------------- Section 3 ------------------------- #')
print('Dice - Statistics' '\n')

# 1. Dice - Statistics
# ------------------------------------------------------------
# Preface
#   When we roll a dice, the side it lands on is random. However, since a dice has multiple sides that are equivalent
#       in chance of falling, then we say a side has a 1/6 chance of happening, or 16.7% chance. Lets test to see if
#       that's true!
#
# 1. Create multiple for loops to run 5, 10, 100, and 1000 times.
#   a. Within the loops, roll a dice and append the roll to a list that is keeping track of all the rolls.
# 2. After the loop has finished rolling, print the number of times each face appeared, as well as the rate of
#   rate of appearance.
#
# The beginning of the loop running 5 times has been done for you. Be sure to finish it.
#
# WRITE CODE BELOW
from random import randint

def total(num_of_rolls):
    for i in range(num_of_rolls):
        dice = randint(1,6) 
        rolls.append(dice)
    
    print(f'rolls | {rolls}')
    for i in range(1,7):  # stop - start --> 7 - 1 = 6
        print(f'{i}\t| total - {rolls.count(i)}\t\t| rate of appearance - {"{:.2%}".format(rolls.count(i) / size)}')


for size in [5, 10, 100, 1000]:
    rolls = []
    total(size)





