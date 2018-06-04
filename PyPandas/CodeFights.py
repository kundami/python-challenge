CodeFight Solutions

Given an array of integers numbers, we'd like to find the closest pair of elements that add up to sum. Return the distance between the closest pair (absolute difference between the two indices). If there isn't a pair that adds up to sum, return -1.

numbers: [1, 0, 2, 4, 3, 0]
For numbers = [1, 0, 2, 4, 3, 0] and sum = 5 the output should be findClosestPair(numbers, sum) = 2


def findClosestPair(numbers, sum):
    closest_pair=999
    for i in range(0,len(numbers)):
        #print("numbers"+str(numbers[i]))
        stack = []
        add=numbers[i]
        for j in range(i+1,len(numbers)):
            #print("numbers inner"+str(numbers[j]))
            add = add+numbers[j]
            #print("add"+str(add))
            if add < sum :
                continue
            if add == sum :
             #   print("found match")
                if closest_pair > (j-i):
                    closest_pair = (j-i)
                else:
                    closest_pair = closest_pair
            if add > sum :
                add = add-numbers[j]
    if closest_pair == 999:
        return -1
    else:
        return closest_pair
    