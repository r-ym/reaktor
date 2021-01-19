import os
import re
import binascii

f = open('1.txt','r')

line = "1"
while line:
    line = f.readline()
    line_arr = re.findall('.'*8, line)
    # print(line_arr)
    valid = 0
    for b in line_arr:
        pointer = int(b,2)
        if pointer < 40:
            valid = pointer
            break
    while True:
        b = line_arr[valid]
        num = int(b,2)
        if num > 40:
            print(b)
            break
        else:
            valid = num

