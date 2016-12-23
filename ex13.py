a = raw_input("write your name")
b = raw_input("your gender")
c = raw_input ("your hobby")
d = raw_input ("your favorite food")


from sys import argv

a, b, c, d = argv

print "The script is called:", a
print "Your first variable is:", b
print "Your second variable is:", c
print "Your third variable is:", d