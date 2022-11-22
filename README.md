# Quantum-Wavefunctions
Modeled the time evolution of Quantum wavefunctions using custom integrator with riemann sums and solving for fourier coeffecients for any initial wavefunction inside a 1D box. Using Matplotlib for graphing the outputs. all the functions are inside the class "MyQuantumBox" and hence any number of plots can be made by just instantiating different objects of the class with different parameters and initial wavefunctions. 

![Constanim25At32](https://user-images.githubusercontent.com/96519848/203317049-0c6fdc79-e64f-4e3a-a205-5b4c45e2e6f1.gif)
 **A simple animation of a case where the initial particle was close to the center of the box and its wavefunction was distributed as a sine wave.**

Notice how in this above animation, the wavefunction periodically goes through all of the stationary states of the box, with 5 peaks, 4 peaks, 3 peaks, 2 peaks etc. When the particle would be "measured" then its wavefunction will simply collapse into one of those stationary states, with probabilities given by their coeffecients in the original expansion of the initial wavefunction.



I got interested in making this because of a question I found while studying for my quantum mechanics course PYL100 at IITD. 
**The question was asked what would happen to a particle when initially it was in a 1D box of length = 'a' in the ground state, and then the size of the box suddenly changes to size '4a'. We had to then find the probability of it being in a particular stationary state of the new box on measurement.**
Here is the animation of the above question.
![leftanim25At250](https://user-images.githubusercontent.com/96519848/203319156-19569940-a536-415e-a56b-74515ab5e80b.gif)

The question itself is easy if you know how to write a wavefunction in a sum of stationary solutions of the '4a' box. But I was interested in how the wavefunction itself would evolve with time in this type of arrangement, and hence I made an animation of it on desmos which you can play here https://www.desmos.com/calculator/rg8yslb1ho
So I wanted to then make a program that can show the time evolution of any initial wavefunction inside a box (and maybe even in other potential systems later)

# **Some Other Animations**
![equalEverywhere4](https://user-images.githubusercontent.com/96519848/203326853-de3455e7-1aa1-4df0-9321-113dd8ecd3ef.gif)
                             **Here Initial wavefunction is equal everywhere. Also, a lot of Noise persists since the series isn't upto infinity**

![ais10](https://github.com/DhruvAhlawat/Quantum-Wavefunctions/blob/main/ais10AndCenteredAt5.gif)
**similar to the first wavefunction, but with a larger length of the box**

![ais10Assymetric](https://github.com/DhruvAhlawat/Quantum-Wavefunctions/blob/main/ais10AndCenteredAt25.gif)
**similar to the wavefunction described just above, but initial position is not in the center**
