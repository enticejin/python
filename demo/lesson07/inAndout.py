#输入和输出
year = 2020
event = 'Referendum'
print(f'Result of {year} {event}')

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} Yes votes {:2.2%}'.format(yes_votes, percentage))

s = 'hello, world.'
print(str(s))
print(repr(s))
print(str(1 / 7))
import math
print(f'{math.pi:.3f}')