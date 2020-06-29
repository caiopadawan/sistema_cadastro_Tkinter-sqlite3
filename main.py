from tkinter import *

application = Tk()
application.title('Sistema de Cadasrto')
application.geometry("640x480+100+100")
application['bg'] = 'red'
application.resizable(False, False)
btn_1 = Button(application,
				text='OK',
				background='black',
				fg='white',
				width=30)
				
btn_1.pack()

application.mainloop()


