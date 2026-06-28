#1. Keras base code
#Tensorflow, PyTorch - frameworks for deep learning
#Keras - Library inbuild in tensorflow
import tensorflow as tf
import sklearn
import keras
keras.backend.backend() 
from keras.models import Sequential
from keras.layers import Flatten,Dense,Activation
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import math

#1. Model on MNIST Dataset
#MNIST Dataset - 28 x 28 images of numbers - 2D matrix (0-255 range)
(x_train,y_train),(x_test,y_test)=keras.datasets.mnist.load_data()
plt.matshow(x_train[0])  #First element of x_train dataset gets printed which is 5 in y_train

x_train=x_train/255 #We are dividing by 255 to scale values between 0-1 better performance
x_test=x_test/255

x_train_flatten = x_train.reshape(len(x_train)) #This will change 28x28 to 784 input
x_test_flatten=x_test.reshape(len(x_test))

#Snippet to build model from keras
model=keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)), #input layer/array
    keras.layers.Dense(100,activation="relu"), #hidden layer
    keras.layers.Dense(10,activation="sigmoid") #output layer
])
model.compile(
              optimizer='adam',  #Optimiser helps to train efficiently
              loss='sparse_categorical_entropy', #Categorical loss
              metrics=['accuracy']
            )
model.fit(x_train,y_train,epochs=5) #epochs is Model ne poora training data kitni baar dekha (ya pass kiya)
model.evaluate(x_test_flatten,y_test) #Gives accuracy of model

y_predicted=model.predict(x_test_flatten) 
np.argmax(y_predicted[0]) #Jis bhi option pe sabse jyada probability aa rhi hongi us option ko dega

#Activation functions - 1)Linear -> 2)Step -> 3)Sigmoid -> 4)tanh -> 5)Relu(Leaky, Exponential) -> 6)

#Perceptron - y = f(w1*x1 + w2*x2 + .. + b)  f is activation function
#Matrix multiplication using numpy -> np.dot(units,price_per_unit)

#Errors - 1)MAE 2)MSE 3)Binary cross entropy(log loss) 4)
#Loss function - Indivisual losses, Cost function - MAE of all losses

#Code for MAE
y_pred=np.array([0,2,3,4])
y_true=np.array([2,3,4,5])

def MAE_loss(y_pred,y_true):
    y_diff=np.abs(y_pred-y_true) 
    loss=np.sum(y_diff)/y_diff.size[1] #Absolute loss using numpy array
    return loss

#Code for sigmoid
def sigmoid(x):
    ep=np.e
    return 1/(1+math.pow(ep,(-1)*x))

#Code for Log loss - mainly used for logistic regression
def log_loss(y_pred,y_true):
    epsilon=1e-15
    y_pred_new=[min(i,1-epsilon) for i in y_pred]   #Value which are 1 are set to 0.9999999
    y_pred_new=[max(i,epsilon) for i in y_pred_new] #Values which are 0 are set to 0.0000001 
    #Above changes are made to avoid log(0) = infinity now all elements of array are able to take log
    loss=-np.mean(y_true*np.log(y_pred_new)+(1-y_true)*np.log(1-y_pred_new))
    #Here log loss is always negative so to avoid it always multiply by -1 and to take log use np.log()
    return loss

#Gradient descent for neural networks
#Weightes are updated as many times as number of epochs
# Weights and biases are updated according to Loss after calculating the output predicted i true output and this is called back propogation
# w1 = w1 - learning_rate*(dL/dw1)
# b1 = b1 - learning_rate*(dL/db1)
# Do scaling that is take all values between 0 - 1 it increases models performance
#Chain rule derivatives are followed to take indirect derivatives
# dL/dw1 = (dL/derror)*(derror/dy_pred)*(dy_pred/dw1) 

