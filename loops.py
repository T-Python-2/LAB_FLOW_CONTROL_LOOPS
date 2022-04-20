
for number in range(45,210):
    if number == 100:
        continue
    if number == 205:
        break
    print(number)
    


checkValue = False

while checkValue == False:
    value = int(input("what is the product of 7 * 24 ?  "))

    if value == 168:
        print("You answered this Question correctly")
        checkValue = True
        break
    else:
        print("Your Answer is wrong try again..")
    
            