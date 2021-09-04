# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 18:20:30 2021

@author: Guoli
"""


import numpy as np
import itertools


def size_check(mat):
        
    assert np.shape(mat)[0] == np.shape(mat)[1], 'Please input square matrices'
         
    return   True
    
def same_size(matA, matB):
    
    assert np.shape(matA) == np.shape(matB), 'Please input same size matrices'
    
    return True

    
def addition(matA, matB, p):
        
    if size_check(matA)== True and same_size(matA, matB)==True:
        sum_mat = matA + matB
        return sum_mat % p
    else:
        print('Please input right size matrices!')
             
        
def multiplication(matA, matB, p):
    
    if size_check(matA)== True and same_size(matA, matB)==True:
        matC =matA.dot(matB)
        return matC % p,
    else:
        print('Input size error')

def generate_matrix(n, p):
    gene_mat = np.zeros((n,n))
    lst = []
    for i in range(n):
        for j in range(n):
            lst.append(gene_mat[i][j])
    lst1 = []
    for i in range(1,len(lst)): 
        for j in range(len(lst)):
        
            lst_copy = lst[:]
            lst_copy[j] = i%p
            lst_copy[0:j]=lst[0:j]
            lst_copy[j+1:]=lst[j+1:]
            lst1.append(lst_copy)
            
    return lst1  
    pass


def list_generator(n,p):
    ist = []
    if n==1:
        for i in range(p):
            ist.append([i])
        return ist
    else:
        for a in list_generator(n-1, p):
            for b in list_generator(1, p):
                ist.append(a+b)
    return ist

#print(list_generator(4, 3))

def list_even_splitor(list_split, n):
    
    '''
    Parameters
    ----------
    list_split : list that needs to be splited.
    n : integer, the length of each list after splitting

    '''
    res = []
    list_splited = list(itertools.combinations(list_split, n))
    #print('list splited is:', list_splited)
    for li in list_splited:
        if list(li) not in res:
            res.append(list(li))
            #print('res is:', res)
            
    return res
#print(list_even_splitor([1,1,1,1], 2))            




def tripotent_generator(n,p):
    
    lst =[]
    if n == 1:
        for i in range(p):
            if i**3 == i:
               lst.append([i])
        return lst
    elif n==2:
        for a11 in tripotent_generator(1, p):
            for a12 in tripotent_generator(1, p):
                for a21 in tripotent_generator(1, p):
                    for a22 in tripotent_generator(1, p):
                        a = np.array([a11,a12,a21,a22]).reshape(2,2)
                        b = (a.dot(a))%p
                        comparsion = (b.dot(a))%p == a
                        if comparsion.all() == True:
                            lst.append(a)
                        #lst.append(np.array([a11,a12,a21,a22]).reshape(2,2))
                       # print(np.array([a11,a12,a21,a22]).reshape(2,2))
                        #print('\n')
                        
        return lst
    elif n > 2:
        for a11 in tripotent_generator(1, p):
            #print('a11 is:', a11)
            for list_ele in list_generator(2*n-2, p):
                #print('list_ele is:', list_ele)
                for splited_list in list_even_splitor(list_ele, n-1):
                    #print('splited_list is:', splited_list)
                    for A in tripotent_generator(n-1, p):
                        A = np.insert(A, 0, splited_list, axis = 0)#row insert
                        #print('A after row insert:', A)
                        #A = np.vstack([A, splited_list])
                        #A[[0,n-1]] = A[[n-1, 0]]
                        for splited_list in list_even_splitor(list_ele, n-1):
                            for a11 in tripotent_generator(1, p):
                                a = np.insert(A, 0, a11+splited_list, axis = 1)#column insert for A
                                #print('A after column insert:',a )
                                b = (a.dot(a))%p
                                comparsion = (b.dot(a))%p == a
                                if comparsion.all() == True:
                                    lst.append(a)



    Lst = {array.tobytes(): array for array in lst}


    return list(Lst.values())
                    
                 
print(tripotent_generator(3, 3))  # print 3 by 3 tripotent matrices over $F_3$ 
 



#Test: decomposing the following matrix 'mat' as a sum of two tripotents
   
mat = np.array([[0,0,1],[1,0,1],[0,1,0]]) 
trip_list = tripotent_generator(3, 3)
decomp_ways = [] # will append ways of different decompositions in this empty list
for trip1 in trip_list:
    
    for trip2 in trip_list:
        new_trip = (trip1 + trip2)%3 
        #print('new trip is:', new_trip)
        comparsion_mat = new_trip == mat
        if comparsion_mat.all() == True:
            decomp_ways.append((trip1,trip2))
          
print(decomp_ways[0])          
       





























            
            
        