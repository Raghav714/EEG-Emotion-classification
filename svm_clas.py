from sklearn import svm
import numpy as np
train_y = []
train_a = []
train_x = np.genfromtxt('train.csv',delimiter=',')
f = open("labels_0.dat","r")
for i in f:
	train_y.append(i)
train_y = np.array(train_y).astype(np.float)
train_y = train_y.astype(np.int)
train_x = np.array(train_x)
#print "valence",train_y
#print train_x
#print "train_x",train_x
clf = svm.SVC()
clf.fit(train_x, train_y)


f = open("labels_1.dat","r")
for i in f:
	train_a.append(i)
train_a = np.array(train_a).astype(np.float)
train_a = train_a.astype(np.int)
#print "arousal",train_a[1040:1280]
#print "train_x",len(train_x[0:26])
clf1 = svm.SVC()
clf1.fit(train_x, train_a)
#print test_a
predict_al = clf1.predict(train_x)
#print "alrosal",predict_al
predict_val = clf.predict(train_x) 
#print "valence",predict_val 
val_count = al_count = 0
for i in range(len(train_y)):
	if train_y[i] == predict_val[i]:
		val_count = val_count+1
	if train_a[i] == predict_al[i]:
		al_count = al_count+1
print "predicted valence",(float(val_count)/len(train_y))*100
print "predicted arousal",(float(al_count)/len(train_y))*100
# classifier efficiency
'''
predicted valence 98.046875 percentage
predicted arousal 97.890625 percentage

predicted valence 95.0
predicted arousal 96.09375 
'''
# output
'''
predicted valence 17.9166666667
predicted arousal 13.3333333333
'''
#chan = ['Fp1','AF3','F3','F7','FC5','FC1','C3','T7','CP5','CP1','P3','P7','PO3','O1','Oz','Pz','Fp2','AF4','Fz','F4','F8','FC6','FC2','Cz','C4','T8','CP6','CP2','P4','P8','PO4','O2']

