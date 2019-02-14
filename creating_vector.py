import csv
from collections import defaultdict
import numpy as np
from scipy.signal import *
from numpy.fft import * 
from scipy import *
from pylab import *
import pywt
fout_data = open("train.csv",'a')
vec = []
chan = ['Fp1','AF3','F3','F7','FC5','FC1','C3','T7','CP5','CP1','P3','P7','PO3','O1','Oz','Pz','Fp2','AF4','Fz','F4','F8','FC6','FC2','Cz','C4','T8','CP6','CP2','P4','P8','PO4','O2']
columns = defaultdict(list) # each value in each column is appended to a list

with open("features_raw.csv") as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k
for i in chan:
	x = np.array(columns[i]).astype(np.float)
	coeffs = pywt.wavedec(x, 'db4', level=6)
	cA6, cD6, cD5,cD4,cD3,cD2,cD1 = coeffs
	cD5 = np.std(cD5)
	cD4 = np.std(cD4)
	cD3 = np.std(cD3)
	cD2 = np.std(cD2)
	cD1 = np.std(cD1)
	if i =="O2":
		fout_data.write(str(cD5)+",")
		fout_data.write(str(cD4)+",")
		fout_data.write(str(cD3)+",")
		fout_data.write(str(cD2)+",")
		fout_data.write(str(cD1))
	else:
		fout_data.write(str(cD5)+",")
		fout_data.write(str(cD4)+",")
		fout_data.write(str(cD3)+",")
		fout_data.write(str(cD2)+",")
		fout_data.write(str(cD1)+",")
fout_data.write("\n")
fout_data.close()
