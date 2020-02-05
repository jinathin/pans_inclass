#%% 
import requests
import json


URL=['https://movie.thepan.cn/', 'https://movie.thepan.cn/details.php?id=1']
max_user_index = 0

#%%
for i in URL:
    r = requests.get(i)
    data = json.loads(r.text)
    current_user = data['']['user']['edge_followed_by']['count']
    max_user = max(max_user ,current_user)
    print(max_user)

#%%
print(r)
