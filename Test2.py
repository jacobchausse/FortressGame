import tkinter

class RandomStuffs:
    def __init__(self, var1):
        self.n1 = var1
        self.var1 = var1
        self.color = 'white'
        
    def thingy(self):
        
        if self.n1 == self.var1:
            self.color = 'white'
            self.n1 = '1'
            
        else:
            self.color = 'blue'
            self.n1 = self.var1
        
        buttontext.set(self.n1)
        
        A.config(bg = self.color) 


in1 = input('what\'s on the button?   ')


p1 = RandomStuffs(in1)

top = tkinter.Tk()
top.geometry('100x100')


w = tkinter.Label(top, text="Testing code", bg='red', fg='white', font='Arial')

B = tkinter.Button(top, text='button', command=p1.thingy, bg='black', fg='white' )

buttontext = tkinter.StringVar()
A = tkinter.Button(top, textvariable=buttontext)
buttontext.set(p1.n1)


C = tkinter.Button(top, text='QUIT', command=top.destroy)


w.grid(row=0,column=0)

C.place(x=70,y=30)

B.grid(row=1,column=0)

A.grid(row=2,column=0)


top.mainloop()