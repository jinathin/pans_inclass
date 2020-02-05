# %% Load Library
import requests

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
start = '"edge_followed_by":{"count":'end'
 end = }'