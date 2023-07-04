import tkinter as tk
from tkinter import StringVar

expression = ""
new_exp = '!'
lst_val = ['1', '2', '3' ,'4', '5', '6', '7', '8', '9', '0', '.']
rep = {str(chr(247)):'/', 'mod':'%', 'x':'*', 'ANS':str(new_exp)}

def inputing_to_calculator(num : str, equation, top):
    global expression
    
    if expression == "" and (num == 'mod' or num == str(chr(247)) or num == 'x' or num == ')'):
        return
    
    if expression == "" and num == '.':
        expression += '0.0'
        equation.set(expression)    
        top.config(text=expression)
        return
    
    characters = [char for char in expression]
    
    for _ in range(0,len(expression)):
        if len(expression) == 0:
            break
        
        if num in lst_val and (characters[-1] == ')' or characters[-1] == 'S') and num != '.':
            expression += f'x{num}'
            equation.set(expression)
            top.config(text=expression)
            
            return
        
        if num == '(' and (characters[-1] in lst_val or characters[-1] == ')' or characters[-1] == 'S'):
            expression += f'x{num}'
            equation.set(expression)
            top.config(text=expression)
            
            return
        
        if num == ')' and (characters[-1] == '+' or characters[-1] == '-' or characters[-1] == 'x' or characters[-1] == str(chr(247)) or characters[-1] == 'd'):
            return
        
        if num == 'ANS' and (characters[-1] in lst_val or characters[-1] == ')' or characters[-1] == 'S'):
            expression += f'x{num}'
            equation.set(expression)
            top.config(text=expression)
            
            return
        
        if num == 'mod' and (characters[-1] == 'd' or characters[-1] == '('):
            return
        
        if (num == 'x' or num == str(chr(247)) or num == '+') and\
            (characters[-1] == 'x' or characters[-1] == str(chr(247)) or characters[-1] == '+' or characters[-1] == '('):
                expression = expression[:-1] + num
                equation.set(expression)
                top.config(text=expression)
                
                return
        
        if num == '.':
            count = 0
            
            for char in characters:
                
                if char not in lst_val:
                    count = 0
                elif char == '.':
                    count += 1
                    
            if count >= 1 or characters[-1] not in lst_val:
                return
            elif count == 1:
                break
    
    expression += num
        
    equation.set(expression)    
    top.config(text=expression)

def solution(equation, bot, top):
    global expression, new_exp

    if expression == "":
        return
    
    for i, j in rep.items():
        expression = expression.replace(i, j)

    try:
        for i in range(len(expression)):
            if expression[i] == '.' and expression[i + 1] == '.':
                raise EOFError
        
        if expression != "" :
            new_exp = str(eval(expression))
            
            if len(new_exp) >= 25:
                expression = ""
                equation.set("")
                rep['ANS'] = '!'
                bot.config(text="The expression is to long")
                top.config(text="")
                return
            
            bot.config(text=new_exp)
            equation.set(new_exp)
            expression = ""
            rep['ANS'] = new_exp
        else:
            raise EOFError
    except:
        for i, j in rep.items():
            expression = expression.replace(j, i)
        equation.set(expression)
        bot.config(text="Invalid")
    
def back(equation, top):
    global expression
    
    if expression == "":
        top.config(text="0")
        return
    
    for i, j in rep.items():
        # Displays every space with ANS
        expression = expression.replace(j, i)    
    
    characters = [character for character in expression]
    
    if characters[-1] == 'd' or characters[-1] == 'S':
        expression = expression[:-3]
        equation.set(expression)
        top.config(text=expression)
    else:
        expression = expression[:-1]
        equation.set(expression)
        top.config(text=expression)
    
def check_s(expression, len_expression):
    
    if len_expression - 3 == 0:
        ex_sign = '-'
        expression = ex_sign + expression
        return expression
    
    ex_find_ANS = expression[len_expression - 3:] # S
    ex_remove_before = expression[:len_expression - 3]
    ex_sign = expression[len(ex_remove_before) - 1]
    
    if ex_sign == '+':
        ex_sign = '-'
        expression = ex_remove_before[:len(ex_remove_before)-1] + ex_sign + ex_find_ANS
    elif ex_sign == '-':
        ex_sign = '+'
        expression = ex_remove_before[:len(ex_remove_before)-1] + ex_sign + ex_find_ANS
    else:
        ex_sign = '-'
        expression = ex_remove_before + ex_sign + ex_find_ANS
    
    return expression
    
def check_number(expression, len_expression, count_numbers):
    if len_expression - count_numbers == 0:
        ex_sign = '-'
        ex_numbers = expression[:count_numbers]
        expression = ex_sign + ex_numbers
        return expression

    ex_numbers = expression[len_expression - count_numbers:]
    ex_letters = expression[:len_expression - count_numbers]
    ex_sign = ex_letters[len(ex_letters) - 1:]

    if ex_sign == '+':
        ex_sign = '-'
        expression = ex_letters[:len(ex_letters)-1] + ex_sign + ex_numbers
    elif ex_sign == '-':
        ex_sign = '+'
        expression = ex_letters[:len(ex_letters)-1] + ex_sign + ex_numbers
    else:
        ex_sign = '-'
        expression = ex_letters + ex_sign + ex_numbers
        
    return expression
    
