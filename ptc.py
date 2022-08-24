import math
import os
import random
import re
import sys
# Complete the 'makingAnagrams' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
def makingAnagrams(s1, s2):
    # Write your code here
    c = 0
    total = 0
    st = set(s1 + s2)
    for i in range(len(st)):
        count1 = s1.count(list(st)[i])
        count2 = s2.count(list(st)[i])
        if(count1 > count2):
            c = count1 - count2
        elif(count2 > count1):
            c = count2 - count1
        elif(count1 == count2):
            c = 0
        total += c
    return total
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s1 = input()
    s2 = input()
    result = makingAnagrams(s1, s2)
    fptr.write(str(result) + '\n')
    fptr.close()