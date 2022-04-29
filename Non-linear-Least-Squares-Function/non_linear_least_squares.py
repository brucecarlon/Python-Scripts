import numpy as np
from scipy.optimize import curve_fit #uses LM algorithm to fit non linear least sq
import matplotlib.pyplot as plt
from statistics import mean

f = open('Damp.txt', 'r')  #assume 0.001m uncert on all pos readings
header = f.readline()

i = 0


tdata, ydata, udata = [], [], []  # time, position and uncertainty
for line in f:
    values = [float(s) for s in line.split()]
    tdata.append(values[0])
    ydata.append(values[1])
    udata.append(0.001)
    
    
tdata = np.array(tdata)
ydata = np.array(ydata) 
    
  
 
def f(t, A, B, gamma, omega, alpha) :
    return A + (B*np.exp(-gamma*t) * np.cos(omega * t - alpha))


# initial guesses

A0 = 0.283
B0= -0.028
gamma0= 0.2812
omega0 =21.46227
alpha0 = 3.470977

p0 = [A0, B0, gamma0, omega0, alpha0] #list of intial guesses
name = ['A', 'B', 'gamma', 'omega', 'alpha']

tmodel = np.linspace(0.0, 5.0, 1000)
ystart = f(tmodel, *p0)


# popt - optimal values for the parameter
# pcov - estimated covariance of popt

popt, pcov = curve_fit(f,tdata,ydata,p0, sigma = udata, absolute_sigma = True)

dymin = (ydata -f(tdata, *popt))/udata #Vectorised
min_chisq = sum(dymin*dymin)   #summation step
dof = len(tdata) - len(popt)   #number of degrees of freedom

perr = np.sqrt(np.diag(pcov))


print('Uncertainty in Parameters', perr)
print('Chi square: ' , min_chisq)  
print('Number of degrees of freedom :' , dof)
print('Chi square per degree of freedom: ' , min_chisq/dof)
print()

#Calculate uncertainty and format for printing

print("Fitted parameters with 68% C.I.:")

for i, pmin in enumerate(popt):
    print("%2i %-10s %12f +/- %10f " %(i, name[i],pmin,np.sqrt(pcov[i,i])*np.sqrt(min_chisq/dof)))
print()

perr = np.sqrt(np.diag(pcov))

print(perr)

# Calculate and print correlation matrix

print("Correlation matrix")
print("     ")
for i in range (len(popt)): print("%-10s " %(name[i] ,)) ,
print()

for i in range(len(popt)):
    print("%10s "%(name[i])),
    for j in range (i+1):
        print( "%10f "%(pcov[i,j]/np.sqrt(pcov[i,i]*pcov[j,j]),)),
    print()    



print(len(tdata))
print(len(ydata))


Npts = 10000
mscan = np.zeros(Npts)
cscan = np.zeros(Npts)
chi_dof = np.zeros(Npts)

i = 0


x_values = tdata
y_values = ydata
print(x_values)


############################################# Line of best
def linearfunc(x,intercept,slope):
    y = slope*x + intercept
    return y

a_fit, cov = curve_fit(linearfunc,x_values,y_values)

inter = a_fit[0]
slope = a_fit[1]

d_inter = np.sqrt(cov[0][1])
d_slope = np.sqrt(cov[1][1])

print(f'the slope = {slope}, with uncertainty{d_slope}')

#################################################################
def best_fit_line(x_values, y_values):
    m = (((mean(x_values)*mean(y_values)) - mean(x_values*y_values))/((mean(x_values)*mean(x_values))-mean(x_values*x_values)))
    b = mean(y_values) - m*mean(x_values)
    
    return m, b


m, b = best_fit_line(x_values,y_values)

print("regreesion line: " + "y = " +str(round(m,6)) + "x +" + str(round(b,6)))

regression_line = [(m*x)+b for x in x_values]

plt.plot(x_values, regression_line, color='000000', label='Regression Line')
yfit = f(tmodel, *popt)   
plt.plot(tmodel,yfit, '-r', color = 'red', label = 'Line Of Best Fit')
plt.xlabel('Time t (s)')
plt.ylabel('Position y (m)')
plt.title('The result of the model fit to the data of oscillator 1')
plt.plot(tdata,ydata, label = 'Data', color = 'blue', marker = 'P' , linestyle = 'none')
plt.legend()
plt.show()
plt.savefig("line.png")