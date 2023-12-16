#Paradoxe de Braess
import random as rd
import matplotlib.pyplot as plt
import numpy as np


def creamat(n):
    M=[]
    
    
    for i in range(n):
        A=[]

        for j in range(n):
            A.append([0,[0,0]])
        M.append(A)

    return M



L=[[ [0,[0,0]],  [2, [1,80]], [1,[81,100]], [0,[0,0]]    ],
   [ [0,[0,0]],  [0, [0,0] ], [0, [1,95] ], [1,[96,100]] ],
   [ [0,[0,0]],  [0, [1,10] ], [0, [0,0]  ], [2,[11,100]] ], 
   [ [0,[0,0]],  [0, [0,0] ],  [0, [0,0]],   [0, [0,0]]  ] ] # [type de la route (qui donne le temps de parcours),prob]

L2=[[ [0,[0,0]],  [2, [1,50]], [1,[51,100]], [0,[0,0]]    ],
   [ [0,[0,0]],  [0, [0,0] ], [0, [0,0] ], [1,[1,100]] ],
   [ [0,[0,0]],  [0, [0,0] ], [0, [0,0]  ], [2,[1,100]] ], 
   [ [0,[0,0]],  [0, [0,0] ],  [0, [0,0]],   [0, [0,0]]  ] ]

def routes(M):
    routes=[]
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j][1]!=[0,0]:
                routes.append([(i,j),0])
    
    return routes





def voitures(n):
    voitures=[['a'*i,(0,0),0] for i in range(n)] # nom, route ,temps
    return voitures

def temps_route(n,i):
    if i==0:
        return 0
    if i==1 :
        T=15
        return T
    if i==2:
        a=20
        b=7
        T=n/a+b
        return T
    if i==3 :
        a=15
        b=15
        return n/a+b
    if i==4 :
        a=15
        b=10
        return n/a+b
    if i==10:
        v=80#vitesse limite
        d=2#longueur de la route
        c=10000#capacité de la route
        u=0.2#valeurs empiriques
        e=0.5
    
        T=d/v*(1+u*(n/c)**e)
    
        return T

def obstacle(i,n):
    
    a=120    
    if i==0: #pas d'obstacle
        return 0
    
    if i ==1 : #obstacle style dos d'âne
        return 1
    if i == 2 : # obstacle style camion sur le bord,travaux
        
        return np.exp(n/a)


def intégrer_obst(M,route,i):
    M[route[0]][route[1]].append(i)
    

def para(n,M,v=[],route=[]):
    if v == []:
        v=voitures(n)
    if route==[]:
        route=routes(M)
    
    
    nf=0
    for i in v:
        if i[1][1]==len(M)-1:
            nf+=1
            
    if nf==n:
        return v
    print(nf,n)


    
    for i in v:
        
        r=rd.randint(1,100)
        if i[1][1]!=len(M)-1:#limiter le nombre de boucles
            for j in range(len(M[i[1][1]])) :
                
                if M[i[1][1]][j][1][0] <= r <= M[i[1][1]][j][1][1]:
                    
                    
                    for k in route:
                        
                        if k[0]==i[1]:
                            k[1]-=1
                        if k[0]==(i[1][1],j):
                            
                            k[1]+=1
                            i[2]+= temps_route( k[1], M[i[1][1]][j][0])
                            g=k[0]
                        if len(M[i[1][1]][j])==3:
                            i[2]+= obstacle(M[i[1][1]][j][2],k[1])
                        
            
            i[1]=g
    
                        
    
    f=para(n,M,v,route)
    return f



def temps_moy(n,M):
    f=para(n,M)
    t=0
    for i in f:
       t+=i[2]
    return t/len(f)
    
def graphes(pas,n,M,M2):
    Y=[]
    X=[]
    Y2=[]
    C=[]
    for i in range(1,n,pas):
        t=temps_moy(i,M)
        X.append(i)
        Y.append(t)
        t2=temps_moy(i,M2)
        Y2.append(t2)
        
        if abs(t-t2)<=0.2:
            C.append(i)
        
    plt.plot(X,Y,label='mode 1')
    plt.plot(X,Y2,'g',label='mode 2')
    plt.legend()
    plt.xlabel("nombre de voitures")
    plt.ylabel("temps moyen")
    print("pas,n :",pas,n)
    return C