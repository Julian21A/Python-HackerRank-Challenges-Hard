import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
matrix = list(zip(*matrix))
txt = str()
for s in matrix:
    for c in s:
        txt += c
print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', txt))