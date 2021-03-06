from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn.metrics import  accuracy_score,confusion_matrix,classification_report
import  matplotlib.pyplot as plt

iris = load_iris()
#======Load Data=======
#print iris.data
#Load Target Data======
#print iris.target
X = iris.data
y = iris.target
#print y
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
#print X_train.shape
#print X_test.shape

#Knn Classifier
knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train,y_train)
p = knn.predict(X_test)
#==Print prediction
#print p
#===Print Confusion matrix
#print confusion_matrix(y_test,p)
#print accuracy
#print accuracy_score(y_test,p)

#=====Plot graph=======
score = cross_val_score(knn, X,y,cv = 10)
print"Report", classification_report(y_test, p)
print "score=",score


