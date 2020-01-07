def is_palindrom(l):
	for i in range(0,len(l)/2):
		if(l[i]!=l[len(l)-i-1]):
			return false
	return true

def no_of_vaid_pair(l):
	ans = len(l)*len(l[0])
	for i in range(3,min(l,l[0],2)+1):
		for j in range(int(i/2),min(l,l[0])-int(i/2)+1):
			for k in range(int(i/2),min(l,l[0])-int(i/2)+1):
				if(is_palindrom(l[j-1:j+2][k]) and is_palindrom(l[j][k-1])):
					ans+=1
	return ans
t = int(input())
while(t>0):
    t-=1
    n,m = input().split()
    l =[]
    for i in range(n):
        temp = [int(x) for x in input().split()]
        l.append(temp)
    print(no_of_vaid_pair(l))