#Code for gradient descent
def gradient_descent(age,affordibality,y_true,epochs,loss_threshold):
    w1=w2=1,b=0,rate=0.5
    n=len(age) #For numpy array cases

    for i in range(epochs):
        weighted_sum=w1*age+w2*affordibality+b
        y_pred=np.sigmoid(weighted_sum)
        loss=log_loss(y_true,y_pred)
        w1d = (1/n)*np.dot(np.transpose(age),(y_pred-y_true))
        w2d = (1/n)*np.dot(np.transpose(affordibality),(y_pred-y_true))
        bd=np.mean(y_pred-y_true)
        w1=w1-rate*w1d
        w2=w2-rate*w2d
        print(f"Epoch:{i},w1:{w1},w2:{w2},b:{b},loss:{loss}")

        if loss<=loss_threshold:
            break
    return w1,w2,b

class myNN:
    def __init__(self):
        self.w1=1
        self.w2=1
        self.b=0

    def fit(self,x,y,epochs,loss_threshold):
       self.w1,self.w2,self.b = self.gradient_descnet(x['age'],x['affordability'],y,epochs,loss_threshold)

    def predict(self,x_test):
        weighted_sum=self.w1*x_test['age']+self.w2*x_test['affordability']+self.b


    def gradient_descent(age,affordibality,y_true,epochs,loss_threshold):
        w1=w2=1,b=0,rate=0.5
        n=len(age) #For numpy array cases

        for i in range(epochs):
            weighted_sum=w1*age+w2*affordibality+b
            y_pred=np.sigmoid(weighted_sum)
            loss=log_loss(y_true,y_pred)
            w1d = (1/n)*np.dot(np.transpose(age),(y_pred-y_true))
            w2d = (1/n)*np.dot(np.transpose(affordibality),(y_pred-y_true))
            bd=np.mean(y_pred-y_true)
            w1=w1-rate*w1d
            w2=w2-rate*w2d
            print(f"Epoch:{i},w1:{w1},w2:{w2},b:{b},loss:{loss}")

            if loss<=loss_threshold:
                print(f"Epoch:{i},w1:{w1},w2:{w2},b:{b},loss:{loss}")
                break
        return w1,w2,b

custom_model=myNN()
custom_model.fit(x_train,y_train,epochs=5,loss_threshold=0.4631)
custom_model.predict(x_test)


#Batch Gradient Descent - We go through all samples calulate cost function by all losses of each sample and at end of epoch we update weights and biases - smooth curve
#Stochastic Gradient Descent - We take one randomly picked sample then update weights and biases then again take a sample and so on. Hence it updates weights and biases by each sample - Zig-zag line
model.compile(optimizer='SGD',loss='categorical_cross_entropy',metrics=['accuracy'])
#Mini-batch Gradient descent - Instead of using one randomly picked sample we use a ramdomly picked batch of(1-10) of samples and then update weights and biases 
model.fit(x_train,y_train,batch_size=64,epochs=10)
#To perform mini-batch gradient descent sirf batch size mention kr dena alag se code likhne ki jarurat nhi hai

#Tensorboard - tool used to debug the issues in neural network
tb_callback = tf.keras.callbacks.Tensorboard(log_dir="logs/",histogram_freq=1)
#To lauch tensorboard in jupyter notebook - use this commands
# %load_ext.tensorboard
# %tensorboard --logdir logs/fit

#Precision, Recall, F1 score -
#For precision, think about predictions as your base - predicted jitne as correct hai unme kitne sahi kiye hai
#For recall, think about truth as your base - sabhi mein se kitne sahi kiye hai
#F1 score = 2*((precision*recall)/(precision+recall))

#DROPOUTS - To reduce overfitting fomr neurons are dropped at time of training
modeel=keras.Sequential([
    keras.layers.Dense(60,input_dim=60,activation='relu'),
    keras.layers.Dropout(0.5),  #50% nerons of above layer gets off during training #These dropuout percentage is always between 10%-50%
    keras.layers.Dense(30,input_dim=60,activation='relu'),
    keras.layers.Dropout(0.2),  #20% nerons of above layer gets off during training
    keras.layers.Dense(1,activation='sigmoid')
])

#Handling imbalance dataset - Accuracy does not matter if the data is imbalance, if data is imbalance then F1 score matters, must be high as possible.Below methods improves pericision, recall, f1-score tested on two datasets one having class as true and another having class as false

