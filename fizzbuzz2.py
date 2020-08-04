#3の倍数時に"fizz"を5の倍数時に"buzz"を表示
num = 1
while num < 101:
    if num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
    num = num + 1
