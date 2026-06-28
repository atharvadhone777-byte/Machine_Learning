import pandas as pd             
import numpy as np               
import matplotlib.pyplot as plt                      
import warnings
warnings.filterwarnings('ignore')  #Isse agar koi warning aa rhi ho toh ignore ho jayengi onlu error ko dekhayega
from sklearn.metrics import classification_report #It is used to show performnace details of model

#VIDEO-0 : Intoduction to ML
#Supervised learning algo = Like teacher, provide correct answer while training and predicting values in testing
#Unsupervised learning = 
#In categorical variables - Nominal variables : Variables which do not have ordering or numeric data like strings "Paul","Arvi",etc
#In categorical variables - Ordinal variables : Variables which have ordering or numeric data like strings "low","high","satissfied","dissatisfied"

#VIDEO-1 - Linear Regression with one variable
#Linear(straigth line) regression = Used to predict values as it finds linear reln with inputs and outputs, use the independent variable to predict the dependent variable.
#Best Fit line = line that minimizes the difference between the actual data points and the predicted values. Reln btwn x and y must be linear. Its eqn : y = mx +c, hypothesis function has also same equation
#Residuals = actual value - predicted values, error is minimised by Least square method ∑(ya-yp)²
#If spread remains same along fit line then it is called homoscedasticity otherwise heteroscedasticity
#Cost function = Batata hai ki total error kitna hai

from sklearn import linear_model    #linear model gives Linear Regression
df=pd.read_csv('homeprice.txt',sep=" ") #Agar text file ho use csv se read krna ho to seperation=" " likho, so csv ki tarah read hoga
rg=linear_model.LinearRegression()
#[[]] are used to create dataframe from existing dataframe
x=df[['col1']] #But for multiple variable x = df[['col1','col2]] krna and y=df[['col3']] only this difference
y=df[['col2']]
from sklearn.model_selection import train_test_split
#80% data - training   20% data - testing
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
rg.fit(x_train,y_train)  #fit is used to train model
y_pred=rg.predict(x_test)
plt.scatter(x_test,y_test)
plt.plot(x_test,y_pred,color="blue") #This plots the line of linear regression 
rg.predict(3300)    #It gives approximate price by y=mx+c
rg.coef_  #Gives value of coefficient m in 'y=mx+c'
rg.intercept_  #Gives value of intercept  c in 'y=mx+c'
rg.score()  #Gives accuracy of that model between 0 and 1

#VIDEO-2 - Data Processing: Handling NA values

#VIDEO-3 - Linear Regression multiple variable(given above)
#But for multiple variable x = df[['col1','col2]] krna and y=df[['col3']] only this difference

#VIDEO-4 - Gradient Descent = Finds best fit line
#It starts with random value and leads to perfection

#Calculate change of cost function with slope and intercept
#∂J/∂m=− 2/n ∑ i=1 n x(y−(mx+c)) 
#∂J/∂c=− 2/n ∑ i=1 n (y−(mx+c))

def gradient_descent(x,y):  #not understood #revise
    m_curr=0    #y=mx+b
    b_curr=0
    n=len(x)    #len gives length of array
    iterations=1000
    learning_rate=0.001
    for i in range(iterations):
        y_predicted=m_curr*x + b_curr
        md = -(2/n)*np.sum(x*(y-y_predicted))  #∂J/∂m=− 2/n ∑ i=1 n x(y−(mx+c)) 
        bd = -(2/n)*np.sum(y-y_predicted)      #∂J/∂c=− 2/n ∑ i=1 n (y−(mx+c))
        m_curr=m_curr-learning_rate*md
        b_curr=b_curr-learning_rate*bd
        print(f"m: {m_curr}, b: {b_curr}, iteration: {i}") 

x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,33])
gradient_descent(x,y)   #gradient descent find krega m,b jispe error minimum hoga

#VIDEO-5 - save model using Joblib And Pickle
import pickle  #Use : Serialize python object into a file
with open('model_pickle','wb') as f:
    pickle.dump(rg,f)    #model is saved into that file

