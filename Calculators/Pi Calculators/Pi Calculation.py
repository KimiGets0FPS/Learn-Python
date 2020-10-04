import math as m
times = int(input("How many times do you want to do this? "))
def perimeter(r):
  # f = (float(input("What do you want as your radius for your circle?(perimeter) ")))
   print (m.pi * r * 2)
def area(r):
   # f = (float(input("What do you want as your radius for your circle?(area) ")))
    print (m.pi * r * r)

#run the code!!!
t = times    
while (t > 0):
    r = (float(input("What do you want as your radius for your circle?(area) ")))
    area(r)
    t = t - 1

t = times    
while (t > 0):
    r = (float(input("What do you want as your radius for your circle?(perimeter) ")))
    perimeter(r)
    t = t - 1
