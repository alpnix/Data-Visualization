import requests
from plotly.graph_objs import Bar
from plotly import offline
import json

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Content-Type": "application/json"}

r = requests.get(url)
print(f"Status: {r.status_code}")
response_dict = r.json()

# with open("repos.json","r") as f:
    # response_dict = json.load(f)

print(f"Repository Count: {response_dict['total_count']}")

repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")

first_repo = repo_dicts[0]
print(f"\nKeys: {len(first_repo)}")

for key, value in first_repo.items():
    print(f"Key: {key}, Value: {value}")


stars, names, labels, repo_links = [], [], [], []
for repo_dict in repo_dicts:
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    label = f"{owner}<br>{description}"
    repo_url = repo_dict["html_url"]
    repo_name = repo_dict["name"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    labels.append(label)
    stars.append(repo_dict["stargazers_count"])
    names.append(repo_dict["name"])

data = [{
    "type": "bar",
    "x": repo_links,
    "y": stars,
    "hovertext": labels,
    "hoverinfo": "text",
    "marker": {
        "color": "rgb(60,100,150)",
        "line": {
            "width": 4.5,
            "color": "rgb(25,25,25)",
        }
    },
    "opacity": 0.6,
}]

my_layout = {
    "title": "Most Starred JavaScript Projects on Github",
    "titlefont": {"size": 28},
    "xaxis": {
        "title": "Repository",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
    "yaxis": {
        "title": "Star Count",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
}

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="python_repos.html")