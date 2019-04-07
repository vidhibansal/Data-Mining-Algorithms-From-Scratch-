import math
file_input = open("input.txt","r")
k = int(file_input.readline().strip())
tran=[]

while True:
    line = file_input.readline().strip()
    if not line:
        break
    l=line.split(",")
    tran.append(l)

print (tran)

def dist(p1,p2):
    res=0
    for i in range(len(p1)):
        res += math.pow(float(p1[i])-float(p2[i]),2)

    final_res = math.sqrt(res)
    return final_res

def clusters(data,centroids):
    l1= dict() #for maintaining the distance corresponding to each cluster
    l2=dict()  #for storing the points in corresponding cluster 
    for i in range(len(centroids)):
        l2[i]=[] #value is going to be a list
    for i in range(len(data)):
        p1 = data[i] #take one point at a time
        for index in range(len(centroids)):  #compute the distance of that one point with all the clusters 
            p2= centroids[index] 
            d = dist(p1,p2)
            #print(d)
            l1[index]=d
            
        res = min(l1.values())
        #print("min",res)
        for key,value in l1.items():
            if value == res:
                kk = key
        l2[kk].append(i)
    print(l2)
    return (l2)

def mean(l2,tran):
    centroids=[]
    tmp=[]
    for key,values in l2.items():
        l=values
        x1=0
        for j in range(len(tran[0])):
            x1=0
            for k in range(len(l)):
                p=tran[l[k]]
                x1 +=int(p[j])
            x1=x1/len(l)
            tmp.append(x1)
        centroids.append(tmp)
        tmp=[]
    print("New Centroids:",centroids)
    return (centroids)
        
            

centroids = tran[0:k]
print(centroids)
old = centroids
new = None
while True:
    old = centroids
    l2=clusters(tran,centroids)
    centroids = mean(l2,tran)
    new = centroids
    if (new == old):
        break
    

    
