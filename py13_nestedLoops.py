# nested loops
# The "inner loop" will finish all of it's iterations before
# finishing one iteration of the "outer loop"

row = int(input("Enter number of Row \t: "))
column = int(input("Enter number of Column \t: "))
symbol = str(input("Enter symbol to use \t: "))

# for i in range(0, row):   //BigO n+1
#     for j in range(0, column):    //BigO n(n+1)                
#         if len(symbol) == 0:  //BigO n(n)+n(n)
#             print("("+str(i)+","+str(j)+")", end="\t")
#         else:
#             print(symbol, end="")
#     print()

if len(symbol) == 0:
    for i in range(0, row):
        for j in range(0, column):
            print("("+str(i)+","+str(j)+")", end="\t")
        print()
else:
    for i in range(0, row):
        for j in range(0, column):
            print(symbol, end="")
        print()
    