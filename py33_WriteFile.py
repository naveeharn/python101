
from os import write

pathName = 'py33_writeText.txt'

message_1 = "Kuay I na Hee\nYed Moter\n44\n"
message_2 = "Hello Motherfucker\nI na Here\nYed Hee"
message_3 = "Mamacita"


 
# with open(pathName,{}) {}={r=read,w=write}
with open(pathName,'w') as file:
    file.write(message_1)

with open(pathName,'r') as file:
    print(file.read())

with open(pathName,'w') as file:
    file.write(message_2)

with open(pathName,'r') as file:
    print(file.read())

with open(pathName,'a') as file:
    file.write(message_3)



