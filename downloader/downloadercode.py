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
    
    
#class aktoraktorrolle(models.Model):
#    
#    id = models.AutoField(primary_key=True)
#    aktoraktorrolleid = models.IntegerField(null=True, blank=True)
#    rolle = models.CharField(max_length=200, null=True, blank=True)
#    opdateringsdato = models.DateTimeField(null=True, blank=True)


# u'Akt\xf8rAkt\xf8rRolle'

aktoraktorrollefeed = c.feeds[u'Akt\xf8rAkt\xf8rRolle'].OpenCollection()   

for k, p in aktoraktorrollefeed.iteritems():
    aktoraktorrolleid=p['id'].value
    rolle=p['rolle'].value
    if (p['opdateringsdato']== None):
        opdateringsdato=None
    else:
        opdateringsdato=p['opdateringsdato'].value.GetCalendarString()
        
    print k,  aktoraktorrolleid,  rolle,  opdateringsdato
    aktoraktorrolle.objects.create(aktoraktorrolleid=aktoraktorrolleid,  rolle=rolle,  opdateringsdato=opdateringsdato)



#class aktortype(models.Model):
#    
#    id = models.AutoField(primary_key=True)
#    aktortypeid = models.IntegerField(primary_key=True)
#    type = models.CharField(max_length=200, null=True, blank=True)
#    opdateringsdato = models.DateTimeField(null=True, blank=True)

    
aktortypefeed = c.feeds[u'Akt\xf8rtype'].OpenCollection()   

for k, p in aktortypefeed.iteritems():
    aktortypeid=p['id'].value
    type=p['type'].value
    if (p['opdateringsdato']== None):
        opdateringsdato=None
    else:
        opdateringsdato=p['opdateringsdato'].value.GetCalendarString()
        
    print k,  aktortypeid,  type,  opdateringsdato
    aktortype.objects.create(aktortypeid=aktortypeid,  type=type,  opdateringsdato=opdateringsdato)
    



# Graph Creation and Plotting
    import networkx as nx
    G=nx.Graph()
    aktorlist = []

    
    for b in aktoraktor.objects.all():
        if (b.tilaktorid == 1):
            aktorlist.append(b.fraaktorid)

    
    for f in aktorlist:
        for q in aktor.objects.all():
            if (f == q.aktorid):
                print q.navn
                
uhh = aktor.objects.filter(aktorid__in=aktorlist)

for nodes in aktoraktor.objects.filter(aktorid=1):
    G.add_node(nodes.aktorid, navn= nodes.navn)


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



nx.draw(G)
pos=nx.spring_layout(G)
labels=dict((n,d['navn']) for n,d in G.nodes(data=True))
nx.draw_networkx_labels(G,pos,labels,font_size=6)
plt.axis('off')

plt.savefig("MPsandCommittees.png")


#Find all MPs (rolleid = 15) and make edges to Folketinget

#MPconnections = aktoraktor.objects.filter(rolleid=15)

#MPconndict = dict((d.fraaktorid,d.tilaktorid) for  d in MPconnections.all() )


commitees =  aktor.objects.filter(typeid=3)
MPs = 

for t in aktoraktor.objects.filter(rolleid=15,  slutdato=None):
     fromnode = aktor.objects.filter(aktorid=t.fraaktorid)[0]
     tonode = aktor.objects.filter(aktorid=t.tilaktorid)[0]
     if (fromnode.typeid == 11 and fromnode.periodeid==32)  and (tonode.typeid == 5)  :
            G.add_node(fromnode.aktorid, navn=fromnode.navn)
            G.add_node(tonode.aktorid, navn=tonode.navn)
            G.add_edge(fromnode.aktorid,tonode.aktorid)
            

                        for roller in aktoraktor.objects.filter(tilaktorid=tonode.aktorid):
                if (roller.rolleid == 15):
             
      
plt.clf()      
plt.figure(figsize=(40, 40))
labels=dict((n,d['navn']) for n,d in G2.nodes(data=True))                    
nx.draw_shell(G2, with_labels=True, labels=labels, alpha=0.6, edge_color='g', style='dotted')

plt.axis('off')

plt.savefig("limited.png")



pos=nx.spring_layout(G)
labels=dict((n,d['navn']) for n,d in G.nodes(data=True))
nx.draw_networkx_labels(G,pos,labels,font_size=6)



