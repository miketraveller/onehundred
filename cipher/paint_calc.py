
import math

def paint_calc(height=1, width=1, cover=1):
    ans = math.ceil(height * width / cover)
    print(f'you will need {ans} cans')

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

