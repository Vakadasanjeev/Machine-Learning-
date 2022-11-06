
# coding: utf-8

# In[1]:

def sqrDist(p1,p2):
    return round(((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2),4)


# In[2]:

def printres(centroids,ptc_map):
    for i in range(len(centroids)):
        print("centroid",i,centroids[i])
    for j in ptc_map:
        print("point",j,"centroid:",ptc_map[i])


# In[3]:

def kmeansclustering(centroids,datapoints):
    d_frm_cluster=DistfrmPoint(centroids,datapoints)
    point_to_cluster_mapping={}
    max_cluster=0
    for i in range(len(datapoints)):
        point_to_cluster_mapping[i]= None
        for j in range(len(d_frm_cluster)):
            if d_frm_cluster[j][i]<d_frm_cluster[max_cluster][i]:
                max_cluster=j
        point_to_cluster_mapping[i]=max_cluster
    cluster_count=0    
    for i in range(len(centroids)):
        for j in point_to_cluster_mapping:
            if  point_to_cluster_mapping[j]==i:
                centroids[i][0]+=datapoints[j][0]
                centroids[i][1]+=datapoints[j][1]
                cluster_count+=1
        if cluster_count!=0:
            centroids[i][0]=round(centroids[i][0]/cluster_count,4)
            centroids[i][1]=round(centroids[i][1]/cluster_count,4)
            cluster_count=0
            
    printres(centroids,point_to_cluster_mapping)
    return centroids


# In[4]:

def kmeansi(centroids,datapoints):
    old_centroids=centroids
    new_centroids=centroids
    i=0
    
    while i<=15:
        i+=1
        print("\niteration:{:d}".format(i))
        old_centroids=new_centroids
        new_centroids=kmeansclustering(new_centroids,datapoints)


# In[5]:

def DistfrmPoint(centroids,datapoints):
    dist_f_clust=[]
    ir=[]
    for i in centroids:
        for j in datapoints:
            ir.append(sqrDist(i,j))
        dist_f_clust.append(ir)
        ir=[]
    return dist_f_clust


# In[6]:

centroids=[[2,10],[5,8],[1,2]]
datapoints=[[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,2],[4,9]]
kmeansi(centroids,datapoints)


# In[ ]:



