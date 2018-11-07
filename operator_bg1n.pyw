import tkinter as tk
from sys import argv
from os import system

class welcome_screen():
	""" This is the login screen for the all users """
	def __init__(me):
		me.main_window = tk.Tk()
		me.main_window.title('the game of the century')
		me.main_window.geometry('300x200')

		me.title = tk.Label(me.main_window,text='The game of the century')
		me.title.pack()

		me.clicky_stuff = tk.Frame(me.main_window, padx= 10, pady = 10)
		me.start = tk.Button(me.clicky_stuff,text='start', fg='white', font = ('Helvetica',18,'bold'), 
			bg ='green',height= 1, width=3, command = me.open_game)
		me.end = tk.Button(me.clicky_stuff,text='quit', fg='#f4f442', font = ('Helvetica',18,'bold'),
		 bg='red', height=1, width=3, command = me.main_window.quit, padx = 10)
		me.start.pack(side=tk.LEFT)
		me.end.pack(side=tk.RIGHT)
		me.clicky_stuff.pack()

		me.button_click = 0

		me.datainfo = tk.Frame(me.main_window)
		me.datainfo.pack(fill= tk.BOTH)
		me.showYstuff = tk.Label(me.datainfo, background= 'red')
		me.showYstuff.config(text=f'the button has been clicked {me.button_click} times')
		me.showYstuff.pack()

	def play_command(self):
		self.button_click += 1
		self.showYstuff.config(text=f'the button has been clicked {self.button_click} times')
		return self.button_click

	def open_game(self):
		system(r'.\main_game.pyw')

def main():
	obx = welcome_screen()
	tk.mainloop()
	times = obx.play_command()
	# print(argv[1:])

if __name__ == '__main__':
	main()