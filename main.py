# Khai bao thu vien tkinter
from tkinter import *

# Set chuc nang cho cac nut bam
def Button_click(number):
    global Operator
    Operator += str(number)
    Text_Input.set(Operator)

# Set chuc nang cho nut clear (xoa toan bo)
def Button_clear():
    global Operator
    Operator = ""
    Text_Input.set("")

# Set chuc nang cho nut bang
def Button_equals():
    global Operator
    # Ham eval(): tinh toan bieu thuc so hoc
    result = str(eval(Operator))
    Text_Input.set(result)

# Set chuc nang cho nut ~ (xoa phan tu vua nhap truoc do)    
def Button_clear1():
    global Operator
    #De lay du lieu duoc nhap vao tu man hinh hay bat cu loai text nao ta dung <Ten bien>.get()
    Operator = Text_Input.get()
    Operator = Operator[0:len(Operator)-1]
    #De hien thi gia tri cua bien ra ma hinh ta dung: <Ten bien>.set(<Gia tri muon hien thi>)
    Text_Input.set(Operator)

# Set cau hinh cho cua so hien len    
Screen = Tk()
Screen.title(string='Calculator')
Screen.iconbitmap(r'c:\Users\Nguye\OneDrive\Máy tính\work_space\project_with_python\may_tinh_cam_tay\logo.ico')
#Screen.geometry("320x500+1000+100")
Screen['background']='#222222'
Screen.resizable(False, False)
Operator = ""
Text_Input = StringVar()

# Set cau hinh cho man hinh hien thi
Display = Entry(Screen,
                # width = 16 co nghia la do rong bang 16 ky tu lien tiep 
                width = 16, 
                font = ('arial', 30, 'bold'), 
                textvariable=Text_Input,
                bd = 10,
                insertwidth=4, 
                bg = '#222222',
                justify = 'right',
                fg = "white").grid(columnspan = 4)
space = Label(Screen, pady = 5, bg = '#222222').grid(row=1,column=0)

# Set cau hinh cho nut 7, padx: chieu dai, fg: mau chu.
Button_7 = Button(Screen,
                  padx = 24,
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 25, 'bold'),
                  text = "7",
                  command=lambda:Button_click(7),
                  bg = '#444444').grid(row = 2, column = 0)

# Set cau hinh cho nut 8
Button_8 = Button(Screen, 
                  padx = 24, 
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 25, 'bold'),
                  text = "8",
                  command=lambda:Button_click(8),
                  bg = '#444444').grid(row = 2, column = 1)

# Set cau hinh cho nut 9
Button_9 = Button(Screen, 
                  padx = 24, 
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 25, 'bold'),
                  command=lambda:Button_click(9),
                  text = "9",
                  bg = '#444444').grid(row = 2, column = 2)

# Set cau hinh cho nut /
Button_dev = Button(Screen, 
                  padx = 31, 
                  pady = 4,
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 22, 'bold'),
                  text = "/",
                  command=lambda:Button_click("/"),
                  bg = '#444444').grid(row = 2, column = 3)

# Set cau hinh cho nut 4
Button_4 = Button(Screen,
                  padx = 24,
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 25, 'bold'),
                  text = "4",
                  command=lambda:Button_click(4),
                  bg = '#444444').grid(row = 3, column = 0)

# Set cau hinh cho nut 5
Button_5 = Button(Screen, 
                  padx = 24, 
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 25, 'bold'),
                  text = "5",
                  command=lambda:Button_click(5),
                  bg = '#444444').grid(row = 3, column = 1)

# Set cau hinh cho nut 6
Button_6 = Button(Screen, 
                  padx = 24, 
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 25, 'bold'),
                  text = "6",
                  command=lambda:Button_click(6),
                  bg = '#444444').grid(row = 3, column = 2)

# Set cau hinh cho nut *
Button_mul = Button(Screen, 
                  padx = 24, 
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 25, 'bold'),
                  text = "×",
                  command=lambda:Button_click("*"),
                  bg = '#444444').grid(row = 3, column = 3)

# Set cau hinh cho nut 1
Button_1 = Button(Screen,
                  padx = 24,
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 25, 'bold'),
                  text = "1",
                  command=lambda:Button_click(1),
                  bg = '#444444').grid(row = 4, column = 0)

# Set cau hinh cho nut 2
Button_2 = Button(Screen, 
                  padx = 24, 
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 25, 'bold'),
                  text = "2",
                  command=lambda:Button_click(2),
                  bg = '#444444').grid(row = 4, column = 1)

# Set cau hinh cho nut 3
Button_3 = Button(Screen, 
                  padx = 24, 
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 25, 'bold'),
                  text = "3",
                  command=lambda:Button_click(3),
                  bg = '#444444').grid(row = 4, column = 2)

# Set cau hinh cho nut -
Button_sub = Button(Screen, 
                  padx = 30, 
                  pady = 4,
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 22, 'bold'),
                  text = "-",
                  command=lambda:Button_click("-"),
                  bg = '#444444').grid(row = 4, column = 3)

# Set cau hinh cho nut C
Button_cls = Button(Screen,
                  padx = 24,
                  pady = 4,
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 22, 'bold'),
                  text = "C",
                  command = Button_clear,
                  bg = '#444444').grid(row = 5, column = 0)

# Set cau hinh cho nut .
Button_dot = Button(Screen, 
                  padx = 31, 
                  pady = 4,
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 22, 'bold'),
                  text = ".",
                  command=lambda:Button_click('.'),
                  bg = '#444444').grid(row = 5, column = 1)

# Set cau hinh cho nut 0
Button_0 = Button(Screen, 
                  padx = 24,
                  pady = 1,
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 25, 'bold'),
                  text = "0",
                  command=lambda:Button_click(0),
                  bg = '#444444').grid(row = 5, column = 2)

# Set cau hinh cho nut +
Button_sum = Button(Screen, 
                  padx = 24, 
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 25, 'bold'),
                  text = "+",
                  command=lambda:Button_click("+"),
                  bg = '#444444').grid(row = 5, column = 3)

# Set cau hinh cho nut (
Button_op = Button(Screen,
                  padx = 30, 
                  pady = 4,
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 22, 'bold'),
                  text = "(",
                  command=lambda:Button_click("("),
                  bg = '#444444').grid(row = 6, column = 0)

# Set cau hinh cho nut )
Button_cl = Button(Screen, 
                  padx = 30, 
                  pady = 4,
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 22, 'bold'),
                  text = ")",
                  command=lambda:Button_click(")"),
                  bg = '#444444').grid(row = 6, column = 1)

# Set cau hinh cho nut =
Button_equa = Button(Screen, 
                  padx = 26, 
                  pady = 4,
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 22, 'bold'),
                  text = "=",
                  command = Button_equals,
                  bg = '#444444').grid(row = 6, column = 2)

# Set cau hinh cho nut ~
Button_1_clear = Button(Screen, 
                  padx = 26, 
                  pady = 4,
                  #bd = 8,
                  fg = 'white',
                  font = ('arial', 22, 'bold'),
                  text = "~",
                  command = Button_clear1,
                  bg = '#444444').grid(row = 6, column = 3)
Screen.mainloop()