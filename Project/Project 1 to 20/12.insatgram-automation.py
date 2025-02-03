from instabot import Bot

bot = Bot()
usernameinput = input("Enter username:")
passwordinput = input("Enter password:")
bot.login(username=usernameinput, password=passwordinput)
# bot.follow("dangiabhi332")
followers = bot.get_user_followers(usernameinput)
for follower in followers:
    print(follower.username)
    bot.follow(follower.username)
