# str.format
# optional method that gives users
# more control when displaying output

animal = "cow" 
item = "moon"

print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format(animal,item))

# Positional Argument Syntax
print("The {0} jumped over the {1}".format(animal,item))
print("The {1} jumped over the {0}".format(animal,item))

# Keyword Argument Syntax
print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))
print("The {item} jumped over the {animal}".format(animal="cow",item="moon"))

text = "The {} jumped over the {}"
print(text.format(animal,item))


name = "qwert"
print("Hello, {}" .format(name))
print("Hello, {:10}. Noise to meet you" .format(name))
print("Hello, {:<10}. Noise to meet you" .format(name))
print("Hello, {:>10}. Noise to meet you" .format(name))
print("Hello, {:^10}. Noise to meet you" .format(name))



pi = 3.141592
print("The number pi is {:.2f}".format(pi))
print("The number pi is {:.9f}".format(pi))
integer = 44112
print("The integer is {:,}".format(integer))
print("The integer is {:b}".format(integer)) #decimal to binary
print("The integer is {:o}".format(integer)) #decimal to octo
print("The integer is {:x}".format(integer))
print("The integer is {:X}".format(integer)) 
print("The integer is {:e}".format(integer))
print("The integer is {:E}".format(integer))