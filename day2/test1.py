from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score,confusion_matrix
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
print X_train.shape
print X_test.shape

#Knn Classifier
knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train,y_train)
p = knn.predict(X_test)
#==Print prediction
print p
#===Print Confusion matrix
print confusion_matrix(y_test,p)
#print accuracy
print accuracy_score(y_test,p)

#=====Plot graph=======
scores = list()
for i in range(1,25):
    knn1 =  KNeighborsClassifier(n_neighbors = i)
    knn1.fit(X_train,y_train)
    p1 = knn1.predict(X_test)
    a1 = accuracy_score(y_test,p1)
    scores.append(a1)
    
print scores
plt.plot(range(1,25),scores)
plt.xlabel("Y value")
plt.ylabel("accuracy")
plt.show()


