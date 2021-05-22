import os

source = "/Users/naveeharntehmarn/Desktop/Sophomore/2_semester_1/everythingPython/python101/py35_floder/before_move/py35_text.txt"
destination = "/Users/naveeharntehmarn/Desktop/Sophomore/2_semester_1/everythingPython/python101/py35_floder/after_move/py35_text.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError as e:
    print(e)
    print(source + " was not found")
except Exception as e:
    print(e)
