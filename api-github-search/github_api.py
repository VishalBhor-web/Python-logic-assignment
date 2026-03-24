import requests


params={
    "q": "python",
    "sort":"stars",
    "order":"desc",
    "per_page":5
}
response=requests.get("https://api.github.com/search/repositories",params=params)

data=response.json()
if response.status_code==200:
    item=data["items"]

    for repo in item:
        print("Name: ",repo["name"])
        print("Stars: ",repo["stargazers_count"])
        print("-"*10)
