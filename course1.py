import calculateHomeWork as calculateHomeWork
myMoney = 50
item = 15
tax = 0.03
total = myMoney - item - item*tax
print(total)
my_list = [1,2,3,4,5]
print(my_list)
my_set = {1,2,3,4,5,1,2}
print(my_set)
for x in my_set:
    print(x)
my_tuple=(1,2,3,4,5,1,2)
print(my_tuple)
animal = ['a','b','c','d','e']
animal.pop(2)
animal.append('f')
animal.pop(0)
like_coffee = True
like_tea = False
if like_coffee:
    print('true')
my_list_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
x=0
while x < len(my_list_day):
    print(my_list_day[x])
    x += 1
user_dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
user_dictionary.pop("age")
print(user_dictionary)

def print_my_name(name):
    print("My name is " + name)
print_my_name("Alice")

homework_assignment_grades={"Math": 85, "Science": 90, "English": 78
}
average = calculateHomeWork.calculate_homework_average(homework_assignment_grades)
print("Average homework grade:", average)