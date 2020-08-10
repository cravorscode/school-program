# age for each class
age = int(input("age"))
name = str(input('name'))

if age < 5:
    print('''%s this section isn't for you''' % name)

# when None
elif age <= -1:
    print('please type an age')

#when 5
elif age == 5:
    print('%s welcome to class, you are to be in year 1' % name)

#when 6
elif age == 6:
    print('%s welcome to class, you are to be in year 2' % name)

#when 7
elif age == 7:
    print('%s welcome to class, you are to be in year 3' % name)

#when 8
elif age == 8:
    print('%s welcome to class, you are to be in year 4' % name)

#when 9
elif age == 9:
    print('%s welcome to class, you are to be in year 5' % name)

#when 10
elif age == 10:
    print('%s welcome to class, you are to be in year 6' % name)

#when 11
elif age == 11:
    print('%s welcome to class, you are to be in year 7' % name)

#when 12
elif age == 12:
    print('%s welcome to class, you are to be in year 8' % name)

#when 13
elif age == 13:
    print('%s welcome to class, you are to be in year 9' % name)
#when 14
elif age == 14:
    print('%s welcome to class, you are to be in year 10' % name)

#when 15
elif age == 15:
    print('%s welcome to class, you are to be in year 11' % name)

#when 16
elif age == 20 or age == 21 or age == 22 or age == 23 or age == 24 or age > 24:
    print("dude get a job") or print('maybe you were surfing the web for porn but ended up here')
