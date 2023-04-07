#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'mostUnlucky' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER start_year
#  2. INTEGER end_year
#

def mostUnlucky(start_year, end_year):
    # Write your code here
    day_names = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    def day_of_week(d,m,y):
        if m == 1 or m == 2:
            m += 12
            y -= 1

        day = int(((13 * m + 3) // 5 + d + y + (y // 4) - (y // 100) + (y // 400)) % 7)
        return day_names[day]
    def unlucky(year):

        date_list = [(y, x, year) for x in range(1,13) for y in range(1,32) if day_of_week(13, x, year) == 'Friday' and y == 13]

        return date_list
    
    end_year += 1
    year_list = [x for x in range(start_year,end_year) if len(unlucky(x)) > 2]
    return year_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    years = list(map(int, input().rstrip().split()))

    answer = mostUnlucky(years[0], years[1])

    fptr.write('['+', '.join(map(str, answer))+']')
    fptr.write('\n')

    fptr.close()
