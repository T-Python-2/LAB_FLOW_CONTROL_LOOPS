#LAB_FLOW_CONTROL_LOOPS

#using a range from 45 to 210 and iterate over it, Skip 100, and break at 205.
for number in range(45,210):
    if number == 100:
        continue
    if number == 205:
        break
    print(number)

#help(input)

correct:bool = False
theCorrectAnswer:int = 7*24

#using while loop to ask a question until the answer is correct
while not correct:
    answer:int = int(input("What is the product of 7 * 24 ? "))
    if answer == theCorrectAnswer:
        correct = True
        continue
    print("Your answer is wrong try again")
    
else:
    print("You answered this Question correctly")