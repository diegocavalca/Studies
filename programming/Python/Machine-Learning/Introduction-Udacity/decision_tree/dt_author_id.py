#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

print "-----------------------------------------"
print "- - - - - - - - RESULTS - - - - - - - - -"
print "-----------------------------------------"

from sklearn import tree

print ">>> Total of features: ", len(features_train[0])

clf = tree.DecisionTreeClassifier(min_samples_split=40)

# Training...
print " "
t0 = time()
clf.fit(features_train, labels_train)
print ">>> Training time:", round(time()-t0, 3), "s"

# Predicting...
print " "
t0 = time()
predict = clf.predict(features_test)
print ">>> Predict values: ", predict
print ">>> Predicting time:", round(time()-t0, 3), "s"

# Accuracy...
print " "
accuracy = clf.score(features_test, labels_test)
print ">>> Clasifier Accuracy: ", accuracy*100

tree.export_graphviz(clf, out_file='tree.dot')

#########################################################

