from tkinter import *



#CREATING THE WINDOW

calculator = Tk() #Creating a Tkinter object named calculator
calculator.title("Calculator") #Setting the application's title'
calculator.configure(background = "light blue") #Setting the applications background colour
calculator.geometry("280x400") #Settings the applications dimensions



#MAKE EVERYTHING RESIZABLE
Grid.rowconfigure(calculator,0,weight=1) 
Grid.rowconfigure(calculator,1,weight=1)
Grid.rowconfigure(calculator,2,weight=1)
Grid.rowconfigure(calculator,3,weight=1)
Grid.rowconfigure(calculator,4,weight=1)
Grid.rowconfigure(calculator,5,weight=1)
Grid.rowconfigure(calculator,6,weight=1)
Grid.rowconfigure(calculator,7,weight=1)
Grid.rowconfigure(calculator,8,weight=1)
Grid.rowconfigure(calculator,9,weight=1)


Grid.columnconfigure(calculator,0,weight=1)
Grid.columnconfigure(calculator,1,weight=1)
Grid.columnconfigure(calculator,2,weight=1)
Grid.columnconfigure(calculator,3,weight=1)
Grid.columnconfigure(calculator,4,weight=1)
Grid.columnconfigure(calculator,5,weight=1)
Grid.columnconfigure(calculator,6,weight=1)
Grid.columnconfigure(calculator,7,weight=1)



#CREATING THE FUNCTIONS 

expression = "" #The expression is what's shown in the equation box, this is set to nothing 

def pressNumber(number): #Creates a function named pressNumber, using number as the method

    global expression #Makes a global variable named expression, this means it can be used outside of the function
    expression = (expression + str(number)) #Sets the expression to whatever the expression originally was + the number which is obtained later from the user
    equation.set(expression) #Sets the equation to the expression


def evaluate(): #Creates a function named evaluate (this is essentialy the enter / equals function)

    try: #will try the following
        global expression #defines a function named expression, this is global
        total = str(eval(expression)) #creates a value named total, the total is the string of the evaluated expression. The eval function essentially tries to used a string value as an int value
        equation.set(total) #equation is now set to the total
        
        #expression = "" #clears the expression by making it nothing - CHANGED TO:
        expression = total #This sets the expression to what the end number was so the user can continue calculations on it
    
    except: #if the above could not be done, do the following
        equation.set(" Error ") #the equation is said to a string which will display an error message to the user
        expression = "" #clears the expression by making it nothing

def clearInput(): #creates a function named clearInput
    global expression #defines a global variable named expression
    expression = "" #the expression variable doesn't equal anything
    equation.set("") #the equation variable doesn't equal anything


def inchConversion(): #creates a function named inchConversion
    pressNumber("*2.54"), evaluate() #runs the pressNumber function with an input of *2.54 then runs the evaluate function to get the answer

def cmConversion(): #creates a function named cmConversion
    pressNumber("/2.54"), evaluate() #runs the pressNumber function with an input of /2.54 then runs the evaluate function to get the answer

equation = StringVar() #Makes the equation variable a String Variable



enteredExpression = Entry(calculator, textvariable = equation, justify = 'right', font=("Times New Roman", 20), bg = 'light blue') #This is the box that will display all of the number entries and the answer at the end

enteredExpression.grid(columnspan = 4, ipadx= 100, ipady = 30, padx = 2.5, pady= 2.5, sticky = W+E) #places the box onto the window, sets the size and sticky position




#CREATE NUMBER BUTTONS 

enterNine = Button(calculator, text = "9", width = 10, height = 3, command = lambda: pressNumber(9)) #creates a button named enterNine, assigns it to the caluclator window, sets the text which will be displayed, the size of the button, and assigns it a command which will run when pressed. this command is pressNumber with an input of 9

enterNine.grid(row=5, column = 2, padx = 2.5, pady = 2.5, sticky = NSEW) #places the button onto the caluclator window, sets which row and column the button is on, sets the size and makes it stick to all sides.

enterEight = Button(calculator, text = "8", width = 10, height = 3, command = lambda: pressNumber(8))
enterEight.grid(row=5, column = 1,padx = 2.5, pady = 2.5, sticky = NSEW)

enterSeven = Button(calculator, text = "7", width = 10, height = 3, command = lambda: pressNumber(7))
enterSeven.grid(row=5, column = 0,padx = 2.5, pady = 2.5, sticky = NSEW)

enterSix = Button(calculator, text = "6", width = 10, height = 3, command = lambda: pressNumber(6))
enterSix.grid(row=6, column = 2,padx = 2.5, pady = 2.5, sticky = NSEW)

enterFive = Button(calculator, text = "5", width = 10, height = 3, command = lambda: pressNumber(5))
enterFive.grid(row=6, column = 1,padx = 2.5, pady = 2.5, sticky = NSEW)

enterFour = Button(calculator, text = "4", width = 10, height = 3, command = lambda: pressNumber(4))
enterFour.grid(row=6, column = 0,padx = 2.5, pady = 2.5, sticky = NSEW)

enterThree = Button(calculator, text = "3", width = 10, height = 3, command = lambda: pressNumber(3))
enterThree.grid(row=7, column = 2,padx = 2.5, pady = 2.5, sticky = NSEW)

enterTwo = Button(calculator, text = "2", width = 10, height = 3, command = lambda: pressNumber(2))
enterTwo.grid(row=7, column = 1,padx = 2.5, pady = 2.5, sticky = NSEW)

enterOne = Button(calculator, text = "1", width = 10, height = 3, command = lambda: pressNumber(1))
enterOne.grid(row=7, column = 0,padx = 2.5, pady = 2.5, sticky = NSEW) 