with open('model_pickle','rb') as f:
    temp_model=pickle.load(f)      #model saved in f gets loaded in variable temp_model

#Dumping file using joblib instead of pickle
from sklearn.externals import joblib
joblib.dump(rg,'new_file')   #model gets saved into this file

#VIDEO-6 - One Hot Encoding(OHE)
#One hot encoding - Method for converting categorial variables into binary format.It creates new columns for each category where 1 means the category is present and 0 means it is not.
#Need of OHE - If Male and female in category mein kaam krna hai. If Male=1 and female=0 kre to model mistakenly ise ranking se samjhega, isse deal krta hai OHE

#Method 1 - Using Pandas - preffered
dummy=pd.get_dummies(df.col1) #col1 ka har ek unique element ek column bn jayega. Like if x and y present tha then two columns col1_x and col1_y ban jayenge
final=pd.concat([df.drop('col1'),dummy],axis='columns') #Merges two dataframes and jis column mein vo data item of col1 present hoga sirf uske us column mein 1 mark hoga else 0. Also wo col1 hmne drop kr diya.
md1=linear_model.LinearRegression()
md1.fit(final.drop('col1',axis=1),final.col1)
md1.predict([2800,0,1]) #This gives value for given input in second place there is 0 i.e this dummy column is not required and in third place 1 ie this dummy column is required among all other dummy columns

#Method 2 - Using sklearn - doubt?
#sklearn will automatically drop a dummy variable but it is a good practice to drop it by your own
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder() #Elements ko 0 1 1 2 jaise encode krega
df.col1=le.fit_transform(df.col1) #Elements ko label de dega 0 1 1 1 2 jaise 
x = df[['col1','col2']]
y = df[['col3']]
from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder() 
ohe.fit_transform(x).toarray() #Converts into array datatype
x_=x[:,1:] #Selected all rows and droped first column and selected rest of other

#VIDEO-7 - Training and testing data

#VIDEO-8+9- Logistic Regression - Predicts probability of input belongs to a seperate class, not values like linear regression hence the dependent variable in logistic regression is categorical.Used for solving classifications
#Logistic regression model transforms linear regression into categorical value output using sigmoid
#Actually ye regression nhi to classification hai as ye value return nhi krta to Yes/no mein react krta hai

#sigmoid(x)= 1/(1 + pow(e,-x­))  s shaped function
#sigmoid(y)=1/(1+pow(e,-(mx+c))) as y=mx+c just substitute 

#Q. Study hours vs pass/fail/topper hone ki probability nikalo
from sklearn.linear_model import LogisticRegression
study_hours=np.array([1,3,5,7,9]).reshape(-1,1) 
#reshape(-1,1) 1D array ko 2D bna dega, as sklearn ko 2D chahiye hota hai, -1 se sklearn khud columns ginega and 1 number of features dikhata hai
Pass_probability=np.array([0,0,0,1,1,2]) #0=fail, 1=pass , 2=topper (multiclass classification)
clf=LogisticRegression(max_iter=1000)
# max_iter batata hai ki model maximum kitni baar try karega best coefficient(gradient descent) dhoondhne ke liye
x_train,x_test,y_train,y_test=train_test_split(study_hours,Pass_probability,test_size=0.20)
clf.fit(x_train,y_train)
clf.predict(6)    # 1 i.e pass not topper 
clf.predict_prob(6) # 0.10,0.55,0.35 fail,pass and topper hone ki probability dega (multinomial)
#Above example mein Pass_probability agar 0 and 1 mein hoti to binomial hota only for pass and fail 


#VIDEO-10 - Decision Tree (flowchart) - Data par questions pooch-pooch kar final decision tak pahuchta hai
#Ex: Kya baarish hori hai? --> Kya umbrella hai? and then it gives final decision, baahar jaana ya nhi

#Parts of decision tree - 1.Root Node : Sabse pehla and most imp question 2.Decision Node : Beech ke questions    3.Leaf Node : Final answer

