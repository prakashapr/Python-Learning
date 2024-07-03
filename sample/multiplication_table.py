##3

# 3 x 1 = 3
# 3 x 2 = 6

# 3 x 10 = 30
# 3 x 20 = 60


def multiplication_table(num=1, start=1, end=20):
    for i in range(start, end+1):
        print(f"{num} * {i} = {num * i}")


a = 10
b = 90
c = 11
multiplication_table(num=a, start=c, end=b)

multiplication_table(num=4, start=20, end=40)
start_num = 1
end_num = 20
for k in range (1, 101):
    multiplication_table(num=k, start=start_num, end=end_num)