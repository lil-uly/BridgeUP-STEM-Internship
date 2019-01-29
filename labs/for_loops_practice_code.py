#Import statements up here
import datetime


## Answer to Question 1 here

1 + 5
2 + 5
3 + 5
4 + 5
5 + 5
6 + 5
7 + 5
8 + 5
9 + 5
10 + 5

## Answer to Question 2 here

x = range(10)
for i in x:
    print (i + 5)



## Answer to Question 3 here
a = [1, 'ocean', -101, 2.2, 'hello world', 'eddies', '110']
##Print out every element in the list using loops
for item in a:
    print(item)


## Answer to Question 4 here
for item in a:
    if type(item) == int:
        print(item + 10)
    elif type(item) == str:
        print("string")



## Answer to Question 5 here
days = [[1901,1,2], [1992, 12, 11], [1685, 9, 4], [2018, 6,29]]

new_dates = []


a = datetime.date(month = 1, day = 2, year =  1950)
new_dates.append(a)
b = datetime.date(month = 12, day = 11, year = 1992)
new_dates.append(b)
c = datetime.date(month = 9, day = 4, year = 1685)
new_dates.append(c)
d = datetime.date(month = 6, day = 29, year = 2018)
new_dates.append(d)


print(new_dates)

##For loop for list
for value in days:
    y = datetime.date(month = value[1], day = value[2], year = value[0])
    new_dates.append(y)

print(new_dates)
## Answer to Question 6 here
time = list(range(1,17))

list

print(time)
units = 'days since Jan. 1, 1950'

#a Using the datetime.date function and timedelta function, write a function called date_adder that takes in a value
#from your time variable and converts it into mm/dd/yy Hint: If your first time value is "1 day since Jan 1, 2019", what
#is its value in mm/dd/yy? What mathematical operation are you performing? Addition

def date_adder(day):
    for item in time:
        datetime.date(time)

date_adder(1)
