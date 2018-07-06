import cPickle
import os
from multiprocessing import Pool
import sys
import numpy as np
chan = ['Fp1','AF3','F3','F7','FC5','FC1','C3','T7','CP5','CP1','P3','P7','PO3','O1','Oz','Pz','Fp2','AF4','Fz','F4','F8','FC6','FC2','Cz','C4','T8','CP6','CP2','P4','P8','PO4','O2']
nLabel, nTrial, nUser, nChannel, nTime  = 4, 40, 32, 32, 8064
print "Program started \n"
fout_labels0 = open("labels_0.dat",'w')
fout_labels1 = open("labels_1.dat",'w')
fout_labels2 = open("labels_2.dat",'w')
fout_labels3 = open("labels_3.dat",'w')
for i in range(nUser):#4, 40, 32, 32, 8064
	if i < 10:
		name = '%0*d' % (2,i+1)
	else:
		name = i+1
	fname = "/data_preprocessed_python/data_preprocessed_python/s"+str(name)+".dat"
	x = cPickle.load(open(fname, 'rb'))
	print fname
	for tr in range(nTrial):
		fout_data = open("features_raw.csv",'w')
		for ch in chan:
			fout_data.write(ch+",")
		fout_data.write("\n")
		for dat in range(nTime):
			for ch in range(nChannel):
				if ch <32:
					if ch == 31:
						fout_data.write(str(x['data'][tr][ch][dat]));	
					else:					
						fout_data.write(str(x['data'][tr][ch][dat])+",");
			fout_data.write("\n");
		fout_labels0.write(str(x['labels'][tr][0]) + "\n");
		fout_labels1.write(str(x['labels'][tr][1]) + "\n");
		fout_labels2.write(str(x['labels'][tr][2]) + "\n");
		fout_labels3.write(str(x['labels'][tr][3]) + "\n");
		fout_data.close()
		os.system('python creating_vector.py')
		print "user "+ str(i) +" trail"+ str(tr)
fout_labels0.close()
fout_labels1.close()
fout_labels2.close()
fout_labels3.close()
print "\n"+"Print Successful"
