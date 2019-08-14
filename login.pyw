import json
import tkinter as tk 
from tkinter.messagebox import showwarning

import account

class login_screen:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Login screen")
		self.root.geometry('280x220+580+300')
		self.root.attributes('-topmost', True)
		self.window = tk.Frame(self.root, bg = "#A3BAC3")
		tk.Label(self.window, text = "Login", bg = "#EAEBED", 
			fg = "#2F2F2F", bd=5, font=('Calibri',16,'bold')).pack(fill = tk.X)
		self.username = ""
		self.password = ""
		self.play = False
		
		tk.Label(self.window, text = "Username:", bg = "#A3BAC3", font=('Calibri',13,'bold')).pack(pady = 2)
		self.Username = tk.Entry(self.window, width = 20, textvariable = self.username, bd=5, bg ="#01A7C2", 
			relief = tk.GROOVE,font=('Calibri',13,'bold'))
		#self.Username.insert(tk.END, "enter your username")
		self.Username.pack()
		
		tk.Label(self.window, text = "Password:", bg = "#A3BAC3",font=('Calibri',13,'bold')).pack(pady = 2) 
		self.Password = tk.Entry(self.window, width = 20, textvariable = self.password, show="*", bd =5, bg ="#01A7C2",
			relief = tk.GROOVE, font=('Calibri',13,'bold'))
		self.Password.pack()

		self.Create_Acc = tk.Button(self.window, text = "New user?", bg = "#F6F930", font=('Calibri',13,'bold'), 
			command = self.creatacc, relief = tk.FLAT, fg= "#2F2F2F")
		self.Create_Acc.pack( pady = 7)
		self.Password.bind('<Return>',self.passcheck)

		self.window.pack(fill = tk.BOTH, expand = 1)
			
	def passcheck(self,*args):
		self.getdetails()
		if read_from_file(self.username, self.password):
			self.play = True
			self.quitwindow()
		else:
			showwarning('INCORRECT CREDENTIALS','Please check the login credentials')
			self.Username.delete(0,tk.END)
			self.Password.delete(0,tk.END)

	def creatacc(self,*args):
		self.root.destroy()
		self.username = account.make_account()
	
	def getdetails(self):
		self.username = self.Username.get()
		self.password = self.Password.get()

	def quitwindow(self):
		self.root.destroy()

def read_from_file(name, password):
	with open('records') as ref:
		longs = json.load(ref)
	return longs.get(name) == password

def main():
	Window = login_screen()
	tk.mainloop()
	return Window.username

if __name__ == '__main__':
	print(main())