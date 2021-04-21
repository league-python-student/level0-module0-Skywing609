from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num =random.randint(0, 3)
    print(num)
    q1 = input("Type something that you think is AWESOME!")
    if num == 0:
        print("That is awesome!")
    elif num == 1:
        print("That's an ok thing.")
    elif num == 2:
        print("that's kinda boring bro.")
    elif num == 3:
        print("THATS LIKE SUPER DUPER POOPER AWESOME BOIIIII!")
    window.mainloop()


    # Make a new window variable, window = Tk()
    
    # Hide the window using the window's .withdraw() method

    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    
    # 2. Print your variable to the console
    
    # 3. Get the user to enter something that they think is awesome
    
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
        
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
        
    # Run the window's .mainloop() method
