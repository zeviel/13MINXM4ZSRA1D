import amino
from src.utils import configs
from tabulate import tabulate
from concurrent.futures import ThreadPoolExecutor

			# -- HELPER FUNCTIONS --


class Login:
	@staticmethod
	def login(client: amino.Client):
		while True:
			try:
				print(
					tabulate(
						configs.LOGIN_MENU,
						headers=[configs.CATEGORIES[4]],
						tablefmt="fancy_grid"))
				select = int(input("[Select]::: "))
				if select == 1:
					email = input("[Email]::: ")
					password = input("[Password]::: ")
					client.login(email=email, password=password)
					break
				elif select == 2:
					SID = input("[SID]::: ")
					client.login_sid(SID=SID)
					break
			except Exception as e:
				print(e)

class Communities:
	@staticmethod
	def communities(client: amino.Client):
		while True:
			try:
				clients = client.sub_clients(start=0, size=100)
				for x, name in enumerate(clients.name, 1):
					print(f"[{x}][{name}]")
				return clients.comId[int(input("[Select the community]::: ")) - 1]
			except Exception as e:
				print(e)

class Chats:
	@staticmethod
	def chats(sub_client: amino.SubClient):
		while True:
			try:
				chats = sub_client.get_chat_threads(start=0, size=100)
				for z, title in enumerate(chats.title, 1):
					print(f"[{z}][{title}]")
				return chats.chatId[int(input("[Select the chat]::: ")) - 1]
			except Exception as e:
				print(e)


			# -- HELPER FUNCTIONS --


			# -- CHAT RAID --

class ChatRaid:
	def __init__(self, client: amino.Client, sub_client: amino.SubClient):
		self.client = client
		self.sub_client = sub_client
	
	def start(self):
		chat_id = Chats.chats(self.sub_client)
		while True:
			try:
				print(
					f"{configs.COLORS[0]}{tabulate(configs.CHAT_RAID, headers=[configs.CATEGORIES[1]], tablefmt='pipe')}"
				)
				select = int(input("[Select]::: "))
				if select == 1:
					self.spam_chat_with_messages(chat_id)
				elif select == 2:
					self.spam_chat_with_join_leave(chat_id)
				elif select == 3:
					self.invite_online_users_to_chat(chat_id)
				elif select == 0:
					break
			except Exception as e:
				print(e)

	def spam_chat_with_messages(self, chat_id: str):
		message = input("[Message]::: ")
		message_type = int(input("[Message type]::: "))
		while True:
			print("[Spamming!]")
			with ThreadPoolExecutor(max_workers=100) as executor:
				[executor.submit(self.sub_client.send_message,
					chat_id,
					message,
					message_type) for _ in range(100_000_000)]

	def join_and_leave(self, chat_id: str):
		try:
			self.sub_client.leave_chat(chatId=chat_id)
			self.sub_client.join_chat(chatId=chat_id)
		except:
			return

	def spam_chat_with_join_leave(self, chat_id: str):
		while True:
			print("[Spamming with join and leave!]")
			with ThreadPoolExecutor(max_workers=100) as executor:
				[executor.submit(
					self.join_and_leave, chat_id) for _ in range(100_000_000)]

			# -- CHAT RAID --
		
		
			# -- COMMENT RAID -- 


class CommentRaid:
	def __init__(self, client: amino.Client, sub_client: amino.SubClient):
		self.client = client
		self.sub_client = sub_client
	
	
	def start(self):
		while True:
			try:
				print(
					f"{configs.COLORS[0]}{tabulate(configs.COMMENT_RAID, headers=[configs.CATEGORIES[2]], tablefmt='plain')}"
				)
				select = int(input("[Select]::: "))
				if select == 1:
					self.spam_wall_with_comments()
				elif select == 2:
					self.spam_wiki_with_comments()
				elif select == 3:
					self.spam_blog_with_comments()
				elif select == 0:
					break
			except Exception as e:
				print(e)


	def spam_wall_with_comments(self):
		user_id = self.client.get_from_code(input("[User link]::: ")).objectId
		message = input("[Message]::: ")
		for i in range(int(input("[Comments count]::: "))):
			self.sub_client.comment(message=message, userId=user_id)
			print(f"[{i+1}][Comment is sent]...")
	
	
	def spam_wiki_with_comments(self):
		wiki_id = self.client.get_from_code(input("[Wiki link]::: ")).objectId
		message = input("[Message]::: ")
		for i in range(int(input("[Comments count]::: "))):
			self.sub_client.comment(message=message, wikiId=wiki_id)
			print(f"[{i+1}][Comment is sent]...")


	def spam_blog_with_comments(self):
		blog_id = self.client.get_from_code(input("[Blog link]::: ")).objectId
		message = input("[Message]::: ")
		for i in range(int(input("[Comments count]::: "))):
			self.sub_client.comment(message=message, blogId=blog_id)
			print(f"[{i+1}][Comment is sent]...")
