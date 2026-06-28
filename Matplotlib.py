import matplotlib as ml
print(ml.__version__)   #3.10.8 
import matplotlib.pyplot as mp
import numpy as np
import pandas as pd

#Making plot
x1=np.array([10,10,12])  #Lists dikhte hi numpy arrays mein convert kr lena
y1=np.array([20,21,22])
x2=np.array([13,17,24])
y2=np.array([22,45,67])
mp.plot(x1,y1)    #To make the graph
mp.plot(x2,y2)    #If we plot 2 graphs simultaneously both will be shown
mp.show()       #To show the graph
mp.plot(y1)      #If only y values are plotted then x values are provided like 0 0.5 1 1.5 as default

#Plot customisation
line_style=dict(marker=".",         #At each point there will be . (dot)
                markersize=20,      #Size of . is 20
                markerfacecolor="cyan", #Inside color is cyan
                markeredgecolor="red",  #Border color is red
                linestyle="dashdot",    #Line is dashdot
                linewidth=3,
                color="green")          #color is line color

mp.plot(x1,y1,**line_style) #** is used to unpack dictionary at those points so styles are applied

#Labels
mp.title("Graph name",          #Title is shown above graph
         fontsize=20,
         family="Arial",
         fontweight="bold",
         color="blue")  
mp.xlabel("Year")   #Label on x axis
mp.ylabel("Value")  #Label on y axis
mp.xticks("x")      #Pass numpy array of x in it so it gives only x-axis value at that point 
mp.tick_params(axis="both",colors="green")  #This gives styles to ticks at both axis 

#Grid lines = Helps make plots easier to read by adding refrence lines
mp.grid(axis="both",              #Grid lines appears on both axis #If want only one select accordingly
        linestyle="dashed",
        color="ligthgray"
        )  

#Bar Charts = compare categories of data by representing each category with a bar
a=np.array(["d1","d2","d3"])
b=np.array([4,3,5])
mp.bar(a,b,color="red") #x axis pe c and y axis pe v
mp.barh(a,b)    #Bar horizontal hoga instad of vertical lines
mp.show()

#Pie chart = Circular chart divided into slices to show percentages of total.
c=np.array(["d1","d2","d3"])
d=np.array([200,230,270])
colors=["red","yellow","blue"]
mp.pie(d,labels=c,          #First pass distribution d the values/labels c
       autopct="%1.2f%%",   #Shows percentage in divisions .2 shows we need only 2 digits after decimal and %% shows % after value
       colors=colors,       #Includes colors list
       explode=[0,0,0.5],   #Explode se vo dision pie chart se break hoke dur chale jata hai like ice plates in antarctica
       shadow=True,         #Applies shadow
       startangle=30        #Pie chart rotates to given angle  
       )   
mp.title("Pie chart title")
mp.show()

#scatter graph = Shows the relationship between two variables. Helps to identify a correlation (+, -, None) Ex: Study hours vs. Test scores
e=np.array([0,1,1,2])
f=np.array([55,60,65,62])
g=np.array([0,1,2,5])
h=np.array([52,69,44,98])
mp.scatter(e,f,
            color="red",
            alpha=0.8,        #alpha is transperancy/opacity of dots
            s=100,            #size of dots
            label="Class A")  #One graph shows unique class with unique color called legend

mp.scatter(g,h,
            color="blue",        
            s=100,
            label="Class B")         

mp.legend() #Class A and Class B will be shown
mp.xlabel("Label for x axis")
mp.ylabel("Label for y axis")
mp.show()

#3D Plotting - only in scatter
ax=mp.axes(projection="3d")
x_1=np.random.random(100)
y_1=np.random.random(100)
z_1=np.random.random(100)
ax.scatter(x_1,y_1,z_1)
mp.show()

#3D plotting ex
bx=mp.axes(projection="3d")
x_2=np.arange(0,50,0.1)
y_2=np.sin(x_2)
z_2=np.cos(x_2)                 #When plotting becomes impossible it throws error
bx.plot(x_2,y_2,z_2)            #Use plot in terms of sin,cos
bx.set_title("3D Plot")
bx.set_xlabel("test")
mp.show()

#3D Meshgrid
import matplotlib.pyplot as mp
import numpy as np
cx=mp.axes(projection="3d")
x_3=np.arange(-5,5,0.2)
y_3=np.arange(-5,5,0.1)
x_3,y_3=np.meshgrid(x_3,y_3)
z_3=np.sin(x_3)*np.cos(y_3)
cx.plot_surface(x_3,y_3,z_3,cmap="Spectral")
cx.view_init(azim=0,elev=90)    #This sets default view then we have to change it
mp.show()

#Histogram = A visual representation of distribution of quantitative data. They group values into bins (intervals) & counts falls in each range
k=np.random.normal(loc=80,      #loc is the midpoint & highest point of histogram
                   scale=10,    #scale is standard deviation 
                   size=100)    #size is spread across x-axis i.e, number of test scores
k=np.clip(k,0,100)              #All scores below 0 are set to zero and all scores above 100 set to zero
mp.hist(k,bins=10,              #It have 10 columns/bins
        color="green",
        edgecolor="black"       #Border of each column will be black
        )      
mp.title("Histogram title")
mp.xlabel("Label for x axis")
mp.ylabel("Label for y axis")
mp.show()

#Subplots
#Figure - The entire canvas
#Ax - A single plot (subplot), it ia a numpy array
u=np.array([1,2,5,4,6]) #As values increasing order mein nhi hai to ek loop bnega beech mein😂
figure,axes=mp.subplots(2,2)  #2 rows and 3 columns

axes[0,0].plot(u,u*2,color="red")       #Plot lines are inserted in on ebox indexed (0,0) 
axes[0,0].set_title("Graph 1 title")

axes[0,1].bar(u,u**2,color="blue")      #Bar charts bhi use kr skte hai   
axes[0,1].set_title("Graph 2 title")

axes[1,0].plot(u,u**3,color="yellow")         
axes[1,0].set_title("Graph 3 title")

axes[1,1].plot(u,u**4,color="purple")         
axes[1,1].set_title("Graph 4 title")

mp.tight_layout()       #Sets everything near to border, tidy look
mp.show()

#Pandas + Matplotlib
df=pd.read_csv("data.csv")
t=df["col1"].value_count()
mp.barh(t.index,t.values)  #This shows columns data as index and values as its frequency      
mp.show()

#Animation in plots
import matplotlib.pyplot as mp
import numpy as np
import random
heads_tails=[0,0]       #Initial values of two variables are set to zero
for _ in range(5):      #Upto 5 iterations loop chalega
    heads_tails[random.randint(0,1)]+=1 
    mp.bar(["Heads","Tails"],heads_tails)  #head_tails is called for score addition and variable initialisation and columns are given names
    mp.pause(2)                            #There is pause of 1 sec after each step
mp.show()

