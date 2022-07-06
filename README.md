<img src="https://cdn.discordapp.com/attachments/453287916584566808/994250135909437490/CoverImage.jpg">  

An open-source discord bot to help you to never forget WYSI 727

### What does this bot do?
It prints a WYSI 727 message at 7:27 AM and PM (depending on sys time)


# How do I run this?
First, clone the repository
```
git clone https://github.com/AlooTheAloo/WYSI-Bot
```
Make sure you have python installed  
If you don't have it installed, follow the directions and install it from the microsoft store (if you are on windows).
```
python
```
Next, install the discord library from pip
```
pip install discord
```
Create an application + bot in the discord developper portal  
https://discord.com/developers/applications  
Generate a token by pressing 'Reset token' in the 'Bot' section  
<img src="https://cdn.discordapp.com/attachments/453287916584566808/982374973417091173/unknown.png">  
Then, paste it in the token.txt file  

Next, you'll want to invite the bot to your server.  
You can do this by copying the application ID of your bot and pasting it inside this link  
(where it says client_id=ID_HERE, replace ID_HERE with your ID)  
https://discordapp.com/oauth2/authorize?client_id=ID_HERE&scope=bot&permissions=0

Finally, run the project using python
```
python wysi.py
```

If you see a timestamp showing every couple of seconds, the code is working correctly!
