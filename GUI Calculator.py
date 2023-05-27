import tkinter as tk 

calculation = ""

def add_to_calculation(symbol):
    global calculation # Global so we can manipulate it inside the function

    calculation += str(symbol) # No matter if it is an integer it will be type casted as a string
    text_result.delete(1.0, "end") # Deletes everything in text box
    text_result.insert(1.0, calculation) # 1.0 is the index where we insert the string. The string itself will be the calculation

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk() # This creates the actual window the calculator is on
root.geometry("300x275") # This is the measurements of the window 

text_result = tk.Text(root, height = 2, width = 16, font=("Great Vibes", 24))
text_result.grid(columnspan=5) #Creates a grid structure that has 5 columns and the text should be across all the columns

# Adding a button to a root with text 1 and command that refrences the function. We use lambda to refer to function instead of calling the function
btn_1 = tk.Button(root, text = "1", command = lambda: add_to_calculation(1), width = 5, font=("Great Vibes", 14))
btn_1.grid(row = 2, column = 1, )

btn_2 = tk.Button(root, text = "2", command = lambda: add_to_calculation(2), width = 5, font=("Great Vibes", 14))
btn_2.grid(row = 2, column = 2, )

btn_3 = tk.Button(root, text = "3", command = lambda: add_to_calculation(3), width = 5, font=("Great Vibes", 14))
btn_3.grid(row = 2, column = 3, )

btn_4 = tk.Button(root, text = "4", command = lambda: add_to_calculation(4), width = 5, font=("Great Vibes", 14))
btn_4.grid(row = 3, column = 1, )

btn_5 = tk.Button(root, text = "5", command = lambda: add_to_calculation(5), width = 5, font=("Great Vibes", 14))
btn_5.grid(row = 3, column = 2, )

btn_6 = tk.Button(root, text = "6", command = lambda: add_to_calculation(6), width = 5, font=("Great Vibes", 14))
btn_6.grid(row = 3, column = 3, )

btn_7 = tk.Button(root, text = "7", command = lambda: add_to_calculation(7), width = 5, font=("Great Vibes", 14))
btn_7.grid(row = 4, column = 1, )

btn_8 = tk.Button(root, text = "8", command = lambda: add_to_calculation(8), width = 5, font=("Great Vibes", 14))
btn_8.grid(row = 4, column = 2, )

btn_9 = tk.Button(root, text = "9", command = lambda: add_to_calculation(9), width = 5, font=("Great Vibes", 14))
btn_9.grid(row = 4, column = 3, )

btn_0 = tk.Button(root, text = "0", command = lambda: add_to_calculation(0), width = 5, font=("Great Vibes", 14))
btn_0.grid(row = 5, column = 2 )

btn_plus = tk.Button(root, text = "+", command = lambda: add_to_calculation("+"), width = 5, font=("Great Vibes", 14))
btn_plus.grid(row = 2, column = 4 )

btn_minus = tk.Button(root, text = "-", command = lambda: add_to_calculation("-"), width = 5, font=("Great Vibes", 14))
btn_minus.grid(row = 3, column = 4 )

btn_mult = tk.Button(root, text = "x", command = lambda: add_to_calculation("*"), width = 5, font=("Great Vibes", 14))
btn_mult.grid(row = 4, column = 4 )

btn_div = tk.Button(root, text = "/", command = lambda: add_to_calculation("/"), width = 5, font=("Great Vibes", 14))
btn_div.grid(row = 5, column = 4 )

btn_opar = tk.Button(root, text = "(", command = lambda: add_to_calculation("("), width = 5, font=("Great Vibes", 14))
btn_opar.grid(row = 5, column = 1 )

btn_cpar = tk.Button(root, text = ")", command = lambda: add_to_calculation(")"), width = 5, font=("Great Vibes", 14))
btn_cpar.grid(row = 5, column = 3 )

btn_equal = tk.Button(root, text = "=", command = evaluate_calculation, width = 11, font=("Great Vibes", 14))
btn_equal.grid(row = 6, column = 1, columnspan = 2 )

btn_clear = tk.Button(root, text = "C", command = clear_field, width = 11, font=("Great Vibes", 14))
btn_clear.grid(row = 6, column = 3, columnspan = 2 )


root.mainloop() # this runs the main loop that holds everything 