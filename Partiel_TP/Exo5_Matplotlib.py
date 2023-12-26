import numpy as np
import matplotlib.pyplot as plt

E = 5
R = 1000
C = 0.001

t = np.arange(0.0, 12, 0.1)

Uc = E*(1-np.exp(-t/(R*C)))
Ud = E*(np.exp(-t/(R*C)))

RC=R*C


plt.figure(1)

plt.subplot(211)
plt.title('charge condensateur')
plt.plot(t,Uc,'r')
plt.plot([0,RC],[0,E], 'k--')
plt.plot([0,12],[E,E], 'k--')
plt.plot([RC,RC],[0,5], 'b')
plt.text(RC, -0.5, 'RC')
plt.grid()

plt.subplot(212)
plt.title('decharge d''un condensateur')
plt.plot(t,Ud,'b')
plt.grid()

# plt.show()

plt.figure(2)
plt.title('charge et decharge d''un condensateur')
plt.plot(t,Uc,'r')
plt.plot(t+12,Ud,'b')
plt.xlabel('temps [s]')
plt.ylabel('Tension [V]')
plt.grid()

plt.show()
