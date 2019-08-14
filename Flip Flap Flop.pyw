from os import system

import tkinter as tk 

from PIL import Image, ImageTk

import login, quickplay, leaderboard, credits

class MainWindow:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title('Flip Flap Flop The Game')
		self.root.geometry('400x300+500+300')
		self.root.configure(background = "#071E3D")

		self.heading = tk.Frame(self.root, bg ="#19647E")

		loader = Image.open('logo.png')
		render = ImageTk.PhotoImage(loader)

		loader1 = Image.open('log1.png')
		render1 = ImageTk.PhotoImage(loader1)

		self.logo = tk.Label(self.heading, image = render, bg ="#19647E")
		self.logo.image = render
		self.logo.pack(side = tk.LEFT, padx = 3)

		self.log1 = tk.Label(self.heading, image = render1, bg ="#19647E")
		self.log1.image = render1
		self.log1.pack(side = tk.RIGHT, padx = 3)

		tk.Label(self.heading, text = "Flip Flap Flop", font = ("Calibri", 30, "bold")
			, fg = "#FFC857", bg ="#19647E").pack(fill = tk.X)

		self.heading.pack(fill = tk.BOTH)

		self.player_name = ""
		with open(".\\Database\\scores.LOG") as reds:
			namer = reds.readlines()[-1].split("'s score: ")[0]
			self.winner_name = f"The Winner Is {namer}"

		self.winner = tk.Frame(self.root)
		tk.Label(text = self.winner_name, font = ("Calibri", 14, "bold"), 
			bg = "#119DA4", fg = "#1F2041").pack(fill = tk.X)
		self.winner.pack()

		self.play_buttons = tk.Frame(self.root, bg = "#071E3D")
		self.login_button = tk.Button(self.play_buttons, text = "Play", command = self.Login
			, font = ("Calibri", 24, "bold"), relief = tk.GROOVE, width = 10, bg ="#C1224F", fg ="#EFE6DD")
		self.login_button.pack(side = tk.LEFT, padx = 10)
		self.qvick = tk.Button(self.play_buttons, text ="Quick Play", command = self.Quick
			, font = ("Calibri", 24, "bold"), relief = tk.GROOVE, width = 10, bg ="#F16F6F", fg ="#EFE6DD")
		self.qvick.pack(padx = 10)
		self.play_buttons.pack(fill = tk.BOTH, padx = 1, pady = 20)

		self.info_buttons = tk.Frame(self.root, bg = "#071E3D")
		self.leaders = tk.Button(self.info_buttons, text = "LeaderBoard", command = self.LeaderBoard
			, font = ("Calibri", 24, "bold"), relief = tk.GROOVE, width = 10, bg ="#94D2E6", fg ="#2C302E")
		self.leaders.pack(side = tk.LEFT, padx = 10)
		self.creds = tk.Button(self.info_buttons, text = "Credits", command = self.Credits
			, font = ("Calibri", 24, "bold"), relief = tk.GROOVE, width = 10, bg ="#FFF78F", fg ="#2C302E")
		self.creds.pack(padx = 10)
		self.info_buttons.pack(fill = tk.BOTH, pady = 15)

	def Login(self):
		self.root.destroy()
		self.player_name = login.main()
		self.start_the_game()

	def Quick(self):
		self.root.destroy()
		self.player_name = quickplay.main()
		self.start_the_game()
		

	def LeaderBoard(self):
		leaderboard.main()

	def Credits(self):
		credits.main()

	def start_the_game(self):
		system(f'python main_game.pyw {self.player_name}')

def main_loop():
	Window = MainWindow()
	tk.mainloop()

if __name__ == '__main__':
	main_loop()
