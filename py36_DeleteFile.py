import os
import shutil
import time

deletePath="py36_copyfileText.txt"

try:
    shutil.copyfile('py36_text.txt','py36_copyfileText.txt')
    print("copy file complete")

    print("delete file py36_copyfileText")
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)

    os.remove(deletePath)       #delete a file
    # os.rmdir(deletePath)        #delete an empty directory
    # shutil.rmtree(deletePath)   #delete a directory containing files

    print("delete py36_copyfileText complete")
except FileNotFoundError as e:
    print(e)
    print("That file was not found")
except PermissionError as e:
    print(e)
    print("You do not have permission to delete that")
except OSError as e:
    print(e)  
    print("You cnnot delete that using that function")  
except Exception as e:
    print(e)
    print("")



