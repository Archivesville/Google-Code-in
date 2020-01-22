import requests

def check(url,username,suffix):
     return requests.get(url+username+suffix).status_code==200


user_name=input("Enter your username : ")
site={
    'Github':{'url':'https://github.com/','check':check},
    'Facebook':{'url':'https://www.facebook.com/','check':check},
    'Instagram ':{'url':'https://www.instagram.com/','check':check},
    'Twitter':{'url':'https://twitter.com/','check':check}
 }
found=False
for i in site:
       if site[i]['check'](site[i]['url'],user_name,""):
           found=True
           print("\033[0;32m"+"[+]User Present in "+i+"\033[0m")
           print("    "+site[i]['url']+user_name)
if not found:
     print("\033[0;31m[-]User not found\033[0m")