#3の倍数時にfizzを表示
num = 1
while num < 101:
    if num % 3 == 0:
        print("fizz")
    else:
        print(num)
    num = num + 1
