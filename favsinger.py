total=int(input())
playlist=input().split(" ")
artists=list(set(playlist.copy()))
highest=0
highestnumber=0
counter=[]
for i in range(len(playlist)):
    print(i)
    print(playlist)
    counter[i]=playlist.count(artists[i])
    if counter[i]>highest:
        highest=counter[i]

print(counter)