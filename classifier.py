##################################################
#Import  Libs

import scipy
import sklearn as sk
import matplotlib.pyplot as plt
from PIL import Image
import numpy
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import SGDClassifier
from sklearn.base import BaseEstimator
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix

#####################################################
#Get datas
new = []
old = []
new_file = open("new_song_array.txt",'r')
import time
star = time.time()
y=[]
for line in new_file:
    data = line.strip().split(',')
    temp = []
    for i in data:
        if i.isdigit():
            temp.append(float(i))
    data = temp
    new.append(data)
    y.append(1)
    #print(data)
print(len(y))
print("done")
new_file.close()
old_file = open("old_song_array.txt",'r')
for line in old_file:
    data = line.strip().split(',')
    temp = []
    for i in data:
        if i.isdigit():
            temp.append(float(i))
    data = temp
    new.append(data)
    y.append(0)
print(len(new))
print("done")
print(time.time()-star)

####################################################
#Shuffle
chaos = np.random.permutation(len(new))
X=[]
Y=[]
for i in chaos:
    X.append(new[i])
    Y.append(y[i])
train_X = X[:90]
train_Y = Y[:90]
test_X = X[90:]
test_Y = Y[90:]
print(np.array(train_X).shape)
print(np.array(train_Y).shape)
####################################################


#Create Classifications
svm_clf = Pipeline((("Scaler",StandardScaler()),("linear_svc",LinearSVC(C=1, loss="hinge")),))
svm_clf.fit(train_X,train_Y)
test = svm_clf.predict(test_X)
n = 0
correct = 0
for i in test:
    if i == test_Y[n]:
        correct+=1
    n+=1
print (float(correct)*100/len(test))
    
svm_score = cross_val_score(svm_clf,train_X,train_Y,cv=3,scoring="accuracy")
print (svm_score)
    
y_train_pred = cross_val_predict(svm_clf,train_X,train_Y,cv=3)
print (confusion_matrix(train_Y,y_train_pred))
    
if True:    
    sgd_clf = SGDClassifier(random_state=42)
    sgd_clf.fit(train_X,train_Y)
    test = sgd_clf.predict(test_X)
#    print len(test)
#    print len(test_Y)
    
    
    
    n = 0
    correct = 0
    for i in test:
        if i == test_Y[n]:
            correct+=1
        n+=1
    print (float(correct)*100/len(test))
    #print test_Y
    sgd_score = cross_val_score(sgd_clf,train_X,train_Y,cv=3,scoring="accuracy")
    print (sgd_score)
    
    y_train_pred = cross_val_predict(sgd_clf,train_X,train_Y,cv=3)
    print (confusion_matrix(train_Y,y_train_pred))
