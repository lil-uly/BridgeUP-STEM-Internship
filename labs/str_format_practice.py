## Question 1
“My favorite movie is {}“.format(‘Harry Potter’)
“My favorite movie is {} and {}“.format(‘Harry Potter’, ‘Oceans 8’)
“My favorite movie is {} and my second favorite movie is {}“.format(‘Harry Potter’, ‘Oceans 8’)


## Question 2
“My favorite subjects are {} and {}“.format(‘science’, ‘social studies’)
“My favorite colore are {}, {}, and {}“.format(‘maroon’, ‘blue’, ‘white’)
“My favorite seasons are {1} and {0}“.format(‘winter’, ‘spring’)


## Question 3
names = [‘Tasluba’, ‘Emily’, ‘Thais’, ‘Diana’, ‘Thalia’, ‘Lillian’]
string = “{} is an intern in Ocean’s Six”
for name in names:
  print(string.format(name))


## Question 4
import datetime
dates = [datetime.date(1995, 10, 12), datetime.date(2000, 11, 17), datetime.date(2004, 3, 1), datetime.date(2012, 6, 30)]
title = “Sea Surface Temp In Bermuda on {}”

for date in dates:
  print(title.format(date))

date1 = datetime.date(year=2019, month=1, day=15)

date1.strftime(“%Y”)
date1.strftime(“%m/%d/%Y”)
date1.strftime(“%B %d, %Y”)
