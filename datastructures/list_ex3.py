x = [1,1,1,1,1,1,2,3,4,5,5,5,5,5,,6,6,7,4,4,4,4,4,7,7,7,7]

x_one = x.count(1)
x_two = x.count(2)
x_four = x.count(4)
x_five = x.count(5)
print('1 occured', x_one,'times')
print('2 occured', x_two,'times')
print('4 occured', x_four,'times')
print('5 occured', x_five,'times')

y = [23,45,6,2,21,22,32,23]
z = [1,3,3,5,6,1]

print('x adding y')
x.extends(y)
print(x)

print('x adding z')
x.extends(z)
print(x)

xyz = x + y + z
