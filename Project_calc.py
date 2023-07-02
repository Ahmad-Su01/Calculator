import tkinter as tk
from tkinter import StringVar
expression = ""
new_exp = '!'
lst_val = ['1', '2', '3' ,'4', '5', '6', '7', '8', '9', '0', '.']
rep = {str(chr(247)):'/', 'mod':'%', 'x':'*', 'ANS':str(new_exp)}

def theExp(num : str, equation, top):
    global expression
    
    expression += num
    
    for i in range(len(expression)):
        print("This is expresison: " + expression)
        
        if  expression[i-1] in lst_val: #num == '(' and
            print(expression[i-1] + ": YES")
            break
        else:
            print(expression[i-1] + ": NO")
            break
        
        # if num == '(' and expression[i-1] in lst_val : # or expression[i-1] == 'S' or expression[i-1] == 'd'
        #     expression += 'x('
        #     equation.set(expression)
        #     top.config(text=expression)
        #     return
        
        
        # if num == '(' and (expression[i-1] != 'x' and expression[i-1] != str(chr(247)) and expression[i-1] != '+' and expression[i-1] != '-'): # ('x' or str(chr(247)) or '+' or '-')
        #     expression += 'x('
        #     equation.set(expression)
        #     top.config(text=expression)
        #     return
                
        # if num == '(' and (expression[i-1] not in lst_val or expression[i-1] != 'S'):
        #     expression += '('
        #     equation.set(expression)
        #     top.config(text=expression)
        #     return
        
        if expression[i-1] in 'ANS' and num == 'ANS':
            expression += 'xANS'
            equation.set(expression)
            top.config(text=expression)
            return
        
        if num == 'ANS' and expression[i-1] in lst_val:
            expression += 'xANS'
            equation.set(expression)
            top.config(text=expression)
            return
        
        if num == 'ANS' and expression[i-1] not in lst_val:
            expression += 'ANS'
            equation.set(expression)
            top.config(text=expression)
            return
        
        if num in lst_val and expression[i-1] == 'S':
            expression += f'x{num}'
            equation.set(expression)
            top.config(text=expression)
            return
        
        if num in lst_val and expression[i-1] != 'S':
            break
    
    equation.set(expression)    
    top.config(text=expression)

def solution(equation, bot, top):
    global expression, new_exp

    for i, j in rep.items():
        expression = expression.replace(i, j)
    
    if expression == "None":
        return

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
    
    for i, j in rep.items():
        # Displays every space with ANS
        expression = expression.replace(j, i)    
    
    _new = len(expression)
    count = 0
    
    for i in range(_new):
        if expression[i] in lst_val:
            count += 1
        else:
            count = 0
    
    if expression == "":
        top.config(text="0")
        return

    exp4 = expression[len(expression) - count - 1]  # sign
    exp5 = expression[len(expression) - 1:]
    
    if count == 0 and (exp4 == 'd' or exp4 == 'S'):
        length = len(expression) - 3
        expression = expression[:length]
        equation.set(expression)
        top.config(text=expression)

    elif count == 0 and (exp4 != 'd' or exp4 != 'S'):
        length = len(expression) - 1
        expression = expression[:length]
        equation.set(expression)
        top.config(text=expression)

    elif exp5 != 'd' or exp5 != 'S':
        length = len(expression) - 1
        expression = expression[:length]
        equation.set(expression)
        top.config(text=expression)
        
    elif exp5 == 'd' or exp5 == 'S':
        length = len(expression) - 3
        expression = expression[:length]
        equation.set(expression)
        top.config(text=expression)
    else:
        top.config(text="0") 
    
# Negate functions
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

def myPer(equation, top):
    global expression

    _new = len(expression)
    count = 0
    valueAns = rep['ANS']

    # Check the values before reaching %
    for i in range(_new):
        if expression[i] in ['%']:
            break
        if expression[i] in lst_val:
            count += 1
        else:
            count = 0

    afterExpression = expression[_new - count:]
    beforeExpression = expression[:_new - count]
    
    for i in range(len(beforeExpression)):
        if beforeExpression[i-1] == 'S':
            afterExpression = valueAns
            break
        else:
            break

    if count == 0 and afterExpression.isdigit():
        theValue = str(float(afterExpression)/100)
        
        beforeExpression = beforeExpression[:_new-3]

        expression = beforeExpression + theValue

        equation.set(expression)
        top.config(text=expression)
        return
        
    if count == 0:
        return
        
    theValue = str(float(afterExpression)/100)

    expression = beforeExpression + theValue
    equation.set(expression)
    top.config(text=expression)

def myDiv(myVal, equation, top):
    global expression
    
    expression += myVal

    equation.set(expression)
    top.config(text=expression)

def myMod(myVal, equation, top):
    global expression
    
    expression += myVal
    
    equation.set(expression)
    top.config(text=expression)  

def Working(val : str, eq, top, bot):
    global expression, new_exp
    
    if len(expression) >= 25:
        expression = 'Invalid'
        top.config(text=expression)
        expression = ''
        eq.set(expression)
        
        return
    
    if val not in ['=', 'CE', '<', str(chr(177)), str(chr(247)), 'mod', '%']:
        theExp(val, eq, top)
    elif val == '=' :
        solution(eq, bot, top)
    elif val == '<':
        back(eq, top)
    elif val == str(chr(177)):
        negate(eq, top)
    elif val == '%':
        myPer(eq, top)
    elif val == str(chr(247)):
        myDiv(val, eq, top)
    elif val == 'mod':
        myMod(val, eq, top)
    elif val == 'CE':
        expression = ""
        new_exp = '!'
        rep['ANS'] = new_exp
        eq.set("")
        top.config(text="")
        bot.config(text="")
    
def myWindow(myRoot):
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

def myBody(root ,eq):
    
    newFrame = tk.Frame(root)
    newFrame.grid(row=0, sticky=tk.NSEW)
    
    top, bot = myBody_up(newFrame, eq)
    myBody_down(newFrame, eq, top, bot)
    
    return newFrame
    
def myBody_up(root, eq):
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
    
def myBody_down(root, eq, topLabel, bottomLabel):
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
                command= lambda btn=myList[j][i]: Working(btn, eq, topLabel, bottomLabel)
            ).grid(row=i, column=j)
    return myFrame
            
def myApp():
    root = tk.Tk()
    equation = StringVar()
    
    myWindow(root)
    
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    
    myBody(root, equation)
    
    root.mainloop()
    
if __name__ == '__main__':
    myApp()