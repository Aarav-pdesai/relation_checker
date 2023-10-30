#program to check type of relations
# 1 1 2 2 3 3
def sq_matrix(arr):
    new_mat=[[0]*n for i in range(n)]
    sum_t=0
    prod=1
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                prod=arr[i][k]*arr[k][j]
                sum_t+=prod
            new_mat[i][j]=sum_t
            sum_t=0
    return new_mat

def isreflexive(arr):
    flag=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                if arr[i][j]==1:
                    continue
                else:
                    flag=1
                    return False
    if flag==0:
        return True

def issymmetric(arr):
    flag=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j]!=arr[j][i]:
                flag=1
                break
        if flag==1:
            print("the given matrix is not symmetric. ")
            break
    if flag==0:
        print("the matrix is symmetric.")

def isTransitive(arr):
    flag=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j]==1:
                for k in range(len(arr)):
                    if matrix[j][k] == 1 and matrix[i][k] == 0:
                        return False
    return True
                    
                
    
def tuple_check(t_r,Rel,emp_arr):
    for i in t_r:
        if i in Rel:
            emp_arr.append(1)
        else:
            emp_arr.append(0)
    return emp_arr

d_s=list(map(int, input("enter the elements in the domain: ").split()))
cd_s=list(map(int, input("enter the elements in the co-domain: ").split()))
t_r=[(x,y) for x in d_s for y in cd_s]
print(t_r)
num=int(input("enter number of elements in the relation: "))
print('\n')
R=[]

for i in range(num):
    t=tuple(map(int,input("tuple: ").split()))
    R.append(t)
n=len(d_s)
matrix = [ [0]*n for i in range(n)]
arr=[]
x=tuple_check(t_r,R,arr)
if len(d_s)==len(cd_s):
    for i in range(n):
        for j in range(n):
            matrix[i][j]=x[3*i+j]

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" " )
    print('\n')

result1=isreflexive(matrix)
print("reflexivity: ",result1)

issymmetric(matrix)

s=sq_matrix(matrix)
print(s)

trans=isTransitive(matrix)
print("transitivity: ",trans)