#Entropy : Pure data(sab Yes ya sab No) -> Entropy 0  & Mixed data(Yes + No) -> Entropy zyada & Tree ka goal entropy kam krna. Gini bhi same as entropy hota bas thhoda fast hota hai.

# Is Study > 5?
#  ├── No → Fail
#  └── Yes:
#       Is Sleep > 5?
#         ├── Yes → Pass
#         └── No → Fail
#Decision tree only for one question is same as logistic regression bas ek se jyada Q ka combination aaya to decision tree use krna pdta hai

# Q. According to study and sleep time calculate whether a student will get passed or get failed
#Logic study and sleep dono enough honi chahiye tab hi pass
study_sleep=np.array([[2,8],[8,2],[6,7],[7,6],[3,3]])
Result=np.array([0,0,1,1,0]) 
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(max_depth=3)
model.fit(study_sleep,Result)
model.predict([[6,6]])  #pass

#VIDEO-11 - Support vector mechanism (SVM) - for both classification and regression
#SVM - Data ko ek line/plane se aise seperate kro ki gap(margin) maximum ho.
# 2D-line , 3D-plane , nD-hyperplane
#Use of SVM : To enlarge the margin between two classes, so it performs better for unseen data.
#Support vector : Wo closest points jo hyperplane ke sbse paas hote hain. Sirf yahi points matter krte hai, agar ye move kre to hyperplane change ho jayga.
#Hyperplane's equation : pow(w,t)x+b=0 Here w=direction of line, b=shift, x=input features
#Hard Margin=Data perfectly seperable
#Soft margin=Thoda error allowed,controlled by C parameter
#If c is higher kam misclassification,small margin but overfitting ka risk. If c is smaller then zyada misclassification,large margin and better generalization
#If data is not seperable by single line to data ko higher dimension mein le jaata hain (Kernel Trick)
#Kernel Types: 1.Linear(Straight line), 2.Polynomial(Curved), 3.RBF/Gaussian Kernel(Circular/Complex boundary), 4.Sigmoid Kernel(Neural network jais behave)
#gamma - 1.float 2.auto

from sklearn.svm import SVC
study_hours_and_Test_score=np.array([[2,40],[3,45],[4,50],[6,70],[7,75],[8,80]])
Admission_prob=np.array([0,0,0,1,1,1])
model=SVC(kernel='linear',C=1)
model.fit(study_hours_and_Test_score,Admission_prob)
prediction=model.predict([[5,65]])
#Above same example can be done using decision tree but in terms of 1.Noise handling, 2.Stability, 3.High dimensions i.e good for handling big number of questions,4.Overlifting

#VIDEO-12  Random Forest Algorithm
#Random Forest = Bhut saare decision trees banata hai and sab trees ka combined decision deta hai.Single decision tree ke liye bhut baar overfitting(galat prediction of new data) hota hai.
#Bootstrapping = Original dataset se random rows with replacement pick krta hai and har tree ka data thhoda alag rakhta hai jisse all possible answers mile.
#Feature Randomness(Column Sampling) = Har split pe saare features nhi dekhta, random subset of features dekhta hai.
#Aggregation(Voting/Averaging) : Classification ->Majority voting , Regression-> Average of predictions
#RandomForestClassifier -> Metric: entropy Ex:Spam detect
#RandomForestRegressor -> Metric: MSE  Ex:House price
#Random forest bta skta hai konsa feature kitna important 
#Random forest ye koi bhi model numerical daata pe kaam krta hai strings pr nhi so string wale data ko numerically encode kr dena by .get_dummies (dummy variables)
#Random forest jo problem solve krta same vo decision tree se bhi ho skte hai bas satbility and overfitting k afarak hai

#Hyperparameters : 
#1.n_estimators : Number of trees, if more trees then better but slower
#2.max_depth : Tree ki max depth, small depth->underfitting
#3.max_features : Har split pe kitne features dekhenge
#4.min_sample_split : Split krne ke liye minimum kitne samples
#5.min_samples_leaf : Leaf node me minimum samples, overfitting km krta hai

