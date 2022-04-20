
#1
num:int = range(45,210)

for i in num :
    if i == 100:
        continue
    print(i)
    if i == 205:
        break

#2

n = True
while n == True:
    
    x = int(input("what is the product of 7 * 24 ?"))
    
    if x != 168:
        print("Your Answer is wrong try again..")
    else:
        print("You answered this Question correctly")
        n = False
        break    
