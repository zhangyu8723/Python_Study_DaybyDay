a = [1,2,3]
b = [4,5,6,7,8]

zipped = zip(*zip(a,b))
#print(list(zipped))
#print(*zip(zipped))


a = [ 1,2,3,None,(),[],]
print(len(a))