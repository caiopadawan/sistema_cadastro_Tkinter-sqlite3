from tkinter import *

application = Tk()
application.title('Sistema de Cadasrto')
application.geometry("640x480+100+100")
application['bg'] = 'gray'
application.resizable(False, False)
lb_1 = Label(application,
			text='Inserindo uma Label',
			background='green',
			fg='red',
			font='Arial 20',
			width=30)
btn_1 = Button(application,
				text='OK',
				background='black',
				fg='white',
				width=30,
				font='Arial 18',
				anchor=W)
lb_1.pack()
btn_1.pack()

application.mainloop()


