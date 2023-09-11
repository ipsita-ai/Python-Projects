from tkinter import *

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text = '')
first = second = operator = None
def get_operator(op):
    global first,operator
    first = int(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    global first,second,operator
    second = int(result_label['text'])
    if operator == '+':
        result_label.config(text = str(first+second))
    elif operator == '-':
        result_label.config(text = str(first-second))
    elif operator == '*':
        result_label.config(text = str(first*second))
    elif operator == '/':
        if second == 0:
            result_label.config(text='Error')
        else:
            result_label.config(text = str(round(first/second)))


window = Tk()
window.title('Calculator')
window.geometry('250x365')
window.resizable(0,0)
window.configure(bg = '#203345')

result_label = Label(window,text = '' ,bg='#203345',fg='white')
result_label.grid(row = 0,column=0,pady=(10,30),columnspan=10,sticky='w')
result_label.configure(font=('verdana',30,'bold'))
btn7 = Button(window,width=4,height=2,text='7',bg = '#B7D1CE',fg = 'black',command=lambda : get_digit(7))
btn7.grid(row=1,column=0,padx=(2,2),pady=(2,2))
btn7.configure(font=('verdana',14))

btn8 = Button(window,width=4,height=2,text='8',bg = '#B7D1CE',fg = 'black',command=lambda : get_digit(8))
btn8.grid(row=1,column=1,padx=(2,2),pady=(2,2))
btn8.configure(font=('verdana',14))

btn9 = Button(window,width=4,height=2,text='9',bg = '#B7D1CE',fg = 'black',command=lambda : get_digit(9))
btn9.grid(row=1,column=2,padx=(2,2),pady=(2,2))
btn9.configure(font=('verdana',14))

btn_add = Button(window,width=4,height=2,text='+',bg = '#B7D1CE',fg = 'black',command=lambda :get_operator('+'))
btn_add.grid(row=1,column=3,padx=(2,2),pady=(2,2))
btn_add.configure(font=('verdana',14))

btn4 = Button(window,width=4,height=2,text='4',bg = '#B7D1CE',fg = 'black',command=lambda : get_digit(4))
btn4.grid(row=2,column=0,padx=(2,2),pady=(2,2))
btn4.configure(font=('verdana',14))

btn5 = Button(window,width=4,height=2,text='5',bg = '#B7D1CE',fg = 'black',command=lambda : get_digit(5))
btn5.grid(row=2,column=1,padx=(2,2),pady=(2,2))
btn5.configure(font=('verdana',14))

btn6 = Button(window,width=4,height=2,text='6',bg = '#B7D1CE',fg = 'black',command=lambda : get_digit(6))
btn6.grid(row=2,column=2,padx=(2,2),pady=(2,2))
btn6.configure(font=('verdana',14))

btn_sub = Button(window,width=4,height=2,text='-',bg = '#B7D1CE',fg = 'black',command=lambda :get_operator('-'))
btn_sub.grid(row=2,column=3,padx=(2,2),pady=(2,2))
btn_sub.configure(font=('verdana',14))

btn1 = Button(window,width=4,height=2,text='1',bg = '#B7D1CE',fg = 'black',command=lambda : get_digit(1))
btn1.grid(row=3,column=0,padx=(2,2),pady=(2,2))
btn1.configure(font=('verdana',14))

btn2 = Button(window,width=4,height=2,text='2',bg = '#B7D1CE',fg = 'black',command=lambda : get_digit(2))
btn2.grid(row=3,column=1,padx=(2,2),pady=(2,2))
btn2.configure(font=('verdana',14))

btn3 = Button(window,width=4,height=2,text='3',bg = '#B7D1CE',fg = 'black',command=lambda : get_digit(3))
btn3.grid(row=3,column=2,padx=(2,2),pady=(2,2))
btn3.configure(font=('verdana',14))

btn_mul = Button(window,width=4,height=2,text='*',bg = '#B7D1CE',fg = 'black',command=lambda :get_operator('*'))
btn_mul.grid(row=3,column=3,padx=(2,2),pady=(2,2))
btn_mul.configure(font=('verdana',14))

btn_clear = Button(window,width=4,height=2,text='C',bg = '#B7D1CE',fg = 'black',command=lambda :clear())
btn_clear.grid(row=4,column=0,padx=(2,2),pady=(2,2))
btn_clear.configure(font=('verdana',14))

btn0 = Button(window,width=4,height=2,text='0',bg = '#B7D1CE',fg = 'black',command=lambda : get_digit(0))
btn0.grid(row=4,column=1,padx=(2,2),pady=(2,2))
btn0.configure(font=('verdana',14))

btn_equal = Button(window,width=4,height=2,text='=',bg = '#B7D1CE',fg = 'black',command=get_result)
btn_equal.grid(row=4,column=2,padx=(2,2),pady=(2,2))
btn_equal.configure(font=('verdana',14))

btn_div = Button(window,width=4,height=2,text='/',bg = '#B7D1CE',fg = 'black',command=lambda :get_operator('/'))
btn_div.grid(row=4,column=3,padx=(2,2),pady=(2,2))
btn_div.configure(font=('verdana',14))
window.mainloop()