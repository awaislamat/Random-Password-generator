import random

uppercase_leeters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_leeters = uppercase_leeters.lower()
digits = "1234567890"
symbols = "<>?|+_(){}[]*&^% $#@!|,.)"

upper ,lower, syms , nums = True, True, True, True

all = ""

if upper:
    all += uppercase_leeters
if lower:
    all += lowercase_leeters
if nums:
    all += digits
if syms:
    all += symbols

lenght = 25
amount = 5

for x in  range (amount):
    password = "".join(random.sample(all, lenght))
    print(password)