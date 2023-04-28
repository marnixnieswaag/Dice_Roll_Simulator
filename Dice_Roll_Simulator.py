rolling_active = True

while rolling_active:
    print("\nWould you like to roll dice?")
    prompt = input("Type 'r' to roll \nType 'q' to quit\n\n")
                   

    if prompt.lower() == 'r':
        response = input("\nHow many dice would you like to roll?\n\n")
        
        if int(response) > 6:
            print("You can't roll more than 6 dice at a time.")
        
        else:
            numbers = []
            numbers_backside = [] 
            
            for i in range(int(response)):
                import random
                roll = random.randrange(1,7)
                numbers.append(roll)
                print("\nYou rolled a " + str(roll) + ".")
                back_side = 7-roll
                numbers_backside.append(back_side)
                print("The opposite side contains a "
                    + str(back_side) + ".")
                
            total = 0
            total_backside = 0

            for i in numbers:
                total += int(i)
            
            for i in numbers_backside:
                total_backside += int(i)
            

                
            print("\nYou rolled a total of " + str(total) + ".")
            print("\nThe total of the opposite sides is " + str(total_backside) )

    elif prompt.lower() == 'q':
        rolling_active = False





           