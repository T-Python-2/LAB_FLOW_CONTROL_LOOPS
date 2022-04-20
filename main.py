
for number in range(45, 211):
    if number == 100 :
        continue
    if number == 205 :
        break
    print(number)

#
ansewer_check = False

while ansewer_check == False:
    input_value = int(input("what is the product of 7 * 24 ?  "))

    if input_value == (7*24):
        print("You answered this Question correctly")
        ansewer_check = True
    else:
        print("Your Answer is wrong try again..")





