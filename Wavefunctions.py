import numpy as np;
from math import *;
from matplotlib import pyplot as plt;
from matplotlib.animation import FuncAnimation;
import matplotlib.animation as animationFunctions;


#if saving is needed then write location here.
saveLocation = r"D:\OneDrive - IIT Delhi\Pictures\_PythonProjects\Wavefunctions\Animations of Wavefunction\CentredAt1at32_35.gif";
        # set the above save location correctly otherwise animation might not work


class MyQuantumBox:
    fineness = 1000; #0 is the left limit of the box and x=a is the right limit of the box
    num = 50; #the maximum n it will go to with sine functions
    exponentConst = 1;
    timeLimit = 5;
    timeDelay = 0.05; #waits for this much seconds each frame
    timeSamples = int(floor(timeLimit/timeDelay));
    #x = np.linspace(0,a,ceil(a*fineness));
   # xPoints = np.linspace(0,a,ceil(a*100));
    originalYval = [];
    cn = [0]*(num+1); #cn[i] stores the coeffecients corresponding to sin((i*pi/a)x), or the (i-1)th excited
            #state of the wavefunction 
    t = np.linspace(0,timeLimit,timeSamples);
    #func = function;
    RealPart = []; 
    ImaginaryPart = [row[:] for row in RealPart]; 
    Modulus = [row[:] for row in RealPart]; 
    maxUpperYbound = 0;
    def __init__(self,a,func,timeLimit = 5, speed = 20, num = 50,fineness = 1000) -> None:
        self.a = a;
        self.fineness = fineness;
        self.num = num;
        #self.func = func;
        self.timeLimit = timeLimit;
        self.timeSamples = int(floor(timeLimit/self.timeDelay));
        self.initialise(func,speed);
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
    
    def initialise(self,func, speed=10):
        self.exponentConst = speed*0.0005718734319419223; #for now
        self.cn = [0]*(self.num+1);
        self.xPoints = np.linspace(0,self.a,ceil(self.a*100));
        self.t = np.linspace(0,self.timeLimit,self.timeSamples);
        self.x = np.linspace(0,self.a,ceil(self.a*self.fineness));
        self.CalculateAllCoeffecients(func);
        
        for i in self.xPoints:
            self.originalYval.append(func(i));
        self.RealPart = []; 
        for i in range(0,self.t.size):
            cur = [0]*self.xPoints.size; 
            self.RealPart.append(cur); 
        self.ImaginaryPart = [row[:] for row in self.RealPart]; 
        self.Modulus = [row[:] for row in self.RealPart]; 
        self.CalculateAllPartsForTime();

        
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
    def RealPartFunction(self,x,t):
        ans = 0;
        for i in range(0,self.num):
            ans += self.cn[i]*sin((pi*i*x)/self.a)*cos(self.exponentConst*t*(i**2));
        ans *= sqrt(2/self.a);
        return ans;
    #anim = FuncAnimation(fig,AnimateFrames,frames=t,init_func=init, blit=True);
    def ImaginaryPartFunction(self,x,t):
        ans = 0;
        for i in range(0,self.num):
            ans += self.cn[i]*sin((pi*i*x)/self.a)*sin(-self.exponentConst*t*(i**2));
        ans *= sqrt(2/self.a);
        return ans;

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
    
    # RealPart = []; 
    # for i in range(0,t.size):
    #     cur = [0]*xPoints.size; 
    #     RealPart.append(cur); 
    # ImaginaryPart = [row[:] for row in RealPart]; 
    # Modulus = [row[:] for row in RealPart]; #effectively deep copies
    
    #now we must calculate the real part of the function as well as the imaginary part of the function at different 
    #input times in the numpy list t
    def CalculateAllPartsForTime(self):
        # print(len(self.RealPart));
        # print(len(self.RealPart[0]));
        for i in range(0,self.t.size):
            #for all of the times calculate the values
            for j in range(0, self.xPoints.size):
                self.RealPart[i][j] = self.RealPartFunction(self.xPoints[j],self.t[i]);
                self.ImaginaryPart[i][j] = self.ImaginaryPartFunction(self.xPoints[j],self.t[i]);
                self.Modulus[i][j] = sqrt(self.RealPart[i][j]**2 + self.ImaginaryPart[i][j]**2);
                if(self.Modulus[i][j] > self.maxUpperYbound):
                    self.maxUpperYbound = self.Modulus[i][j]; 
                # if(self.Modulus[i][j] < self.maxLowerYBound):
                #     self.maxLowerYBound = self.Modulus[i][j];
        
    def DisplayAnimation(self):
        fig, ax = plt.subplots(); fig.set_size_inches(10,6);
        ax.set_xlim(0,a); ax.set_ylim(-self.maxUpperYbound*1.1,self.maxUpperYbound*1.1);

        line = ax.plot(self.xPoints,self.RealPart[0][:],color = 'k', lw=1, label = "Real Part Re(Psi)")[0];
        ModLine = ax.plot(self.xPoints,self.Modulus[0][:],color = 'r', lw=2,label="|Psi|")[0];
        ImLine = ax.plot(self.xPoints,self.ImaginaryPart[0][:],color = 'b', lw=1, label="Imaginary part Im(Psi)")[0];
        def animate(i):
            line.set_ydata(self.RealPart[i][:]);
            ModLine.set_ydata(self.Modulus[i][:]);
            ImLine.set_ydata(self.ImaginaryPart[i][:]);
        originalFunction, = ax.plot(self.xPoints,self.originalYval,'b--', label="Psi at T=0");
        ax.legend();
        anim = FuncAnimation(fig,animate, interval = self.timeDelay*1000, frames=len(self.t)-1);
        
        #for some reason, the r must be placed in front of the path

        Writer = animationFunctions.FFMpegWriter(fps=30);
        anim.save(saveLocation,writer='imagemagick');
        plt.draw();
        plt.show();

        
a = 4;
def f(x):
    a = 0; b = 1;
    if(a <= x <= b):
        return sqrt(2/(b-a))*sin((x-a)*pi/(b-a));
    else:
        return 0;
def CentredAt1(x):
    a = 0.85; b = 1.15;
    if(a <= x <= b):
        return sqrt(2/(b-a))*sin((x-a)*pi/(b-a));
    else:
        return 0;
def equalEverywhere(x):
    return 1/a;
def sinc(x):
    start = 0; end = a;
    if(start < x <= end):
        return sin(pi*x)/x;
    else:
        return 0;
box1 = MyQuantumBox(a,CentredAt1,40,32,400,10000);
#box1.initialise(CentredAt2,20);
box1.DisplayAnimation();
