
# if __name__ == '__main__'

# 1. Module can be run as a standalone program
# or
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if it's
# the initial module being run

# import py61_module_two_

# print(__name__)

# print(py61_module_two_.__name__)


# if __name__ == '__main__':
#     print("running this module directly")
# else:
#     print("running other module indirectly")



def main():
    print("Hello main")

if __name__ == '__main__':
    main()


