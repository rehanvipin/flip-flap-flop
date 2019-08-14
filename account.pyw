import json
import tkinter as tk
from tkinter.messagebox import showwarning

class creator:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title('Create your account')
		self.root.geometry('290x219+580+350')

		self.window = tk.Frame(self.root, bg = "#A3BAC3")
		self.username = ""
		self.password = ""
		self.confirm = ""

		tk.Label(self.window, text = "Make Account", font=("Calibri", 20,"bold"), bg = "#A3BAC3", 
			fg = "#2F2F2F").pack(fill = tk.BOTH, pady = 10)

		self.usn_wind = tk.Frame(self.window, bg = "#A3BAC3")
		tk.Label(self.usn_wind, text = "Username:", font = ("Calibri",12,"bold"), bg = "#A3BAC3").pack(side = tk.LEFT)

		self.Username = tk.Entry(self.usn_wind, width = 16, font = ("Calibri",12,"bold"), relief = tk.GROOVE, bd = 3,
		fg = "#FFE900", bg = "#007090")
		self.Username.pack(fill = tk.X)
		self.usn_wind.pack(fill= tk.BOTH, pady = 5)

		self.pas_wind = tk.Frame(self.window, bg = "#A3BAC3")
		tk.Label(self.pas_wind, text = "Password:", font = ("Calibri",12,"bold"), bg = "#A3BAC3").pack(side =tk.LEFT)

		self.Password = tk.Entry(self.pas_wind, width = 15, font = ("Calibri",12,"bold"), show = "*", relief = tk.GROOVE,
		 bd = 3, fg = "#FFE900", bg = "#007090")
		self.Password.pack(fill = tk.X)
		self.pas_wind.pack(fill= tk.BOTH, pady = 5)

		self.con_wind = tk.Frame(self.window, bg = "#A3BAC3")
		tk.Label(self.con_wind, text = "Confirm It:", font = ("Calibri",12,"bold"), bg = "#A3BAC3").pack(side = tk.LEFT)

		self.Confirm = tk.Entry(self.con_wind, width = 15, font = ("Calibri",12,"bold"), show = "*", relief = tk.GROOVE, 
			bd = 3, fg = "#FFE900", bg = "#007090")
		self.Confirm.bind('<Return>', self.verify_password)
		self.Confirm.pack(fill = tk.X)
		self.con_wind.pack(fill= tk.BOTH, pady = 5)

		self.Go = tk.Button(self.window, text = "Play!", font = ("Calibri",14,"bold"), command = self.verify_password,
		 bd = 3, relief = tk.FLAT, bg="#F5FBEF", fg ="#2F2F2F")
		self.Go.pack(side = tk.BOTTOM, pady = 3)

		self.window.pack(fill = tk.BOTH)
		self.root.lift()
		self.root.focus()

	def verify_password(self,*args):
		self.username = self.Username.get()
		self.password = self.Password.get()
		self.confirm = self.Confirm.get()

		if (self.username not in self.record_get_list()) and (self.username.strip()):
			if self.password.strip() and self.password == self.confirm:
				self.record_add_list(self.username, self.password)
				self.root.quit()
			else:
				showwarning("Invalid Password","The passwords do not match\n The password cannot be null")
				self.Password.delete(0,tk.END)
				self.Confirm.delete(0,tk.END)
		else:
			showwarning("Give new username","That username already exists! Give a new one")
			self.Username.delete(0,tk.END)

	def record_get_list(self):
		with open('records') as reader:
			recorder = json.load(reader)
		return recorder

	def record_add_list(self, name, password):
		current = self.record_get_list()
		current[name] = password
		with open('records','w') as writer:
			json.dump(current, writer)

	def get_creds(self):
		self.root.destroy()
		return self.username,self.password

def make_account():
	Window = creator()
	tk.mainloop()
	return Window.get_creds()[0]

if __name__ == '__main__':
	print(make_account())