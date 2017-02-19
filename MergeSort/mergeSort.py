'''
Merge Sort:
split array in half until there is only one
merge bottom up
http://www.ee.ryerson.ca/~courses/coe428/sorting/mergesort.html
'''
import random

randomUnsorted = random.sample(range(50),11)
listStr = ", ".join(map(str, randomUnsorted))
print("unsorted list is " + listStr)

listLength = len(randomUnsorted)
leftSize = int(listLength / 2)
rightSize = listLength - leftSize

print(str.format("left is {0!s} and right is {1!s}", leftSize, rightSize))

leftList = randomUnsorted[0..leftSize]
leftListStr = ", ".join(map(str, leftList))
print("left list is " + leftListStr)