# %% Load library
import json
from requests_html import HTMLSession


# %% Request
URL = 'https://movie.thepan.cn/details.php?id='
session = HTMLSession()
titles = []
stories = []

# %%
for i in range(1, 21):
    site_url = URL + str(i)
    r = session.get(site_url)
    titles.append(r.html.find('h2')[1].text)
    stories.append(r.html.find('p')[1].text)

# %%
output_file = 'details.json'
movies = dict(zip(titles, stories))

with open(output_file, 'w') as output_handler:
    json.dump(movies, output_handler, indent=4)


# %%


# %%
