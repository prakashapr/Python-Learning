task = ["amma", "appa", "god", "job"]
print(task)
task[1] = "anna"
print(task)
# print(task + task1)
print(task[0:3])
python = ["12"]
print(task + python)



a = "he is a good boy"
print(a)
print(a + " " + "python")
b = 10
c = 12
d = 1
d += b + c
print(d)
a = 10
b = 20
c = 30
if (a == b / 1) or (c == b + 10):
    print("condition is true")
else:
    print("condition is false")
if not a:
    print("condition is true")
else:
    print("false")

    count = 0
    while count < 5:
        print("count is:", count)
        count = count + 1

        i = 2
        while i < 100:
            j = 2
            if j <= (i / j):
                if not (i % j):
                    break
                j = j + 1
        if j > i / j:
            print(i, "is a prime")
            i = i + 1