enterZero = Button(calculator, text = "0", width = 10, height = 3, command = lambda: pressNumber(0))
enterZero.grid(row = 8, column = 0, columnspan = 2,padx = 2.5, pady = 2.5, sticky = NSEW)

#CONVERSION BUTTONS

iToCM = Button(calculator, text = "Inch to CM", width = 10, height = 3, command = inchConversion) #creates a button named iToCM in the calculator window, gives it text, size and the command: inchConversion
iToCM.grid(row = 3, column = 0, columnspan = 2,padx = 2.5, pady = 2.5, sticky = NSEW) #places the button onto the window, sets the place, size and stickyness of the button


cmToI = Button(calculator, text = "CM to Inch", width = 10, height = 3, command = cmConversion) #creates a button named cmToI in the calculator window, gives it text, size and the command: cmConversion
cmToI.grid(row = 3, column = 2, columnspan = 2,padx = 2.5, pady = 2.5, sticky = NSEW) #places the button onto the window, sets the place, size and stickyness of the button




#CREATE FUNCTION BUTTONS

divideButton = Button(calculator, text = "/", width = 10, height = 3, command = lambda: pressNumber("/")) #creates a button named divideButton, sets the text, width, height and gives it a lambda function which runs the pressNumber function with an input of /
divideButton.grid(row = 4, column = 3, padx = 2.5, pady = 2.5,sticky = NSEW) #places the button on the grid

multiplyButton = Button(calculator, text = "X", width = 10, height = 3, command = lambda: pressNumber("*")) #creates a button named multiplyButton, sets the text, width, height and gives it a lambda function which runs the pressNumber function with an input of *

multiplyButton.grid(row = 5, column = 3, padx = 2.5, pady = 2.5,sticky = NSEW) #places the button on the grid

minusButton = Button(calculator, text = "-", width = 10, height = 3, command = lambda: pressNumber("-"))#creates a button named minusButton, sets the text, width, height and gives it a lambda function which runs the pressNumber function with an input of -

minusButton.grid(row = 6, column = 3, padx = 2.5, pady = 2.5,sticky = NSEW) #places the button on the grid

addButton = Button(calculator, text = "+", width = 10, height = 3, command = lambda: pressNumber("+")) #creates a button named addButton, sets the text, width, height and gives it a lambda function which runs the pressNumber function with an input of +

addButton.grid(row = 7, column = 3, padx = 2.5, pady = 2.5,sticky = NSEW) #places the button on the grid


clear = Button(calculator, text = "AC", width = 10, height = 3, command = clearInput)

clear.grid(row=4, column = 0, padx = 2.5, pady = 2.5, sticky = NSEW) #places the button on the grid




equals = Button(calculator, text = "=", fg = 'black', bg = 'cyan', width = 10, height = 3, command = evaluate) #creates a button named equals, gives it text, a background colour and foreground colour, sets the size and gives it the command 'evaluate'
equals.grid(row = 8, column = 3, padx = 2.5, pady = 2.5,sticky = NSEW) #places the button the grid

decimal = Button(calculator, text = ".", width = 10, height = 3, command = lambda: pressNumber(".")) #creates a button named decimal, sets the text, width, height and gives it a lambda function which runs the pressNumber function with an input of .

decimal.grid(row = 8, column = 2, padx = 2.5, pady = 2.5,sticky = NSEW) #places the button the grid

minusButton = Button(calculator, text = "+/-", width = 10, height = 3, command = lambda: pressNumber("-")) #creates a button named minusButton, sets the text, width, height and gives it a lambda function which runs the pressNumber function with an input of -

minusButton.grid(row=4, column = 1, padx = 2.5, pady = 2.5, sticky = NSEW) #places the button the grid

percentageButton = Button(calculator, text="%", width = 10, height = 3, command = lambda: [pressNumber("/100"), evaluate()]) #creates a button named percentageButton, sets the text, width, height and gives it a lambda function which runs the pressNumber function with an input of /100 and then runs the evaluate function

percentageButton.grid(row = 4, column = 2, padx = 2.5, pady = 2.5,sticky = NSEW) #places the button the grid



#CREATE INPUTS?


calculator.bind('9', lambda event: pressNumber('9')) #When the user presses the number 9 it runs a the pressNumber function with an input of 9
calculator.bind('8', lambda event: pressNumber('8'))
calculator.bind('7', lambda event: pressNumber('7'))
calculator.bind('6', lambda event: pressNumber('6'))
calculator.bind('5', lambda event: pressNumber('5'))
calculator.bind('4', lambda event: pressNumber('4'))
calculator.bind('3', lambda event: pressNumber('3'))
calculator.bind('2', lambda event: pressNumber('2'))
calculator.bind('1', lambda event: pressNumber('1'))
calculator.bind('0', lambda event: pressNumber('0'))

calculator.bind('%', lambda event: [pressNumber("/100"), evaluate()]) #When the user presses the % button it runs the pressNumber function to divide by 100 and then evaluates the result with the evaluate function
calculator.bind('+', lambda event: pressNumber("+")) #When the user presses the + button it runs a the pressNumber function with an input of +
calculator.bind('x', lambda event: pressNumber("*"))
calculator.bind('*', lambda event: pressNumber("*"))
calculator.bind('/', lambda event: pressNumber("/"))
calculator.bind('-', lambda event: pressNumber("-"))
calculator.bind('.', lambda event: pressNumber("."))

calculator.bind('<Return>', lambda event: evaluate()) #when the user presses the enter key the caluclator will run the evaluate function


#RUN THE CALCULATOR
calculator.mainloop() #uses the mainloop function of Tkinter to run the calculator window
