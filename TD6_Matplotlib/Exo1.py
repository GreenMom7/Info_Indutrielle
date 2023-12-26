import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 4*np.pi, 0.02)

cosin = np.cos(t)
ex = np.exp(-t)*np.cos(t)
#sinc = (np.sin(t))/t
#plt.axis([0, 4*np.pi, -0.5, 1])
#plt.plot(t,cosin)
plt.figure(figsize=(9, 3))
plt.subplot(211)
plt.plot(t,ex)
plt.subplot(212)
plt.plot(t,np.sinc(t))
plt.suptitle('les fonctions')
plt.show()