# Q.Loan Approval prediction can only be done by random forest classifier
data = {
    "Age": [25, 45, 35, 28, 50, 40, 30, 29, 60, 33],
    "Income": [3, 12, 7, 9, 15, 10, 6, 9, 20, 8],  # in Lakhs
    "CreditScore": [650, 800, 720, 710, 820, 760, 680, 740, 830, 700],
    "City": ["Tier2", "Metro", "Tier2", "Tier1", "Metro",
             "Metro", "Tier2", "Tier1", "Metro", "Tier2"],
    "JobType": ["Private", "Govt", "Private", "Private", "Govt",
                "Private", "Private", "Private", "Govt", "Private"],
    "PastDefault": [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    "Accounts": [2, 5, 3, 4, 6, 4, 3, 4, 7, 3],
    "Approved": [0, 1, 0, 1, 1, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)
df_encoded = pd.get_dummies(df,drop_first=True) #strings ko numerical data me encode kr dega
#Data ko train krne ke liye y mein result wala column store krenge and x mein baaki ke bache sabhi
x=df_encoded.drop("Approved",axis='columns')
y=df_encoded['Approved']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=100,max_depth=5)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,y_pred) #Gives score

#As it can also tell which feature is how much important
imp=model.feature_importances_
f_imp_df=pd.DataFrame({"Feature":x.columns, "Importance":imp}).sort_values(by="Importance",ascending=False) #Sabse jyada se km ki taraf importance and features name dega
new_customer = pd.DataFrame({
    "Age": [29],
    "Income": [9],
    "CreditScore": [720],
    "PastDefault": [0],
    "Accounts": [4],
    "City_Tier1": [1],
    "City_Tier2": [0],
    "JobType_Private": [1]
})
prediction = model.predict(new_customer)

#VIDEO-13 - Cross Validation(Evaluating Model performance)
#Option 1 = Use all available data for training and test on same dataset
#Option 2 = Split available dataset into training and testing dataset like (80-20 or 70-30)
#Option 3 = K Fold Cross validation - For 100 tests(folds), we will train model for test 2to100 and test for 1 then again train from 3to100 including 1 and test for 2 and keep doing untill the 100th test gets tested. Each time we do this process is called as split.

#Agar test data easy nikla ->more accuracy. Agar test hard nikla ->Less accuracy. So result luck pe depend kr rha hai so for overall better testing ke liye hm cross validation krte hai. Sabka average is final score of data

#shuffle=True krne se data random ho jata hai non-sorted way mein.
#Number of folds(k) = 5 to 10 tk thik hai km karoge to unreliiable rahega and zyada kroge to slow hoga
#Normal k fold - sirf data todta hai. Stratified k-fold - Har fold mein same class ratio rakhta hai.
#Time series mein K-Fold nhi kyuki future data se past predict krna = cheating, TimeSeriesSplit use kro

from sklearn.model_selection import KFold, cross_val_score
x=np.array([[1,60],[2,65],[8,95],[7,90]])
y=np.array([0,0,1,1])
model=LogisticRegression()
model.fit(x,y)
kf=KFold(n_splits=5, shuffle=True)
scores=cross_val_score(model,x,y,cv=kf) #cv=cross-validation splitting strategy or you can manually give cv value which is equal to number of splits
final_score=scores.mean()

#VIDEO-14 - K Means Clustering Algorithm
#Use - Data ko similar groups mein divide krna jab labels available na ho
#Clusters - Two median points assume kro and unhe join kro, then us line ko perpendicular nikalo then left side wale left cluster and right side wale right cluster

