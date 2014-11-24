
# coding: utf-8

# In[163]:

from __future__ import print_function

from collections import Counter
import networkx as nx
import requests
import pandas as pd
import time
import matplotlib.pyplot as plt


# In[10]:

# Aktørtype
url = "http://oda.ft.dk/api/Akt%C3%B8rtype?$inlinecount=allpages"
aktortype = pd.DataFrame(requests.get(url).json()['value'])


# In[11]:

aktortype


# In[13]:

url = 'http://oda.ft.dk/api/Akt%C3%B8r?$inlinecount=allpages&$filter=typeid%20eq%205'
aktor_person_dict = requests.get(url).json()


# In[22]:

response = requests.get(url).json()
aktor_person_list = []
while True:
    try: 
        aktor_person_list.extend(response['value'])
        url = response['odata.nextLink']
        response = requests.get(url).json()
    except:
        break
    print(url)
    time.sleep(3)


# In[23]:

aktor_person = pd.DataFrame(aktor_person_list)


# In[24]:

aktor_person


# In[31]:

url = 'http://oda.ft.dk/api/Akt%C3%B8rAkt%C3%B8rRolle?$inlinecount=allpages'
rolle = pd.DataFrame(requests.get(url).json()['value'])


# In[28]:

rolle


# In[33]:

# Limited download of aktør-aktør table (it is quite bit) 
url = 'http://oda.ft.dk/api/Akt%C3%B8rAkt%C3%B8r?$inlinecount=allpages'
response = requests.get(url).json()
aktor_aktor_list = []
for _ in range(10):
    try: 
        aktor_aktor_list.extend(response['value'])
        url = response['odata.nextLink']
        response = requests.get(url).json()
    except:
        break
    print(url)
    time.sleep(3)


# In[34]:

aktor_aktor = pd.DataFrame(aktor_aktor_list)


# In[201]:




# In[192]:

url_base = 'http://oda.ft.dk/api/Akt%C3%B8rAkt%C3%B8r?$inlinecount=allpages&$filter=fraakt%C3%B8rid%20eq%20' 
try: 
    aktor_aktor_dict_list
except:
    aktor_aktor_dict_list = {}
    
for id in aktor_person.id:
    if id not in aktor_aktor_dict_list:
        print(id)
        response = requests.get(url_base + str(id)).json()
        aktor_aktor_dict_list[id] = []
        while True:
            try: 
                aktor_aktor_dict_list[id].extend(response['value'])
                url = response['odata.nextLink']
                response = requests.get(url).json()
            except:
                break
            print(url)
            time.sleep(3)
        break


# In[195]:

graph_actor_actor = nx.DiGraph()
for from_id, fields_list in aktor_aktor_dict_list.items():
    for fields in fields_list:
        to_id = fields[u'tilakt\xf8rid']
        graph_actor_actor.add_edge(from_id, to_id)


# In[204]:

positions = nx.layout.spectral_layout(graph_actor_actor)
positions = nx.layout.spring_layout(graph_actor_actor, pos=positions)
plt.figure(figsize=(15, 10))
nx.draw_networkx_nodes(graph_actor_actor, pos=positions, alpha=0.3, linewidths=0)
nx.draw_networkx_edges(graph_actor_actor, pos=positions, alpha=0.05)

actors_to_display = aktor_aktor_dict_list.keys()
for node in graph_actor_actor.nodes():
    if node in actors_to_display:
        position = positions[node]
        name = aktor_person.ix[aktor_person.id == node, 'navn'].values[0]
        plt.text(position[0], position[1], name, horizontalalignment='center', verticalalignment='center')

plt.axis((0., 1, 0, 1))
plt.savefig('Folketinget_aktor_aktor.png')


# In[78]:

get_ipython().magic(u'matplotlib inline')


# In[200]:




# In[199]:




# In[196]:




# In[196]:




# In[ ]:



