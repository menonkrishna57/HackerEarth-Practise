checker=input().strip()
l=len(checker)
if l%2!=0:
    l=len(checker)
    pt1=checker[0:l//2]
    pt2=checker[-1:l//2:-1]
    if pt1==pt2:
        print("YES")
    else:
        print("NO")
else:
    l=len(checker)
    pt1=checker[0:l//2]
    pt2=checker[-1:(l//2)-1:-1]
    if pt1==pt2:
        print("YES")
    else:
        print("NO")