## 1) Using range(),  make a range from 45 to 210, using a for loop iterate over the sequence and print the elements.
#  Skip the number 100 and break the loop at 205


number:int = range(45,210)

for i in number :
    if i == 100:
        continue
    print(i)
    if i == 205:
        break

## 2) Using a while loop and input , do the following :

n = True
while n == True:

    x = int(input("what is the product of 7 * 24 ?"))

    if x != 168:
        print("Your Answer is wrong try again..")
        
    else:
        print("You answered this Question correctly")
        n = False