#1)Under sampling majority class - 
#Ex: 99000 true, 1000 false --> combine random 100 true samples with 100 false samples then train model
# df_class_0_under_sampled=df_class_0.sample(count_class_1)
# Here df_class_0 has more samples than df_class_1 but we want both classes 1 and 0 as same so we take random number of samples equal to number of class 1 hence we created Under sampling df
# During train_test_split stratify=y ensures in train and test class distribution is equal

#2)Oversample the minority class by duplicating
#Ex: 99000 true, 1000 false --> 99000 true, 99000 flase by duplicating false elements
# df_class_1_over_sampled=df_class_1.sample(count_class_0, replace=True)
# Here as class 1 have less samples the samples gets duplicated according to the size of class 0

#3)Oversampling using SMOTE - Generate synthetic examples using k nearest neighbours algorithm. SMOTE = Synthetic Minority Over-sampling Technique. Here we use k nearest algorithm
# from imbleran.over_sampling import SMOTE
# smote=SMOTE(sampling_strategy='minority')
#x_sm,y_sm=smote.fit_sample(x,y)


#4)Ensemble method - Not useful
#Ex: 3000 true, 1000 false --> 1000 true, 1000 same false, 1000 true, 100 same false and 1000 true and 1000 same false making bunches and taking the majority vote

#5)Focal Loss - Penalize majority samples during loss calculation and give more weight to minority class samples

#---------------------CNN----------------------#
#CNN = Convolutional Neural Network
#Disadvantage of ANN - 1)Too much computation 2)Sensitive to location
#Filters - Matrix of nxn usually 3x3 wgich gets dot product from each matrix in original pictures are used for feature detection
#For a particular feature(eye,ear,nose) we build particular filters then after combining those small features we get the bigger one

from keras import datasets, layers, models
(x_train,y_train),(x_test,y_test)=datasets.cifar10.load_data()

classes=["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]

def plot_sample(x,y,index):
    plt.figure(figsize=(15,2))
    plt.imshow(x[index])
    plt.xlabel()

plot_sample(x_train,y_train,0)  #First image gets printed

cnn=models.Sequential([
    #cnn - Feature extraction
    layers.Conv2D(filters=32,kernel_size=(3,3),activation='relu',input_shape=(32,32,3)),
    layers.MaxPooling2D((2,2)), #Maxpooling reduces the dimensions and overfitting so it leads to faster computation

    layers.Conv2D(filters=64,kernel_size=(3,3),activation='relu'),
    layers.MaxPooling2D((2,2)),

    #ann - Classification
    layers.Flatten(),
    layers.Dense(64,activation='relu'), #activation relu is to introduce non-linearity in model
    layers.Dense(10,activation='softmax') #softmax for multiclass classification
])

cnn.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

cnn.evaluate(x_test,y_test)
y_pred=cnn.predict(x_test)
y_classes=[np.argmax(element) for element in y_pred]
plot_sample(x_test,y_test,0) #Image for y_test[0] along with label
classes[y_classes[0]] #Predicted label of that test data, here both may print 'ship'

#Padding -To increase importance of border elements Add one more frame of 0's in border
#Strides - By how much units we are jumping the window(size of filter) in image from left to right and from up to down



#Data Augmentation ------------------------------------
#If we have less data we build more images from existing images by rotating, scaling, zooming,etc as CNN by itself doesn't take care of rotation
dataset_url="https://----.tgz"
data_dir=keras.utils.get_file('flower_photos',origin=dataset_url,cache_dir='.',untar=True) 

import pathlib
data_dir=pathlib(data_dir) #data_dir contains path of flower_photos

flower_image_dict={
    'roses':list(data_dir.glob('roses/*')),
    'tulips':list(data_dir.glob('tulips./*')),
    'sunflower':list(data_dir.glob('sunflower./*')),
    'daisy':list(data_dir.glob('daisy./*')),
    'dandelion':list(data_dir.glob('dandelion./*')),
}

flower_labels_dict={
    'roses':0,
    'daisy':1,
    'dandelion':2,
    'sunflower':3,
    'tulips':4,
}

import cv2
x,y=[],[]
for flower_name,images in flower_image_dict.items():
    for image in images:
        img=cv2.imread(str(image)) #cv2 read the image from disc and converts it to three dimensional numpy array
        resized_img=cv2.resize(img,(180,180)) #Resizes image to a standard size because model expects all images to be of same dimensions
        x.append(resized_img)
        y.append(flower_image_dict[flower_name])

x=np.array(x)/255
y=np.array(y)/255

data_augmentation=keras.Sequential([
    layers.experimental.preprocessing.RandomZoom(0.9),
    layers.experimental.preprocessing.RandomContrast(0.9)
])
plt.axis=('off')
plt.imshow(x[0]) #orginal image
plt.imshow(data_augmentation(x)[0].numpy.astype("uint8")) #This will give changed images

#Just add line data_augmentation inside you model.Sequential and it will automatically apply
#Here you get x,y augmented dataset from available dataset

#Transfer Learning---------------------------------------------------------------------
#Tranfer Learning - Using a pretrained model, just replacind last layer of classification part accoding to out need of work but keep remining other layers which are used to study from edges of images,etc

from tensorflow_hub import hub #Hub se pretrained model milte hai

pretrained_model_without_top_layer=hub.KerasLayer(
"https://tfhub.dev/google/tf22-preview/mobilenet_v2/feature_vector/4",input_shape=(224,224,3),trainable=False)

num_of_flowers=5    #We are taking data from flower dataset used during data augmentation
model=tf.keras.Sequential([
    hub.KerasLayer(
    "https://tfhub.dev/google/tf22-preview/mobilenet_v2/feature_vector/4",
    input_shape=(224,224,3),
    trainable=False
    ),
    tf.keras.layers.Dense(num_of_flowers)

])
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossEntropy(from_logits=True),
    metrics=['acc']
)
model.fit(x,y,epochs=5)


