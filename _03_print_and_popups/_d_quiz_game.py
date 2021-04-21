from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    score = 0
    answer = input('What is the name of a six string instrument?')
    if answer == "guitar":
        score += 1
    else:
        score -= 1
    print(score)

    answer2 = input("what is the most common percussion instrument?")
    if answer2 == "drums":
        score += 1
    else:
        score -= 1
    print(score)

    answer3 = input("What fret on the e string of a guitar is the A on?")
    if answer3 == "5":
        score += 1
    else:
        score -= 1
    if score == 3:
        print('YOU WIN!')
    elif score == 2:
        print('ALMOST!')
    else:
        print("YOU LOSE!")



    # Make a new window variable, window = Tk()
    
    # Hide the window using the window's .withdraw() method
    
    # 1. Create a variable to hold the user's score. Set it equal to zero. 

    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    
    #      // 3.  Use an if statement to check if their answer is correct

    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
