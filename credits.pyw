import tkinter as tk 

def show_the_fun():
	text = """   Ice Cold Articuno \nand\n Team LEGION"""
	root = tk.Tk()
	root.geometry('225x245+580+200')
	root.title('Credits')
	fram = tk.Frame(root, bg = "#A3BAC3")
	tk.Label(fram, text = "MADE BY", font =('Calibri', 20, "bold"), 
		bg = "#A3BAC3").pack(fill = tk.X, pady = 3)
	tk.Label(fram, text = text, font = ('Calibri',20, 'bold')
		, bg ="#A3AAFF", fg= "#4F4F9F", height = 195).pack(fill = tk.BOTH, padx = 3)

	fram.pack(fill = tk.BOTH)

def main():
	show_the_fun()
	tk.mainloop()

if __name__ == '__main__':
	main()