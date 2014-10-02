from pyslet.odata2.client import Client
from downloader.models import *
c = Client("http://oda.ft.dk/api/")
aktorfeed = c.feeds[u'Akt\xf8r'].OpenCollection()   


for k, p in aktorfeed.iteritems():
    aktorid=p['id'].value
    typeid=p['typeid'].value
    gruppenavnkort=p['gruppenavnkort'].value
    navn=p['navn'].value
    fornavn=p['fornavn'].value
    efternavn=p['efternavn'].value
    biografi= p['biografi'].value
    if (p['opdateringsdato']== None):
        opdateringsdato=None
    else:
        opdateringsdato=p['opdateringsdato'].value.GetCalendarString()
    
    periodeid=p['periodeid'].value
    if (p['startdato']== None):
        startdato=None
    else:
        startdato=p['startdato'].value.GetCalendarString()
        
    if (p['slutdato']== None):
        slutdato=None
    else:
        slutdato=p['slutdato'].value.GetCalendarString()
        
    print aktorid,  typeid, gruppenavnkort,  navn,  fornavn,  efternavn,  opdateringsdato,  periodeid,  slutdato,  startdato
    aktor.objects.create(aktorid=aktorid,  typeid= typeid, gruppenavnkort=gruppenavnkort,  navn=navn,  fornavn=fornavn,  efternavn=efternavn, biografi=biografi, opdateringsdato=opdateringsdato,  periodeid=periodeid,  slutdato=slutdato,  startdato=startdato)



# u'Akt\xf8rAkt\xf8r'

aktoraktorfeed = c.feeds[u'Akt\xf8rAkt\xf8r'].OpenCollection()   

for k, p in aktoraktorfeed.iteritems():
    aktoraktorid=p['id'].value
    fraaktorid=p[u'fraakt\u00f8rid'].value
    tilaktorid=p[u'tilakt\u00f8rid'].value
    rolleid=p['rolleid'].value
    if (p['startdato']== None):
        startdato=None
    else:
        startdato=p['startdato'].value.GetCalendarString()
        
    if (p['slutdato']== None):
        slutdato=None
    else:
        slutdato=p['slutdato'].value.GetCalendarString()
        
    print aktoraktorid, fraaktorid, tilaktorid,  rolleid,  slutdato,  startdato
    aktoraktor.objects.create(aktoraktorid=aktoraktorid,  fraaktorid=fraaktorid, tilaktorid=tilaktorid,   slutdato=slutdato,  startdato=startdato, rolleid=rolleid, )
    
    
    aktorlist = []

    
    for b in aktoraktor.objects.all():
    if (b.tilaktorid == 1):
        aktorlist.append(b.fraaktorid)

    
    for f in aktorlist:
    for q in aktor.objects.all():
        if (f == q.aktorid):
            print q.navn

    
    
    uhh = aktor.objects.filter(aktorid__in=aktorlist)


for nodes in aktor.objects.filter(aktorid=1):
    G.add_node(nodes.aktorid, navn= nodes.navn)

listofnodes = G.nodes()

for t in aktoraktor.objects.all():
    if (t.fraaktorid in listofnodes):
        print t.fraaktorid,  t.tilaktorid
        fromnode = aktor.objects.filter(aktorid=t.fraaktorid)
        tonode = aktor.objects.filter(aktorid=t.tilaktorid)
        G.add_node(fromnode[0].aktorid, navn=fromnode[0].navn)
        G.add_node(tonode[0].aktorid, navn=tonode[0].navn)
        G.add_edge(t.fraaktorid,t.tilaktorid)

import matplotlib.pyplot as plt

labels=dict((n,d['navn']) for n,d in G.nodes(data=True))

 nx.draw(G)

 nx.draw_networkx_labels(G,pos,labels,font_size=8)
  pos=nx.spring_layout(G)

plt.axis('off')

plt.savefig("labels_and_colors.png")