#Same clusters ke points pass mein ho baaki sab dur ho
#How to determine correct number of clusters - i.e ek banda bolega ki 2 clusters hai dusra 4 to tisra 6, actually correct number of clusters kitne hai ye ELBOW METHOD se pata chalega
#Elbow method - minimum SSE hona chahiye
# Sum of Squared errors = summation i=0 se i=n dist(x(i)-c1)² here c1 is position of first median point
# SSE = SSE1 + SSE2 + ... + SSEK (k = no. of clusters) From this formula aisa k select karo jaha SSE min ho

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
km=KMeans(n_clusters=3) #Khud se no. of clusters diye
df['cluster']=km.fit_predict(df[['col1','col2']])
#fit=centroid calculate krta hai and predict=har point ko cluster assign karta hai and fit_predict() dono ek saath krta hai .Adding new column to dataframe
scaler=MinMaxScaler()
scaler.fit(df[['col1','col2']])
df.col2=scaler.transform(df.col2) #col2 scale mein aa jaygi i.e between 0.0 to 1.0
df.col1=scaler.transform(df.col1)
#Ab tk centroid correct ho chuke hai
km1=KMeans(n_clusters=3)  #Humne bataya hai ki 3 clusters banenge
df['cluster']=km1.fit_predict(df[['col1','col2']])

#Data ko show krne ke liye
df1=df[df.cluster==0] #rows with data '0' in cluster column
df2=df[df.cluster==1] 
df3=df[df.cluster==2]
plt.scatter(df1.col1,df1.col2,color='green') 
plt.scatter(df2.col1,df2.col2,color='red') 
plt.scatter(df3.col1,df3.col2,color='black') 
plt.xlabel('x ka label')
plt.ylabel('y ka label')
plt.legend()

#VIDEO-15 - Naive Bayes - 1 
# Conditional probability P(A/B) = (P(B/A)*P(A))/P(B)
# Naive = Features such as male,class,age,etc are independent of each other

# Q.Find survival probabilty on titanic data using Bayes 
df=pd.read_csv("titanic.csv")
target=df.survived
input=df.drop('Survived',axis='columns')
dummies=pd.get_dummies(input.Sex) #One hot encoding of sex
input=pd.concat([input.drop('Sex'),dummies],axis='columns')
input.columns[input.isna().any()] #Columns jinme NaN value hai unke naam return krta hai
input.Age=input.Age.fillna(input.Age.mean()) #Most commonly mean value ko hi NaN me fill kiya jata hai
x_train,x_test,y_train,y_test=train_test_split(input,target,test_size=0.2)
from sklearn.naive_bayes import GaussianNB
model=GaussianNB() 
#NB = Naive bayes #As naive means features as independent of each other similarly Gaussian means features have Gaussian (normal) distribution
model.fit(x_train,y_train)
model.score(x_test,y_test)

#VIDEO-16 - Naive Bayes - 2

# Q.Spam detection in messages using naive bayes theorem
df=pd.read_csv('spam.csv')
df.groupby('Category').describe() #Category wise grouping with their count of occurences,unique,top,etc
df['spam']=df['Category'].apply(lambda x: 1 if x=='spam' else 0) #Spam column add ho jayga jisme if Category column mein 'spam' likha hoga then column mein 1 jayga otherwise 0
x_train,x_test,y_train,y_test=train_test_split(df.Messages,df.spam,test_size=0.2)
from sklearn.feature_extraction.text import CountVectorizer
v=CountVectorizer() #ML models can't understand test, they only understand numbers so CountVectorizer does this job
# Here v is a object 
x_train_count=v.fit_transform(x_train.values) #transform converts sentence into vector in which each position i is count of that word. Fit finds all unique words and assigns an index to them all like 'hello'=0, 'free'=1, etc.
x_train_count.toarray()[:3] #With any number of columns and fixed 3 number of rows

from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB() #Multinomial strongly predicts spam
#P(free/spam) = high, P(meeting/spam)=low, so using conditional probablity it predict accurate value
model.fit(x_train_count,y_train) 

emails=['Hey, mohan','Free money']
emails_count=v.transform(emails)
model.predict(emails_count) #Gives spam output 0 means no spam and 1 means spam
x_test_count=v.transform(x_test)
model.score(x_test_count,y_test)

