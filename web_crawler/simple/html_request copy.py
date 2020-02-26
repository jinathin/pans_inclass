# %% Load library
from requests_html import HTMLSession

# %% Build the session this way
session = HTMLSession()

# %% Request
URL = 'https://bbs.ruliweb.com/'
r = session.get(URL)
print(r)

# %%
print(r.html.links)
print(r.html.absolute_links)

# %%
gnb_menu_list = r.html.find('#gnb_menu_list', first=True)
print(gnb_menu_list.html)
print(gnb_menu_list.text)
a
# %%
import json
output_file = 'menu.json'
menu = dict(zip(gnb_menu_list))

with open(output_file,'w') as output_handler:
    json.dump(menu,output_handler, indent=4)


# %%
