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
		me.datainfo.pack(expand = 1)
		me.showYstuff = tk.Label(me.datainfo, background= '#f00ff0', font = ('Helvetica',14))
		me.showYstuff.config(text='Press x to pause the game', pady = 3)
		me.showscore = tk.Label(me.datainfo, background = "Blue", font = "ComicSansms", pady = 3)

		with open('.\\Database\\scores.LOG','r') as tops:
			me.showscore.config(text = "highscore  " + tops.readlines()[-1])

		me.showscore.pack(fill = tk.Y)
		me.showYstuff.pack()

	def open_game(self):
		system(r'python main_game.pyw')
		

def loginScr():
	obx = welcome_screen()
	tk.mainloop()

if __name__ == '__main__':
	loginScr()
