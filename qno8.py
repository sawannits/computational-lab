import numpy as np
mid = np.array([
    [65, 70, 68, 72],
    [78, 75, 80, 77],
    [55, 60, 58, 62],
    [82, 85, 80, 88],
    [70, 68, 72, 74]
])
end = np.array([
    [72, 78, 75, 80],
    [84, 82, 86, 83],
    [65, 68, 66, 70],
    [88, 90, 85, 92],
    [78, 75, 80, 82]
])
tm=np.sum(mid,axis=1) #axis 1= row and axis 0= coloumn
te=np.sum(end,axis=1)
a1=np.mean(mid,axis=1)
a2=np.mean(end,axis=1)
#percent improvement=(end-mid)/mid*100

for i in range(0,mid.shape[0]):
	pi=(te-tm)/tm*100 
	print(f"total of student {i+1} is mid sem:{tm[i]},end sem:{te[i]}\navg of student {i+1} is mid sem:{a1[i]},end sem:{a2[i]}")
	print(f"percentage improvement={pi[i]:.2f}%\n")
