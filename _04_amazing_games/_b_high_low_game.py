from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    G = 10
    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    # 2. Print out the random variable above
    print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for q in range(10):
        # 4. Ask the user for a guess using a pop-up window, and save their response
        q = input("Guess a random number from 1 to 100!")
        if q == str(random_num):
            print('You win!')
            exit()
        else:
            G -= 1
            print("you have " +str(G)+ " Guesses!")

        # 5. If the guess is correct
        if q > str(random_num):    # 6. Win. Use 'sys.exit(0)' to end the program
            messagebox.showinfo(None,"Too High!")
        elif q < str(random_num):
            messagebox.showinfo(None, "Too low!")
        # 7. if the guess is high
            # 8. Tell them it's too high
        # 9. Else if the guess is low
            # 10. Tell them it's too low
    if G == 0:
        print("YOU LOSE!")
        sys.exit(0)
    #11. Outside of the loop, tell the user they lost


