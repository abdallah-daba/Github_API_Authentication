import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

token = os.getenv("GITHUB_TOKEN")

username = "abdallah-daba"
url = f"https://api.github.com/users/{username}/repos"

headers ={
     "Authorization": f"token {token}"
     }

response = requests.get (url,headers = headers)

if response.status_code == 200 :
    data = response.json()


    clean_data = []
    for repo in data:
        clean_data.append ({
            "name" : repo ["name"],
            "stars" : repo ["stargazers_count"],
            "language" : repo ["language"]
        })


    with open ("repos.json", "w", encoding = "utf-8") as f :

        json.dump(clean_data, f , indent=4)

        print ("Data exported successfully to repos.json")
        
else :
    print ( "Failed to export data, try handling your error! ", 
           response.status_code), " is your status code" )


