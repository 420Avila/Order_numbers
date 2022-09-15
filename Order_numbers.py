# create a function that returns a list sorted from smallest to largest.
# Neither sorted() nor libraries can be used. 

from unittest import result


def bubbleSort(arrayNums):

    change = True

    while change:

        change = False

        for num in range(len(arrayNums) -1):

            if arrayNums[num] > arrayNums[num + 1]:

                Temp = arrayNums[num]
                arrayNums[num] = arrayNums[num + 1]
                arrayNums[num +1] = Temp 
                change = True
    return arrayNums


arrayNums = [28, 35, 24, 43, 49, 14, 37, 13, 45, 10, 6, 1, 15, 20, 42, 22, 12, 8, 16, 2, 26, 4, 3, 34, 46, 7, 36, 21, 27, 30, 23, 5, 47, 31, 39, 38, 44, 48, 25, 40, 29, 19, 18, 50, 32, 41, 11, 9, 33, 17]

result = bubbleSort(arrayNums)

print(result)