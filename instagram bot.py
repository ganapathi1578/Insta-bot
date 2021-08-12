
def instagram():
	from instabot import Bot
	bot=Bot()
	print("[1] FOLLOW \n[2] UNFOLLOW \n[3] FOLLOW BY FOLLOWER \n[4] MESSAGE \n[5] MESSAGE BY FOLLOWER")
	order=input("\nSELECT ONE FROM ABOVE \n")
	#login
	user_name = input("Enter your user name :")
	pass_word = input("Enter your password :")
	bot.login(username=user_name,password=pass_word)
	print("Login succesfull as",user_name)
	
	# Setting Target
	target = input("Enter Target  instagram id :")
	
	# Getting Target followers
	followers=bot.get_user_followers(target)
	
	#follow ,argument =1
	if order==1:
		bot.follow(target)
		print("you followed",target)
		
	# Unfollow ,argument=2
	if order==2:
		bot.unfollow(target)
		print("you unfollowed",target)
	
	# follow by follower ,argument=3
	if order==3:
		for follower in followers :
			bot.follow(follower)
			print("you followed :",follower)
	
	#dm my followers ,argument=5
	if order==4:
		msg=input("Enter a message:")
		bot.send_message(msg,user_name)
	
	#dm followers by person ,argument=6
	if order==5:
		msg=input("Enter message :")
		for follower in followers :
			bot.send_message(msg,target)
			
			
instagram()