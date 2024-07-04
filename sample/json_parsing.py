import json
json_file = "../files/students.json"
f = open(json_file)
data = json.load(f)
print(data['students'][0])
number_of_students = len(data['students'])
print(number_of_students)
for i in range(number_of_students):
    print(f"{data['students'][i]['id']} : {data['students'][i]['name']}")