if True:
    print("that's true")
if False:
    print("nothing at all")
if not False:
    print("what's going on here?")

abc = [1,2,3,4,5]
abc_sq = []
for num in abc:
    new_number = num ** 2
    abc_sq.append(new_number)
print(abc_sq)

is_even = []
is_odd = []
for num in abc_sq:
    if num % 2 == 0:
        print("this is even")
        is_even.append(num)
    else:
        is_odd.append(num)
print(is_even, is_odd)