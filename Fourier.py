import numpy as np;
from math import *;
from matplotlib import pyplot as plt;
from matplotlib.animation import FuncAnimation;

#custom integrator that uses the riemann summation technique to integrate any function
class ConvertToFourierSeries:
    a = 10;
    fineness = 1000; #0 is the left limit of the box and x=a is the right limit of the box
    num = 50; #Increase this for a more accurate plot. IDenotes the maximum number of sine functions
    exponentConst = 1;
    timeLimit = 1;
    timeDelay = 0.1; #waits for this much seconds each frame
    timeSamples = int(ceil(timeLimit/timeDelay));
    x = np.linspace(0,a,ceil(a*fineness));
    xPoints = np.linspace(0,a,ceil(a*100));
    cn = [0]*(num+1); #cn[i] stores the coeffecients corresponding to sin((i*pi/a)x), or the (i-1)th excited
            #state of the wavefunction 
    orig = []; #original function's y values
    def __init__(self,a,func,num = 50,fineness = 1000) -> None:
        self.a = a;
        self.fineness = fineness;
        self.num = num;
        self.cn = [0]*(self.num+1);
        self.xPoints = np.linspace(0,self.a,ceil((self.a)*100));
        self.x = np.linspace(0,self.a,ceil(self.a*self.fineness));
        self.CalculateAllCoeffecients(func);
        self.orig = [];
        for i in self.xPoints:
            self.orig.append(func(i));
        #self.func = func;
    #general function to integrate things, can be used without instantiating object
    def Integrate (func, xlimL,xlimR,fineness = 1000):
        #func is a function of one variable, that returns a floating point value
        x = np.linspace(xlimL,xlimR,ceil((xlimR-xlimL)*fineness));
        #generates the points to run the function on while integrating through the 
        #riemann sum method. fineness increases the accuracy, default deltaX is 0.001 at fineness = 1000
        sum = 0; 
        for i in x:
            #for each value in x, I compute the area of the rectangle
            sum += (func(i)/fineness);

        return sum; #then return the sum of the total areas
    
    #special integration with effeciency improved for multiple integrations over same period
    def Integrate(self, func1): 
        sum = 0; 
        for i in self.x:
            #for each value in x, I compute the area of the rectangle
            sum += (func1(i)/self.fineness);
        return sum;       

    def CalculateNthCoeffecient(self,func,n):
        sum = 0; 
        for i in self.x:
            #for each value in x, I compute the area of the rectangle
            sum += (func(i)*sin((n*pi*i)/self.a)/self.fineness);
        sum *= sqrt(2/self.a); 
        self.cn[n] = sum;

    #Calculate all the coeffecients required for the expansion
    def CalculateAllCoeffecients(self,func):
        for i in range(1,self.num+1):
            self.CalculateNthCoeffecient(func,i);

    def initialFunction(self,x):
        ans = 0;
        for i in range(0,self.num):
            ans += self.cn[i]*sin((pi*i*x)/self.a)
        ans *= sqrt(2/self.a);
        return ans;
   
    def createPlotInitial(self):
        y = [];
        for i in self.xPoints:
            y.append(self.initialFunction(i));
        # for i in range(0,self.timeSamples):
        #     for j in range(0,len(self.xPoints)):
        #         self.Re[i][j] = self.RealPart(self.xPoints[j]);
        #         self.Comp[i][j] = self.ImaginaryPart(self.xPoints[j]);
        fig, ax = plt.subplots();
        originalFunction, = ax.plot(self.xPoints,self.orig,'r--'); originalFunction.set_label("original function");
        fourierSeriesFunc, =  ax.plot(self.xPoints,y,'g'); fourierSeriesFunc.set_label("fourier series");

        plt.xlabel("x value",color='blue');
        plt.ylabel("y value",);
        ax.legend();
        plt.show();


def f(x):
    if(x == 0):
        return 1;
    return sin(x)/x;
def g(x):
    if(x < 5):
        return sin(x);
    else:
        return 0;
a = 10;
obj1 = ConvertToFourierSeries(a,f,70,2000); #create an object like this
obj2 = ConvertToFourierSeries(a,g,70,2000);
#a is the endpoint of the graph, for the function and its fourier series (Calculated through the wavefunction method)
#f is the function itself
#the 'num' variable denotes the number of terms in the expansion, since there can't be infinite
#finally, fineness denotes the accuracy of the integral in the custom integration done using riemann sums
#the riemann sums take a small width rectangle and add the areas to find the integral, hence higher fineness = higher accuracy of the coeffecients
obj1.createPlotInitial();
obj2.createPlotInitial();
