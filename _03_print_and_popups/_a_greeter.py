from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block 
if __name__ == '__main__':
    
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # Ask the user for their name and save it to a variable
    name = simpledialog.askstring(title='Greeter', prompt = 'What is your name?')
    # name = simpledialog.askstring(title='Greeter', prompt="What is your name?")
    
    # Show a message box with your message using the .showinfo() method
    messagebox.showinfo('title', 'Hello ' + name + ',nice to meet you!')
    # Print your message to the console using the print() function
    print('Hello from the console')
    # Show an error message using messagebox.showerror()
    messagebox.showerror('ERROR', 'RUN FOR YOUR LIFE')
    # Run the window's .mainloop() method


