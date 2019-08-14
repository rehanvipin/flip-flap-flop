import tkinter as tk

class LeaderBoard:
	def __init__(self):

		self.toor = tk.Tk()
		self.toor.title("The winners")

		self.root = tk.Frame(self.toor, bg ="#DC493A")

		tk.Label(self.root, text = "LEADERBOARD", font=('Calibri',20,'bold'), 
			fg ="#262626", bg ="#DC493A", relief = tk.GROOVE).pack(fill = tk.BOTH, pady = 3)

		self.score_frame = tk.Frame(self.root, bg ="#006494")

		self.rank_frame = tk.Frame(self.root, bg ="#006494")
		tk.Label(self.rank_frame, text = "Rank", font=('Calibri',13,'bold'), fg ="#262626", bg ="#006494").pack(side = tk.TOP)
		self.rank_list = tk.Listbox(self.rank_frame, font=('Calibri',12,'bold'),
			justify = tk.CENTER, bg ="#E2E8DD")
		self.fillup(0)
		self.rank_list.pack()
		self.rank_frame.pack(side = tk.LEFT, fill = tk.BOTH)

		self.name_frame = tk.Frame(self.root, bg ="#006494")
		tk.Label(self.name_frame, text = "Username", font=('Calibri',13,'bold'), fg ="#B7D1DA", bg ="#006494").pack(side = tk.TOP)
		self.name_list = tk.Listbox(self.name_frame, font=('Calibri',12,'bold'),
			justify = tk.CENTER, bg ="#E2E8DD")
		self.fillup(1)
		self.name_list.pack()
		self.name_frame.pack(fill = tk.BOTH, side = tk.LEFT)

		tk.Label(self.score_frame, text = "Score", font=('Calibri',13,'bold'), fg ="#262626", bg ="#006494").pack(side = tk.TOP)

		self.score_list = tk.Listbox(self.score_frame, 
			font=('Calibri',12,'bold'), justify = tk.CENTER, bg ="#E2E8DD")
		self.fillup(2)

		self.scroll_bar = tk.Scrollbar(self.score_frame)
		self.scroll_bar.config(command = self.multiple_scrolls)
		self.rank_list.config(yscrollcommand = self.scroll_bar.set)
		self.name_list.config(yscrollcommand = self.scroll_bar.set)
		self.score_list.config(yscrollcommand = self.scroll_bar.set)
		self.scroll_bar.pack(side = tk.RIGHT,fill=tk.Y)

		self.score_list.pack()
		self.score_frame.pack(side = tk.LEFT, fill = tk.BOTH)

		self.root.pack(fill = tk.BOTH)

	def multiple_scrolls(self,*args):
		self.name_list.yview(*args)
		self.rank_list.yview(*args)
		self.score_list.yview(*args)

	def fillup(self, l_no):
		with open('.\\Database\\scores.LOG') as file:
			log = file.readlines()
		log = list(map(lambda x:x.strip().split("'s score: "),log))[1:][::-1]
		record = [[],[],[]]
		for i in log:
			if (i[0] not in record[1]) and (i[0] != "admin"):
				record[1].append(i[0])
				record[0].append(str(len(record[0])+1))
				record[2].append(i[1])

		for i in range(len(record[1])):
			if l_no == 0:
				self.rank_list.insert(tk.END,record[0][i])
			elif l_no == 1:
				self.name_list.insert(tk.END,record[1][i].title())
			else:
				self.score_list.insert(tk.END,record[2][i])

def main():
	Window = LeaderBoard()
	tk.mainloop()

if __name__ == '__main__':
	main()
