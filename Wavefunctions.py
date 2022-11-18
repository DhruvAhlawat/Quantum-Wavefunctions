import numpy as np;
from math import *;
from matplotlib import pyplot as plt;
from matplotlib.animation import FuncAnimation;
def f(x):
    if(0 < x <= 20):
        return sin(x)/x;
    if(x == 0):
        return 1;
    else:
        return 0;

#custom integrator that uses the riemann summation technique to integrate any function
class MyQuantumBox:
    a = 10;
    fineness = 1000; #0 is the left limit of the box and x=a is the right limit of the box
    num = 50; #the maximum n it will go to with sine functions
    exponentConst = 1;
    timeLimit = 1;
    timeDelay = 0.1; #waits for this much seconds each frame
    timeSamples = int(ceil(timeLimit/timeDelay));
    x = np.linspace(0,a,ceil(a*fineness));
    xPoints = np.linspace(0,a,ceil(a*100));

    cn = [0]*(num+1); #cn[i] stores the coeffecients corresponding to sin((i*pi/a)x), or the (i-1)th excited
            #state of the wavefunction 
    t = [0]*(timeSamples);
    #func = function;
    
   
    def __init__(self,a,num = 50,fineness = 1000) -> None:
        self.a = a;
        self.fineness = fineness;
        self.num = num;
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
    
    def initialise(self,func):
        self.exponentConst = np.pi*np.pi*1; #for now
        self.cn = [0]*(self.num+1);
        self.xPoints = np.linspace(0,self.a,ceil(self.a*100));
        self.t = np.linspace(0,self.timeLimit,self.timeSamples);
        self.x = np.linspace(0,self.a,ceil(self.a*self.fineness));
        self.CalculateAllCoeffecients(func);
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
    #anim = FuncAnimation(fig,AnimateFrames,frames=t,init_func=init, blit=True);
    def createPlotInitial(self):
        y = [];
        for i in self.xPoints:
            y.append(self.initialFunction(i));
        orig = [];
        for i in self.xPoints:
            orig.append(f(i));
        # for i in range(0,self.timeSamples):
        #     for j in range(0,len(self.xPoints)):
        #         self.Re[i][j] = self.RealPart(self.xPoints[j]);
        #         self.Comp[i][j] = self.ImaginaryPart(self.xPoints[j]);
        plt.plot(self.xPoints,y);
        plt.plot(self.xPoints,orig);
        #plt.plot(self.xPoints,f(self.xPoints));
        plt.show();
        # anim = FuncAnimation(self.fig,self.AnimateFrames,
        #  frames=self.timeSamples,interval = self.timeDelay
        # );
        


a = 10;
box1 = MyQuantumBox(a);
box1.initialise(f);

#xPoints = np.linspace(0,a,ceil(a*100));
plt.xlabel("x coordinate",color='red');
#box1.CalculateAllParts(f);
box1.createPlotInitial();
