COLORS = [
	"\033[38;5;196m", # RED
	"\033[38;5;45m", # LIGHT_BLUE
	"\033[38;5;73m" # DARK BLUE
]

CATEGORIES = [
	"Main Menu",
	"Chat Raid",
	"Comment Raid",
	"Message Types",
	"Login Menu"
]

MAIN_MENU = [
	[1, f"{COLORS[0]}Chat Raid"],
	[2, f"{COLORS[1]}Comment Raid"],
	[3, f"{COLORS[2]}Message Types"]
]

LOGO = """                                                        
 #  ### # # ### ### # # # # # # ###  ## ##   #   #  ##
##    # ###  #  # # # # ### # #   # #   # # # # ##  # # 
 #   ## ###  #  # #  #  ### ###  #   #  ##  ###  #  # # 
 #    # # #  #  # # # # # #   # #     # # # # #  #  # # 
### ### # # ### # # # # # #   # ### ##  # # # # ### ##
[Author]::: zeviel
[GitHub]::: https://github.com/zeviel
"""

CHAT_RAID = [
	[1, f"{COLORS[0]}Spam chat with messages"],
	[2, f"{COLORS[1]}Spam chat with join and leave"],
	[3, f"{COLORS[0]}Invite users to chat"]
]

COMMENT_RAID = [
	[1, f"{COLORS[0]}Spam user wall with comments"],
	[2, f"{COLORS[1]}Spam wiki with comments"],
	[3, f"{COLORS[0]}Spam blog with comments"]
]

MESSAGE_TYPES = [
	[50, "USER_SHARE_EXTURL"],
	[51, "USER_SHARE_OBJECT"],
	[56, "USER_VIDEO_CALL_CANCELLED"],
	[57, "USER_VIDEO_CALL_DECLINED"],
	[58, "USER_AVATAE_CALL_NO_ANSWERED"],
	[59, "USER_AVATAR_CALL_CANCELLED"],
	[60, "USER_AVATAR_CALL_DECLINED"],
	[103, "INFO_SESSION_INIT"],
	[107, "INFO_START_AUDIO_CHAT"],
	[108, "INFO_START_VIDEO_CHAT"],
	[109, "INFO_START_AVATAR_CHAT"],
	[111, "INFO_END_VIDEO_CHAT"],
	[112, "INFO_END_AVATAR_CHAT"],
	[114, "INFO_START_SCREENING_ROOM"]
]

LOGIN_MENU = [
	[1, "Login with email & password"],
	[2, "Login with sid"]
]