#RCNN--------------------------------------------------------------------

#PixelMasking - CNN sirf us particular chiz ko alag colour se map krta hai
#Imagenet,coco,google open are some platforms for pretrained cnn models
#sliding window object detection - too much computation as we have try out for different wondow sizes - It developed as RCNN with lower computation

#YOLO - You only look once - fast
#Image classification - Is dog on that image VS Object Localization - Where exactly is the dog in this image using array
#Matrix - [Pc Bx By Bw Bh C1 C2]
#Pc - Probability of a person
#Bx - Point of centre of a n object in image, Bw- width of box, Bh - Height of box
#C1 - Here used if dog is present, C2- Here it woul be 1 if a person is present
#After trying all boxes the intersection of all such boxes make that particular object
#If a box in grid contains centre of both the objects such box is called anchor box

#RNN---------------------------------------------------------------------
#RNN = Recurrent neural network - used for textual data
#For a statement if we have single hiddenlayer it will process word by word of sentence with Names as 1 and proper englsih words as 0 and then translate it
#Vanishing gradient descent - With time the change in weights gets to 0 and it doesnt change due to almost 0 gradient to make change in them. As number of hidden layers grow, gradient becomes very small and weights will hardly change. This hamper the learning process
#Exploding gradient - When indivisual derivatives are large, the final derivatives will also become huge and weights would change drastically

#GRU - Gated Recurrent Unit - lightweight version of LSTM. GRU combines long term and short term memory units. As traditional RNN connot remember the key-words required to guess remaining sentence this help to accomplish this task. It has only two gates update gate and Reset gate

#Named Entity Recognition Problem - apple = company or fruit -> This is decided by words used after word apple. To keep track of those words use bidirectional RNN
#To convert words into numbers 1)TF-IDF 2)Word2Vec - An objects features are stored in vector like, iscountry, isperson, have-eyes,etc.

#Word Embedding - Embedding are not hand crafted. Instead, they are learnt during neural network training.Sabhi mile words ke har ek word ko ek index diya jata hai and usi feature matrix me weights initialize krke vertical matrix jisme jo feature hoga toh 1 otherwise 0 se multiply krte hai and resultant matrix milta hai. Then loss calculate krke by backpropogation weights get updated

#Techniques to computer word embedding : 1)Using supervised learning. 2)Using self-supervised learning - Word2Vec, Glove

