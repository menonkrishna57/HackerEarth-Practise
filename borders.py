"""Problem
You are given a table with 
 rows and 
 columns. Each cell is colored with white or black. Considering the shapes created by black cells, what is the maximum border of these shapes? Border of a shape means the maximum number of consecutive black cells in any row or column without any white cell in between.

A shape is a set of connected cells. Two cells are connected if they share an edge. Note that no shape has a hole in it.

Input format

The first line contains 
 denoting the number of test cases.
The first line of each test case contains integers 
 denoting the number of rows and columns of the matrix. Here, '#' represents a black cell and '.' represents a white cell. 
Each of the next 
 lines contains 
 integers."""



casesno=int(input())
cases=[]
for i in range(casesno):
    thecaseinfo=input().split(" ")
    thecase=[]
    for v in range(int(thecaseinfo[0])):
        a=list(set(input().split(".")))
        a.pop(0)
        if a!=[]: 
            l=len(a[0])
        else:
            l=0
        thecase.append(l)
    cases.append(thecase)

for i in cases:
    print(max(i))