#Pipelines= Multiple ML steps chained together as ONE model
from sklearn.pipeline import Pipeline
clf=Pipeline([  #clf=classifier
    ('step_1',CountVectorizer()),
    ('step_2',MultinomialNB())
])
clf.fit(x_train,y_train) #clf will automatically apply CountVectorizer and MultinomialNB to elements which gets fitted inside it. (This was main use of pipeline)

#VIDEO-17 - Hyper parameter tuning (GridSearchCV)
#Hyperparameter tunning = The process of choosing optimal model like SVM,Logistic Regression,Random forest,etc.
#To find the accurate score of each model don't go for train test split. Use K-Fold cross validation
from sklearn import datasets
iris=datasets.load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
df.isnull().sum()   #Har column mein kiyne null values hai ye batayega
#Here feature_names are petals height,sepals height,etc
df['flower']=iris.target #iris.target is a numpy array which labels of answers like 0='sentosa', 2='virginica'
df['flower']=df['flower'].apply(lambda x : iris.target_names[x]) #lambda function iterates through each row of that column and gives return accordingly 
#target_names converts the numeric 1 into its word form like 'versicolor'
svm_score=cross_val_score(SVC(kernel='linear',C=10,gamma='auto'),iris.data,iris.target,cv=5) # Here model ki jagah pe SVM ko directly initialize kr diya
# But there can diff values of c like 5,10,15 and diff kernels like 'linear', 'rbf' so we have take all those combinations values using for loop but this can be easily done by GridSearchCV

from sklearn.model_selection import GridSearchCV
model=SVC(gamma='auto')
parameters_grid={ #Contains all parameters values
    'C':[1,10,20],
    'kernel':['rbf','linear']
}

clf=GridSearchCV(model,parameters_grid,cv=5,scoring='accuracy',return_train_score=False)
#Grid->Saari possible combinations, Search->Sab combinations try, CV->Cross validation se correct score
#return_train_score decide krta hai training data ka score store karna hai ya nahi, False mtlb nhi
#scoring='accuracy' se decide hota hai ki best model accuracy ke base par decide hoga
clf.fit(iris.data,iris.target)
clf.cv_results_ #Gives mean test score
clf.best_score_ #Gives best score
clf.best_params_ #Gives best parameters for that model

#How to choose best model - Using GridSearchCV
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
model_params={  #Dictionary containing all models
    'svm':{
        'model':svm.SVC(gamma='auto'),
        'params':{
            'C':[1,10,15],
            'kernel':['rbf','linear']
        }
    },
    'random_forest':{
        'model': RandomForestClassifier(),
        'params':{
            'n_estimators':[1,5,10]
        }
    },
    'logistic_regression':{
        'model':LogisticRegression(solver='liblinear'),#liblinear - Ek time par ek feature ka weight optimize karta hai
        'params':{
            'C':[1,5,10]
        }
    }
}

scores=[] #Scores ki empty list
#Below model_name shows key and mp shows value and mp['model] is another key with all its values stored in it
for model_name,mp in model_params.items():
    clf=GridSearchCV(mp['model'],mp['params'],cv=5,return_train_score=False)
    clf.fit(iris.data,iris.target)
    scores.append({ #Each element will be dictionary
        'model':model_name,
        'best score':clf.best_score_,
        'best_params':clf.best_params_
    })

df=pd.DataFrame(scores,columns=['model','best_score','best_params']) #This gives model name and score along with best paramters to use

# Q.

#VIDEO-18 - L1 and L2 Regularization
#Overfitting ka issue remove krte hai L1 and L2
#Three types of fitting - underfit , overfit , balanced fit (does best prediction on new data)

#In equation f(x)=a1 + a2*x + a3*x² + a4*x³ + a5*x⁴
#L1: mse=(1/n)∑ i=1 to n (y - f(x))² + λ*∑ i=1 to n |a(i)|
#L2: mse=(1/n)∑ i=1 to n (y - f(x))² + λ*∑ i=1 to n a(i)²

