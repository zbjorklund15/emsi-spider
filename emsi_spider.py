import requests
import json


url = "https://api.lever.co/v0/postings/economicmodeling?group=team&mode=json"
if "economicmodeling" in url:
    company = "Emsi"
response = requests.get(url)
jobs = response.json()
data = {}
data["jobs"] = []

for title in jobs:
    if(title["title"] == "Talent Network"):
        break
    for post in title["postings"]:
        data["jobs"].append({
            "job-title" : post["text"],
            "company" : company,
            "tags" : post["categories"],
            "description" : post["descriptionPlain"],
            "url" : post["applyUrl"],
            "id" : post["id"],
        })

with open("jobs.json", "w") as outfile:
    json.dump(data, outfile)