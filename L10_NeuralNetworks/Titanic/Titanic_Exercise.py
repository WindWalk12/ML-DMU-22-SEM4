#Titanic dataset predictions

#import panda library and a few others we will need.
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# skipping the header
data =pd.read_csv('titanic_train_500_age_passengerclass.csv', sep =',', header = 0)

# show the data
print ( data .describe( include = 'all' ))
#the describe is a great way to get an overview of the data
print ( data .values)

# Replace unknown values. Unknown class set to 3
data["Pclass"].fillna(3, inplace = True)

# Replace unknown values. Unknown age set to 25
data["Age"].fillna(27, inplace = True)

# Replace unknown values. Unknown survival set to survived
data["Survived"].fillna(1, inplace = True)


yvalues = pd.DataFrame( dict ( Survived =[]), dtype = int )
yvalues[ "Survived" ] = data [ "Survived" ].copy()
#now the yvalues should contain just the survived column

x = data[ "Age" ]
y = data[ "Pclass" ]
#plt.figure()
#plt.scatter(x.values, y.values, color = 'black' , s = 20 )
#plt.show()

#now we can delete the survived column from the data (because
#we have copied that already into the yvalues.
data.drop( 'Survived' , axis = 1 , inplace = True )

data.drop( 'PassengerId' , axis = 1 , inplace = True )

# show the data
print ( data.describe( include = 'all' ))

xtrain = data.head( 400 )
xtest = data.tail( 100 )

ytrain = yvalues.head( 400 )
ytest = yvalues.tail( 100 )

print ( ytrain )

from sklearn.model_selection import train_test_split
datasets = train_test_split(xtrain, ytrain, test_size=0.2)

X_train, X_test, y_train, y_test = datasets

# Feature scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=10000, random_state=0)
mlp.fit(X_train, y_train)

#predictions
predictions = mlp.predict(X_test)

print(predictions)

import matplotlib.pyplot as plt
import numpy as np

# Calculate confusion matrix
conf_matrix = confusion_matrix(y_test, predictions)

# Calculate accuracy
accuracy = np.trace(conf_matrix) / float(np.sum(conf_matrix))

# Plot confusion matrix
plt.figure(figsize=(8, 6))
plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix (Accuracy: {:.2f}%)'.format(accuracy * 100))
plt.colorbar()
tick_marks = np.arange(2)
plt.xticks(tick_marks, ['Predicted Survived', 'Predicted Not\nSurvived'], rotation=0, ha='center')
plt.yticks(tick_marks, ['True Survived', 'True Not\nSurvived'], va='center')

for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):
        plt.text(j, i, str(conf_matrix[i, j]), horizontalalignment="center", color="white" if conf_matrix[i, j] > conf_matrix.max() / 2 else "black")

plt.tight_layout()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()
