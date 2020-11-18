import os
green="\033[0;32m"
white="\033[0;37m"
os.system("clear")
print(" ▒█░░▒█░▒███░░▒█▒█░░▒█▒█░▒█░░▒█▒█████")
print(" ▒█░░▒█▒█░░▒█▒█▒█▒█▒█▒█▒█▒██░▒█░░▒█░░")
print(" ▒█████▒█████▒█░░▒█▒█░░▒█▒█▒█▒█░░▒█░░")
print(" ▒█░░▒█▒█░░▒█▒█░░▒█▒█░░▒█▒█░▒██░░▒█░░")
print(" ▒█░░▒█▒█░░▒█▒█░░▒█▒█░░▒█▒█░░▒█░░▒█░░")

print("┌────────────────────────────────────┐")
print("│Author :  HAMM-WISS                       │")
print("│Github :  https://github.com/HAMM-WISS    │")
print("└────────────────────────────────────┘")

import amino

client=amino.Client()

uurl=input(green+"WIKI URL :  "+white)
uourl=client.get_from_code(uurl)
wikiId=uourl.objectId
comId=uourl.path[1:uourl.path.index('/')]
print(green+"------------------------------------------------"+white)
comment=input(green+"ENTER YOUR COMMENT :  "+white)
print(green+"------------------------------------------------"+white)
email=input("ENTER YOUR EMAIL :  ")
password=input("ENTER YOUR PASSWORD :  ")
print(green+"------------------------------------------------"+white)
client.login(email=email,password=password)
subclient=amino.SubClient(comId=comId,profile=client.profile)
os.system("clear")
f=True
while f==True:
	try:
		subclient.comment(message=comment,wikiId=wikiId)
		print(green + "commenting " + comment + "...|Makyron:)"+ white)
		
	except:
		pass

