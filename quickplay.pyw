import tkinter as tk

class Quick:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title('Speedy play')
		self.root.geometry('280x140+650+350')
		self.name = ""
		self.window = tk.Frame(self.root, bg ="#299B15")
		tk.Label(self.window, text = "Quick Play", font=('Calibri', 20,'bold'), bg ="#235B00",
		 fg="#B8F948").pack(fill= tk.X,pady= 5)
		tk.Label(self.window, text = "Enter a name and go!", font=('Calibri', 16,'bold'), bg ="#299B15", 
			fg ="#B8F948").pack(pady = 5)

		self.Name = tk.Entry(self.window, width = 16, font=('Calibri', 16,'bold'), 
			justify = tk.CENTER, bg="#A9F99A", fg ="#4C6832", bd = 3, relief = tk.GROOVE)
		self.Name.insert(0,"Player-2")
		self.Name.bind('<Return>', self.setname)
		self.Name.pack(pady= 5, ipady = 5)

		self.window.pack(fill = tk.BOTH)

	def setname(self, *args):
		self.name = self.Name.get()
		self.root.destroy()
		return self.name

def main():
	Window = Quick()
	tk.mainloop()
	return "temp-"+Window.name

if __name__ == '__main__':
	print(main())