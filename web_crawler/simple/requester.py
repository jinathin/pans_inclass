# %% Load Library
import requests
<<<<<<< HEAD

user = "espn"
URL = 'https://www.dcinside.com/' + user


# %% Send out the request 
r = requests.get(URL)

# %% Checkout the Results

print(r)


# %%
print(r.request.headers)
print(r.headers)

# %% to see all the text like index.html
print(r.text)


# %%
print(r.status_code
)


# %%
start = "edge_followed_by":{"count": end = }
=======
import json
URL = 'https://movie.thepan.cn/'
InstgrameURL = 'https://www.instagram.com/fanshawecollege/?__a=1'

# %% Send out the request
r = requests.get(InstgrameURL)

# %% Checkout the Results
print(r)

# %%
print(r.request.headers)
print(r.headers)
# %%
print(r.text)

# %%
print(r.status_code)


# %%
data = json.loads(r.text)

print(data["graphql"]['user']['edge_followed_by']['count'])


# %%

import requests

>>>>>>> ed9496ec1e9ce0fefed0130b68d501b860798112