# 

from sets import  Set
G=nx.DiGraph()

MPs = []
MPids = []
coms = []
comsid = []
for t in aktoraktor.objects.filter(rolleid=15,  slutdato=None):
    fromnode = aktor.objects.filter(aktorid=t.fraaktorid)[0]
    tonode = aktor.objects.filter(aktorid=t.tilaktorid)[0]
    if (fromnode.typeid == 3 and fromnode.periodeid==32)  and (tonode.typeid == 5)  :
        coms.append(fromnode)
        comsid.append(fromnode.aktorid)
    
    
        tilaktorid__in=MPids
        
for t in aktoraktor.objects.filter(rolleid=15,  slutdato=None):
    fromnode = aktor.objects.filter(aktorid=t.fraaktorid)[0]
    tonode = aktor.objects.filter(aktorid=t.tilaktorid)[0]
    if (fromnode.typeid == 11 and fromnode.periodeid==32)  and (tonode.typeid == 5):
        MPs.append(tonode)
        MPids.append(tonode.aktorid)
        print tonode.navn
    
for t in aktoraktor.objects.filter(tilaktorid__in=MPids, fraaktorid__in=comsid,   slutdato=None):
    fromnode = aktor.objects.filter(aktorid=t.fraaktorid)[0]
    tonode = aktor.objects.filter(aktorid=t.tilaktorid)[0]
    G.add_node(fromnode.aktorid, navn=fromnode.navn)
    G.add_node(tonode.aktorid, navn=tonode.navn)
    G.add_edge(fromnode.aktorid,tonode.aktorid)

for t in aktoraktor.objects.filter(,  rolleid=):
    
    

from networkx.algorithms.traversal.depth_first_search import dfs_tree

names = []
for o in coms:
    names.append((o.aktorid, o.navn))

na=dict((n,d) for n,d in names)      

for p in comsid:
    H= dfs_tree(G,p)
    I=G.subgraph(H.nodes())
    plt.clf()      
    plt.figure(figsize=(10, 10))
    labels=dict((n,d['navn']) for n,d in I.nodes(data=True))                    
    nx.draw_spring(I, with_labels=True, labels=labels, alpha=0.6, edge_color='g', style='dotted')
    plt.axis('off')
    plt.savefig("Udvalg-" + na[p] + "-" + str(p) + ".png")


#concentric circles
names = []
for o in coms:
    names.append((o.aktorid, o.navn))

na=dict((n,d) for n,d in names)      

nlist = []
for p in comsid:
    nlist.append(dfs_tree(G,p).nodes())
    
    

plt.clf()      
plt.figure(figsize=(40, 40))
labels=dict((n,d['navn']) for n,d in G.nodes(data=True))                    
nx.draw_shell(G, with_labels=True, labels=labels, alpha=0.6, edge_color='g', style='dotted', nlist=nlist)

plt.axis('off')

plt.savefig("concentri.png")
    


def remove_edges(g, in_degree=1, out_degree=1):
    g2=g.copy()
    d_in=g2.in_degree(g2)
    d_out=g2.out_degree(g2)
    print(d_in)
    print(d_out)
    for n in g2.nodes():
        if d_in[n]==in_degree and d_out[n] == out_degree: 
            g2.remove_node(n)
    return g2


def remove_edges2(g, in_degree=1, out_degree=1):
    g2=g.copy()
    d_in=g2.in_degree(g2)
    d_out=g2.out_degree(g2)
    print(d_in)
    print(d_out)
    for n in g2.nodes():
        if d_in[n]<=in_degree and d_out[n] <= out_degree: 
            g2.remove_node(n)
    return g2

plt.clf()      
plt.figure(figsize=(40, 40))
labels=dict((n,d['navn']) for n,d in G2.nodes(data=True))                    
nx.draw_shell(G2, with_labels=True, labels=labels, alpha=0.6, edge_color='g', style='dotted')

plt.axis('off')

plt.savefig("limited.png")


for node in G.nodes():
    temp = r'{"name": "' + G.node[node]['navn'] + r'"' + r',"size":1, "imports":['
    for edge in G.edge[node]:
        temp = temp + r'"' + G.node[edge]['navn'] + r'",'
    temp = temp + r']},'
    d3strlist.append(temp)