reviews=['good','bad']
sentiments=np.array(1,0);
from keras.preprocessing import TextVectorization
TextVectorization('good',30)

vocab_size=30
encoded_reviews=[TextVectorization(d,vocab_size) for d in reviews]

from keras.preprocessing.sequence import pad_sequences
max_length=4
padded_reviews=pad_sequences(encoded_reviews,maxlen=max_length,padding='post')

from keras.layers import Sequential
from keras.layers import Embedding
from keras.layers import Flatten
embedded_vector_size=4
model.Sequential()
model.add(Embedding(vocab_size,embedded_vector_size,input_length=max_length, name="embedding"))
model.add(Flatten())
model.add(Dense(1,activation='sigmoid'))
x=padded_reviews
y=sentiments
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

model.fit(x,y,epochs=50,verbose=0)
model.get_layer('embedding').get_weights()[0] #This gives the weights of that RNN matrix

#Word2Vec - Allows to do mathematics with the words - ex: king - man + women = queen 
#Embeddings are not handcrafted. Instead, they are learnt during neural network training - 1.Take a fake problem 2.Solve it using neural network 3.You get word embeddings as a side effect

#RNN structure : Input layer->Hidden layers->Output layer(Vector with different value for each word). The weights get updated by backpropogation i.e calculating loss between y_pred and y_true and apply formula.Weights for similar kind of data would be similar.
#Continuos Bag of words (CBOW) = Given context words then predict target word
#Skip Gram = Given the target word then predict the context word like in sentence "king ordered that" where 'king' is target word and 'ordered that' are context words

#gensim library 
import gensim
# import python-Levenshtein
gensim.utils.simple_preprocess("This is! a sentence")  #->["this","sentence"] # It is used to tokenize the statement also by removing words like is the and remove ! marks,etc.
df=pd.read_json("reviews_cell_phones.json",lines=True)
review_text=df.reviewText.apply(gensim.utils.simple_preprocess)
model=gensim.models.Word2Vec(
    window=10, #number of words taken at a time
    min_count=2, #Atleast two words required for a sentence
    workers=4,
)
model.build_vocab(review_text,progress_per=1000)
model.train(review_text,total_examples=model.corpus_count,epochs=model.epochs)
model.wv.most_similar("bad") #This gives top 10 words present in dataset with similarity score ex: it goves terrible, awful,etc
model.wv.similarity(w1="great",w2="nice") #This gives similarity perecantage here 89% similarity in meaning or use in sentence

# VIDEO - 43 - Distributes training on NVIDEA DGX Station A100
# Distributed training - 50000 images hai toh 1000 uske baad 1000 aisa krke saare image distribute krke train krenge

tf.config.experimental.list_physical_devices()    #This showa all cpu and gpu available 
(x_train,y_train),(x_test,y_test)=keras.datasets.cifar10.load_data()
classes=['airplane','automobile','bird','dear'] #Is 4 tarike ki images rahengi jinhe hum classify krenge
x_train_scaled=x_train/255
x_test_scaled=x_test/255
y_train_categorical=keras.utils.to_categorical(
    y_train,num_classes=10,dtype='float32'
)
y_test_categorical=keras.utils.to_categorical(
    y_test,num_classes=10,dtype='float32'
)

def get_model():
    model=keras.Sequential([
        keras.layers.Flatten(input_shape=(32,32,3)),
        keras.layers.Dense(3000,activation='relu'),
        keras.layers.Dense(1000,activation='relu'),
        keras.layers.Dense(10,activation='sigmoid')
    ])

    model.compile(optimizer='SGD',loss='categorical_crossentropy',metrics=['accuracy'])
    return model

train_tf_dataset=tf.data.Dataset.from_tensor_slices(x_train_scaled,y_train_categorical) #This converst numpy array to tensorflow slice dataset
test_tf_dataset=tf.data.Dataset.from_tensor_slices(x_test_scaled,y_test_categorical)

strategy=tf.distribute.MirroredStrategy()
strategy.num_replicas_in_sync #Number of active GPUs
Batch_size_per_replica=250
Batch_size=Batch_size_per_replica*strategy.num_replicas_in_sync