def negate(equation, top):
    global expression 
    
    len_expression = len(expression)
    count_numbers = 0
    
    if expression == "":
        return
    
    # check the consecuitive numbers
    for i in range(len_expression):
        if expression[i] in lst_val:
            count_numbers += 1
        else:
            count_numbers = 0
            
    the_S = expression[count_numbers - 1].upper()
    
    if count_numbers == 0 and the_S != 'S':
        return

    if the_S == 'S':
        expression = check_s(expression, len_expression)
    else:
        expression = check_number(expression, len_expression, count_numbers)
    
    equation.set(expression)
    top.config(text=expression)

def percentage(equation, top):
    global expression

    len_expression = len(expression)
    count = 0
    value_ans = rep['ANS']
    
    if expression == "":
        print("IN")
        return
    
    characters = [_ for _ in expression]
    i = 1
    # Check if it is a number
    while i <= len_expression:
        if characters[-i] not in lst_val or characters[-i] == (None or ""):
            break
        
        count += 1
        i += 1
        
    numbers = expression[-count:]
    values = expression[:-count]
    
    print(count)
        
    if count != 0:
        the_value = str(float(numbers)/100)
        expression = values + the_value
        print(expression)
    elif characters[-i] == 'S' and value_ans != '!':
        the_value = str(float(value_ans)/100)
        expression = expression[:-3]
        expression += the_value
    else:
        return

    equation.set(expression)
    top.config(text=expression)

def button_inputs(val : str, eq, top, bot):
    global expression, new_exp
    
    if len(expression) >= 25:
        expression = 'Invalid'
        top.config(text=expression)
        expression = ''
        eq.set(expression)
        
        return
    
    if val not in ['=', 'CE', '<', str(chr(177)), '%']:
        inputing_to_calculator(val, eq, top)
    elif val == '=' :
        solution(eq, bot, top)
    elif val == '<':
        back(eq, top)
    elif val == str(chr(177)):
        negate(eq, top)
    elif val == '%':
        percentage(eq, top)
    elif val == 'CE':
        expression = ""
        new_exp = '!'
        rep['ANS'] = new_exp
        eq.set("")
        top.config(text="")
        bot.config(text="")
    
def window(myRoot):
    # Title
    myRoot.title("Calculator")
    
    # Size of Window
    window_width = 330 # 315
    window_height = 415
    
    # get the screen dimension
    size_width = myRoot.winfo_screenwidth()
    size_height = myRoot.winfo_screenheight()

    # find the center point
    center_x = int(size_width/2 - window_width/2)
    center_y = int(size_height/2 - window_height/2)
    
    myRoot.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    myRoot.resizable(False, False)

def body(root ,eq):
    
    newFrame = tk.Frame(root)
    newFrame.grid(row=0, sticky=tk.NSEW)
    
    top, bot = body_up(newFrame, eq)
    body_down(newFrame, eq, top, bot)
    
    return newFrame
    
def body_up(root, eq):
    global expression, new_exp0
    
    myFrame = tk.Frame(root, width= 50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1, bg='white')
    myFrame.grid(row=0, column=0, sticky=tk.EW)

    # Create two labels, one containing Text and the other only label
    topLabel = tk.Label(
        myFrame,
        height= 2,
        bg='white',
        font=('Helvetica bold', 15, 'bold')
    )
    topLabel.grid(row=0, sticky=tk.W)
    
    bottomLabel = tk.Label(
        myFrame,
        height= 2,
        bg='white',
        font=('Helvetica bold', 15, 'bold')
    )
    bottomLabel.grid(row=1, sticky=tk.W)
    
    return topLabel, bottomLabel
    
def body_down(root, eq, topLabel, bottomLabel):
    # Horizontal
    myList : list = [
        ['mod','%' ,'7', '4', '1', str(chr(177))], 
        ['ANS', '(','8', '5', '2','0'],
        ['CE', ')','9', '6', '3', '.'], 
        ['<', str(chr(247)),'x', '-', '+', '=']
    ]
    
    colorBack : list = [
        ['white', 'white','white', 'white', 'white', 'white'], 
        ['white', 'white','white', 'white', 'white','white'],
        ['#FF2E2E', 'white','white', 'white', 'white', 'white'], 
        ['#FF2E2E', 'white','white', 'white', 'white', '#01949A']
    ]
    
    myFrame = tk.Frame(root)
    myFrame.grid(row=1, sticky=tk.EW)
    
    for i in range(6):
        for j in range(4):
            tk.Button(
                master=myFrame,
                width= 5,
                height= 1,
                bg=colorBack[j][i],
                fg="black",
                text=f"{myList[j][i]}",
                anchor= tk.CENTER,
                borderwidth=0.5,
                font=('Helvetica bold', 19, 'bold'),
                command= lambda btn=myList[j][i]: button_inputs(btn, eq, topLabel, bottomLabel)
            ).grid(row=i, column=j)
    return myFrame
            
def my_app():
    root = tk.Tk()
    equation = StringVar()
    
    window(root)
    
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    
    body(root, equation)
    
    root.mainloop()
    
if __name__ == '__main__':
    my_app()