#Lasso Regression - L1 Regularization
#Use Lasso Regression in place of logistic regression, gives very less gap between training and testing data
from sklearn.linear_model import Lasso
lasso_reg=Lasso(alpha=50,max_iter=100,tol=0.1)
lasso_reg(x_train,y_train)
lasso_reg.score(x_test,y_test)

#Ridge Regression - L2 Regularization
#L2 is better than L1 as gap again decreses between training and testing dataset scores
from sklearn.linear_model import Ridge
ridge_rg=Ridge(alpha=50,max_iter=100,tol=0.1)
ridge_rg.fit(x_train,y_train);
ridge_rg.score(x_test,y_test)

#VIDEO-19 - KNN classification (K nearest neighbours classification)
# If 3 clusters mein data divided hai, ek random point hamne choose kiya and uske nearest k points count kiye ki kitne konse cluster ke hai, jis cluster ke max number of points us cluster ko vo point belong karega

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=3) 
# n_neighbors = number of k i.e points we consider
knn.fit(x_train,y_train)
knn.score(x_test,y_test) #It gives score whether a from given input it gives correct class or not

from sklearn.metrics import confusion_matrix
y_pred=knn.predict(x_test)
confusion_matrix(y_test,y_pred) #Check accuracy test-wise

#VIDEO-20 - Principal Component Analysis (PCA)
# You have 100's of columns among which cols which does not affect that much are removes or not considered
# PCA is a process of figuring out most important features/columns or principal components that has the most impact on the target variable
#Principal Component - It is a new uncorrelated feature created by linear combination of other features that captures maximum varinance from data
#PC1 - It is just like line of linear regression
#PC2 - Feature line\/direction perpendicular to PC1

#PCA(n_components=6) ,here we are asking PCA to give only 6 most imp features
#Things to keep in mind before using PCA 1.Scale Features Before Applying PCA  2.Accuracy might drop
#PCA helps to reduce dimentions so it is called dimentionality reduction technique

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model=LogisticRegression()
model.fit(x_train,y_train)
model.score(x_test,y_test) #Without PCA - 0.9722

from sklearn.decomposition import PCA
pca=PCA(0.95) #This shows retain 95% of useful features
pca_x=pca.fit_transform(x)
pca.explained_variance_ratio_ #Explains each column
pca.n_components_ #Gives number of columns after doing PCA sorting the useful features
x_train,x_test,y_train,y_test=train_test_split(pca_x,y,test_size=0.2)
model=LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)
model.score() #With PCA - 0.9694 (almost equal) but higher speed due to less features

#VIDEO-21 - Bias vs Variance 
#overfit: train error=0 , test error=93
#underfit: train error=42, test error=47
#balanced fit: train error=11, test error=15

#Bias: Bias is measurement of how accurately a model can capture a pattern in a training dataset. If high train error then is is said to have higher bias

#VIDEO-22
# Resampling with replacement - Randomly pick datapoint however we have already selected it
# Pick multiple datasets and train model on all those subsets, final result prediction will be taken by majority vote which is called ensemble learning. 
# As these models are not all exact datapoints of original set, so our model will not overfit
# Bootstrap Aggregation - Taking average of all those subclasses if they are giving certain value

# Bagging - Underlying models can be anything (SVM,knn,Logistic regression,etc)
# Bagged tress - Each model is a tree

from sklearn.ensemble import BaggingClassifier

bag_model=BaggingClassifier(
    base_estimator=DecisionTreeClassifier(),
    n_estimators=10, #Number of subsets of dataset
    max_samples=0.8, #Use 80% of total datset for each subset
    oob_score=True,  #oob = Out of bag 
)
bag_model.fit(x_train,y_train)
bag_model.score()  #score=78%

#If we do same method by random forest method as it also works on majority decision taken by number  of decision trees  it gives score of 71% whci is less than bagging

















