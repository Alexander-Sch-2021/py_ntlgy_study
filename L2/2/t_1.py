some_str = input()
x_len = len(some_str)

if x_len % 2 != 0:
    print(some_str[x_len // 2])
else:
    print(some_str[x_len // 2 - 1:x_len // 2 + 1])
