import random

x = random.randint(1,6)

print(random.random())
print(random.randint(1,6))

myList = ['rock','paper','scissors']
print(random.choice(myList))

ranks = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
random.shuffle(ranks)
print(ranks)