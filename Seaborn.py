import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

x=[1,2,3,4,5]
y=[2,6,2,4,5]
sns.lineplot(x="x",y="y")

from sklearn.datasets import load_digits    #load_digits is a dataset of handwritten numbers
digits=load_digits()
plt.gray()  #gray is used for mapping colors to numbers like heatmap

for i in range(10):
    plt.matshow(digits.images[i])   # matshow is used to show from load_digits #Upto 10 digits will be shown

x_tr, x_ts, y_tr, y_ts = train_test_split(digits.data, digits.target,test_size=0.2)

mdl=LogisticRegression()   
mdl.fit(x_tr,y_tr)  #Training the model
mdl.score(x_ts,y_ts) 
plt.matshow(digits.images[67])  #A random image will get generated
mdl.predict([[digits.data[67]]])   
#Making confusion matrix - used to show performance of our model
y_predicted=mdl.predict(x_ts)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_ts,y_predicted)
#For better visualisation use seaborn
import seaborn as sn
plt.figure(figsize=(10,7))
sn.heatmap(cm,annote=True)  #A heatmap is generated
plt.xlabel('Predicted')
plt.ylabel('Truth')