train_dataset=train_tf_dataset.batch(Batch_size).prefetch(tf.data.AUTOTUNE) #Humne yaha pr main dataset ko 1000 ke size ke batches mein toda hai #prefetch 1000 ka datset process krke ho gya tph uske baad ke 1000 tyyar rakhega
test_dataset=test_tf_dataset.batch(Batch_size)

with strategy.scope():
    gpu_model=get_model()
    gpu_model.fit(train_dataset,epochs=50)

# VIDEO - 44 - Tensorflow Input Pipeline - Use 1)Handle huge dataset 2)Appy transformations to make dataset ready for model training
# tf_dataset=tf.data.Dataset.list_files('images/*').map(process_img).filter(filter_func).map(lambda x:x/255)  1)list_files - images load krega 2).map(process_img) - converts img to numpy ara=ray #.filter - removes blurry images 4).map(lamda x:x/255) - scaling krta hai

daily_sales_numbers=[21,22,-108,31,-1,32,34,31]
tf_dataset = tf.dataset.Dataset.from_tensor_slices(daily_sales_numbers)

#2 METHODS to iterate a tensorflow dataset
for sales in tf_dataset.as_numpy_iterator():
    print(sales)

for sales in tf_dataset:
    print(sales.numpy())

tf_dataset = tf_dataset.filter(lambda x: x>0) #Only positive values taken
tf_dataset = tf_dataset.map(lambda x:x*93) #Multipy all values by 93
tf_dataset = tf_dataset.shuffle(3) #3 ke set ko shuffle karge like 1 2 3 4 5 ko 2 3 1 4 5 krega but 4 5 differently shiffle honge and 1 2 3 differently. Is 3 ko buffer size kehte hai
tf_dataset = tf_dataset.batch(2) #Batching kr lega
#These all operations can be done in one line 

images_ds=tf.data.Dataset.list_files('images/*/*',shuffle=y_true)
class_names=["cat","dog"]
image_count=len(images_ds)
train_ds=images_ds.take(image_count*0.8) #80% of data lega 
test_ds=images_ds.skip(image_count*0.8) #80% od data skip krega and bacha hua 20% hi lega

s='images\\dog\\...jpg'
s.split("\\") #Ye \\ and \\ ke beech words ko numpy array ke form mein deta hai = ['images','dog','...jpg']
s.split("\\")[-2] #Ye sirf 'dog' dega i.e last second

#Is uper ki information ko use krke
def process_image(file_path):
    import os
    label=tf.strings.split(file_path,os.path.sep)[-2]
    img=tf.read_file(file_path)
    img=tf.image.decode_jpeg(img)
    img=tf.image.resize(img,[128,128])
    return img/255,label

#VIDEO 45 -  Optimize pipeline performance by prefetching by cpu as well as carryibg the training operation in GPU - ChatGPT Revise
import time
class FileDataset(tf.data.Dataset):
    def read_file_in_batches(num_samples):
        time.sleep(0.03)
        for sample_idx in range(num_samples):
            time.sleep(0.015)
            yield (sample_idx,)

        def __new__(cls):
            tf.data.Dataset.from_generator(
                cls.read_file_in_batches,
                output_signature=tf.TensorSpec(shape=(1,),dtype=tf.int64),
                args=(num_samples)
        )
    
def benchmark(dataset, num_epochs=2):
    for epoch_num in num_epochs:
        for sample in dataset:
            time.sleep(0.01)

benchmark(FileDataset().prefetch(1))
benchmark(FileDataset().prefetch(tf.data.AUTOTUNE))

dataset=tf.data.Dataset.range(5) #This stores 0 to 4 in that dataset
dataset.map(lambda x:x**2) #Each element of that data gets squared
dataset=dataset.cache()

def mapped_function(s): #Ye function kya kr rha hai
    tf.py_function(lambda:time.sleep(0.03),[],())
    return s

benchmark(FileDataset().map(mapped_function).cache(),5) #chache() se time almost half ho jata hai 

#VIDEO 46 - What is BERT





