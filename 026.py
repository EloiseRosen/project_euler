"""
example:
1/7=0.(142857)

1 mod 7 -> remainder of 1

Multiply remainder by 10:  1 * 10 = 10
Next digit in decimal expansion is 10/7=1
New remainder is 10 mod 7 -> remainder of 3

Multiply remainder by 10: 3 * 10 = 30
Next digit in decimal expansion is 30/7=4
New remainder is 30 mod 7 -> remainder of 2

Multiply remainder by 10: 2 * 10 = 20
Next digit in decimal expansion is 20/7=2
New remainder is 20 mod 7 -> remainder of 6

Multiply remainder by 10: 6 * 10 = 60
Next digit in decimal expansion is 60/7=8
New remainder is 60 mod 7 -> remainder of 4

Multiply remainder by 10: 4 * 10 = 40
Next digit in decimal expansion is 40/7=5
New remainder is 40 mod 7 -> remainder of 5

Multiply remainder by 10: 5 * 10 = 50
Next digit in decimal expansion is 50/7=7
New remainder is 50 mod 7 -> remainder of 1

We've seen the remainder 1 before. The same sequence of multiplying by 10 and modding by 7 will give us the same sequence of digits
in the decimal expansion again. So we've found a cycle, and its length is how many steps it took to get back to the same remainder.
"""

def get_cycle_length(num):
    remainders_seen = {} # remainder: place we saw that remainder in
    place = 0

    remainder = 1 % num
    while remainder not in remainders_seen and remainder != 0:
        remainders_seen[remainder] = place
        remainder = remainder * 10
        remainder = remainder % num
        place += 1

    if remainder == 0:
        return None
    return place - remainders_seen[remainder]  # length of cycle


max_cycle_length = None
max_cycle_length_divisor = None
for num in range(1, 1_001):
    cycle_length = get_cycle_length(num)
    if cycle_length is not None:
        if max_cycle_length is None or cycle_length > max_cycle_length:
            max_cycle_length = cycle_length
            max_cycle_length_divisor = num

print(max_cycle_length_divisor)
