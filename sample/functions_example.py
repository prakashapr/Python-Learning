def addition (num_one=0, num_two=0):
    print ("inside the functiomn")
    return num_one + num_two

num1 = 20
num2 = 30
res = addition(num_one=num1, num_two=num2)
print (f"sum of {num1} + {num2} = {res}")


#uppercase string
"""a ="hello world"
print(a.upper())"""

#lowercase string
"""a ="HELLO WORLD"
print(a.lower())"""

#remove whitespace in string

"""a ="hello ,world"
print(a.strip())"""

#replace string
"""
a = "hello world"
print(a.replace("h" , "j"))   ###replacing (h) to (j)
"""
#escape character
"""txt = "We are the so-called \"Vikings\" from the north."       #\"ks\" is an escape character

print(txt)"""


"""
a = 100
b = 200
if a > b :
    print(True)
else:
    print(False)

print(bool("hello"))
print(bool(0))
"""
"""
def myFunction():
    return True == False
print(myFunction())"""

x = 200
print(isinstance(x, int))

