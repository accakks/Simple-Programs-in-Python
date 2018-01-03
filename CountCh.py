#Prints number of times each character occurs in input string
import pprint
print("Enter string!")
line = str(input())
count = {}

for character in line:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count, )