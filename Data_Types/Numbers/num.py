# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
# Float can also be scientific numbers with an "e" to indicate the power of 10.
a1 = 1.10
c1 = -35.59
d1 = 12E4
e1 = -87.7e100
print(type(a1))
print(type(c1))
print(type(d1))
print(type(e1))

#Complex numbers are written with a "j" as the imaginary part:
x1 = 3+5j
y1 = 5j
z1 = -5j
print(type(x1))
print(type(y1))
print(type(z1))
print(x1)

# Type Conversion - converting from one type to another with the int(), float(), and complex() methods:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))