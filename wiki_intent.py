import requests
from collections import OrderedDict

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
#r.status_code
#r.headers['content-type']
#r.encoding
#r.text
#r.json()

title ="Berlin"
url = "https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles={}&rvslots=*&format=json&rvlimit=50".format(title)
result = requests.get(url).json()

print(result)

revisions_ids = []
for page_id in result["query"]["pages"]:
    for revision in result["query"]["pages"][page_id]["revisions"]:
        revisions_ids.append(str(revision["revid"]))

print(revisions_ids)

ores_url = "https://ores.wikimedia.org/v3/scores/enwiki/?revids={0}&models=goodfaith".format("|".join(revisions_ids))

print(ores_url)
scores={}

ores_results = requests.get(ores_url).json()

for revision in ores_results["enwiki"]["scores"]:
    prob = ores_results ["enwiki"]["scores"][revision]["goodfaith"]["score"]["probability"]["true"]
    #print(revision, prob)
    scores[revision] = prob

    
ordered_scores = OrderedDict(
    sorted(scores.items(), key=lambda t: t[1]))

for case in ordered_scores:
    print(case, ordered_scores[case])
    break

#Special:Diff/111269104



