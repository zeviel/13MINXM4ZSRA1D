import amino
from src.utils import configs
from tabulate import tabulate
from src.utils.main_functions import Login
from src.utils.main_functions import ChatRaid
from src.utils.main_functions import Communities
from src.utils.main_functions import CommentRaid

class MainApp:
	def start(self):
		print(f"{configs.COLORS[2]}{configs.LOGO}")
		self.client = amino.Client()
		Login.login(self.client)
		self.sub_client = amino.SubClient(
			comId=Communities.communities(
				self.client), profile=self.client.profile)
		while True:
			try:
				print(tabulate(
					configs.MAIN_MENU,
					headers=[configs.CATEGORIES[0]],
					tablefmt="fancy_grid"))
				select = int(input("[Select]::: "))
				if select == 1:
					ChatRaid(self.client, self.sub_client).start()
				elif select == 2:
					CommentRaid(self.client, self.sub_client).start()
				elif select == 3:
					print(tabulate(
						configs.MESSAGE_TYPES,
						headers=[configs.CATEGORIES[3]],
						tablefmt="presto"))
			except Exception as e:
				print(e)

MainApp().start()
