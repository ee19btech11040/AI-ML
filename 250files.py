import numpy as np
import soundfile as sf

new_data = np.empty([25000,]) #creating an empty array for new file to be generated from original file
y1 = np.empty([25000,])

loc="back"

ind = 1
for j in range(1,80):
	b= loc+str(j)+".wav"
	data, samplerate = sf.read(b) #reading audio file using soundfile library
	print(len(data), samplerate)
	x= len(data)
	p = 25000-x
	d = int(p/26)
	
	for y in range(1 ,p, d):   
		for i in range(0,y-1):      #adding empty elements in the array in the start
			new_data[i] =y1[i]
		for i in range(y,25000-x+y-1):
			new_data[i] =data[i-y]
		for i in range(25000-y , 24999):    #adding empty elements in the array in the end 
			new_data[i] = y1[i]	
		a = "Final/"+loc+"/"+loc+str(ind)+".wav"    #total length becomes 25000
		ind += 1
		sf.write(a, new_data, samplerate)  #audio files are written back to harddisk
		print(len(new_data),j)
