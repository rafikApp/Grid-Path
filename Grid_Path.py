# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: RAFIK
"""






from collections import deque
from random import *
from turtle import *






# partie 1
def initialisergrille(n,m):

    l = [[[0, 0, 0, 0] for i in range(m)] for j in range(n)]
    print(l)
    for i in l:#initialiser
         for j in i:
             for k in range(len(j)):
                       j[k]=randint(1,20)

    for i in l:# affichage
        for j in i:
            print(j,end=" ")
        print()
    # egalisation des colognnes partagées entres les cases
    for i in range(n):
        for j in range(m-1,0,-1):
            l[i][j][3]=l[i][j-1][1]
    #egalisation des lignes partagées
    for i in range(n-1,0,-1):
        for j in range(m):
            l[i][j][0]=l[i-1][j][2]
    print("#"*100)
    for i in l:
        for j in i:
            print(j, end=" ")
        print()
    return l

#Partie 2


def parcoursgrille1(G):
    m,n=len(G),len(G[0])
    L=[]
    Gra=[[] for i in range(m*n)]
    for i in range(len(G)):
        for j in range(len(G[0])):
            if (i!=len(G)-1) or (j!=len(G[0])-1):
                if j == len(G[0]) - 1:
                    Gra[j+i*n].append([G[i][j][2],(i+1,j)])
                    L.append((i,j))
                elif i == len(G)-1:
                    Gra[j+i*n].append([G[i][j][1],(i,j+1)])
                    L.append((i,j))
                else:
                    Gra[j+i*n].append([G[i][j][1],(i,j+1)])
                    Gra[j+i*n].append([G[i][j][2], (i + 1, j)])    
                    L.append((i,j))
    L.append((len(G)-1,len(G[0])-1))
    return Gra,L

def chemins_glt_rec1(Gra,G,i,j,c):
    m,n=len(G),len(G[0])
    if i!=m or j != n:
        v=Gra[j+i*n]
        if len(v)>1:
            if v[0][0]>v[1][0]:
                c+=v[1][0]
                return [(i,j)]+chemins_glt_rec1(Gra,G,v[1][1][0],v[1][1][1],c)
            c+=v[0][0]
            return [(i,j)]+chemins_glt_rec1(Gra,G,v[0][1][0],v[0][1][1],c)
        elif len(v)==1:
            c+=v[0][0]
            return [(i,j)]+chemins_glt_rec1(Gra,G,v[0][1][0],v[0][1][1],c)
        print("La distance minimal est : ",c)
        return [(i,j)]
    return [(i,j)]



#partie 3
def initialiser_partie3(m,n):
    l = [[[0, 0, 0, 0,False] for i in range(m)] for j in range(n)]
    print(l)
    for i in l:  # initialiser
        for j in i:
            for k in range(len(j)-1):
                j[k] = randint(1,20)

    for i in l:  # affichage
        for j in i:
            print(j, end=" ")
        print()
    # egalisation des colognnes partagées entres les cases
    for i in range(m):
        for j in range(n - 1, 0, -1):
            l[i][j][3] = l[i][j - 1][1]
    # egalisation des lignes partagées
    for i in range(m -1, 0, -1):
        for j in range(n):
            l[i][j][0] = l[i - 1][j][2]
    l[m-1][n-1][3]=l[m-1][n-2][1]

    print("-" * 200)
    for i in l:
        for j in i:
            print(j, end=" ")
        print()
    return l
def chemins_glt_rec_partie3(Gra,G,i,j,c):
    m,n=len(G),len(G[0])
    G[0][0][4]=True
    if i!=m or j != n:
        v=Gra[j+i*n]
        if len(v)>1:
            if v[0][0]>v[1][0]:
                c+=v[1][0]
                G[v[1][1][0]][v[1][1][1]][0]=0
                G[i][j][2]=0
                G[v[1][1][0]][v[1][1][1]][4] = True
                return [(i,j)]+chemins_glt_rec_partie3(Gra,G,v[1][1][0],v[1][1][1],c)
            else:
                c+=v[0][0]
                G[v[0][1][0]][v[0][1][1]][3] = 0
                G[i][j][1] = 0
                G[v[0][1][0]][v[0][1][1]][4] =True
                return [(i,j)]+chemins_glt_rec_partie3(Gra,G,v[0][1][0],v[0][1][1],c)
        elif len(v)==1:
            if i==len(G)-1:
                G[v[0][1][0]][v[0][1][1]][3] = 0
                G[i][j][1] = 0
                G[v[0][1][0]][v[0][1][1]][4] = True
                c+=v[0][0]
            else:
                G[v[0][1][0]][v[0][1][1]][0] = 0
                G[i][j][2] = 0
                G[v[0][1][0]][v[0][1][1]][4] = True
                c+=v[0][0]
            return [(i,j)]+chemins_glt_rec_partie3(Gra,G,v[0][1][0],v[0][1][1],c)
            # G[v[0][1][0]][v[0][1][1]][3] = 0
            # G[i][j][1] = 0
            # G[v[0][1][0]][v[0][1][1]][4] = True
            # c+=v[0][0]
            # return [(i,j)]+chemins_glt_rec_partie3(Gra,G,v[0][1][0],v[0][1][1],c)
        # G[v[0][1][0]][v[0][1][1]][0] = 0
        # G[i][j][2] = 0
        # G[v[0][1][0]][v[0][1][1]][4] = True
        print("La distance minimal suivant algorithme de glouton est : ",c)
        return [(i,j)]
    return [(i,j)]



def dessiner_case(c,j,s,color,d):
    for i in range(len(c)):
        if i == len(c)-1:
            if c[0]!=0:
                pensize(c[0])
                forward(d)
            else:
                pencolor('white')
                forward(d)
                pencolor(color)
        else:
            if c[i]==0:
                pencolor('white')
                forward(d)  # Déplace la tortue de 150 unités vers l'avan
                right(90)  #
                pencolor(color)
            else:
                pensize(c[i])
                forward(d)  # Déplace la tortue de 150 unités vers l'avan
                right(90)  #
    if j == s:
        penup()
        hideturtle()
        setx(-300.0)
        sety(ycor()-d)
        showturtle()
        pendown()

def dessiner_grille(G,color):
    resetscreen()
    speed(1500)
    penup()
    hideturtle()
    setx(-300.0)
    sety(300.0)
    showturtle()
    pendown()
    pencolor(color)
    t = len(G)
    d=150
    if t>3:
        d = 100
    if t>6:
        d = 50
    if t>=8:
        d = 35
    for i in range(len(G)):
        for j in range(len(G[0])):
            dessiner_case(G[i][j],j,len(G[0])-1,color,d)

# Partie 4 
def list_to_dic(G):
    return {i:G[i] for i in range(len(G))}

def minimum(dico):
 m=float('inf')
 for k in dico: #parcours des clés
     if dico[k] < m:
         m=dico[k]
         i=k
 return i

def dijkstra(G,L,s,a):
 n=G[len(G)-2][-1][-1][-1]+1
 D={} #tableau final des distances minimales
 d={k: float('inf') for k in G} #distances initiales infinies
 d[s]=0 #sommet de départ
 P = {}
 while len(d)>0: #fin quand d est vide
     k=minimum(d) #sommet de distance minimale pour démarrer une étape
     for i in range(len(G[k])): #on parcourt les voisins de k
         v = G[k][i][1][1]+G[k][i][1][0]*n
         c = G[k][i][0]
         if v not in D: #si v n'a pas été déjà traité
             if d[v]>d[k]+c: #est-ce plus court en passant par k ?
                 d[v]=d[k]+c
                 P[v]=k
     D[k]=d[k] #copie du sommet et de la distance dans D
     del(d[k]) #suppression du sommet de d
 C = [0]+chemin_rec(P, 0, len(L)-1)    
 R = [L[k] for k in C]
 print("La distance minimal suivant algorithme de dijkstra est :",D[len(L)-1])
 return D,R

def chemin_rec(P,s,a):
    while a!=s:
        return chemin_rec(P, s, P[a])+[a]
    return []


g = initialiser_partie3(4, 4)
gra,l= parcoursgrille1(g)
print(gra)
print(chemins_glt_rec_partie3(gra, g, 0, 0, 0))
dessiner_grille(g, 'orange')
# GD = list_to_dic(gra)
# D,R=dijkstra(GD,l, 0,8)
# print(R)









