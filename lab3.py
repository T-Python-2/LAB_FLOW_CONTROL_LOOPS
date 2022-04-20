for n in range(45,210) :
    if n == 100 :
        continue
    if n == 205:
        break

    print(n)


product =168
answer = input("what is the product of 7 * 24 ?")
if answer == product:
    print("You answered this Question correctly")

while answer != product:
    print("Your Answer is wrong try again..") 
    answer = input("what is the product of 7 * 24 ?")

   
      