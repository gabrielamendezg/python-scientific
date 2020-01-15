"""
==================
HolaMundo
==================

Un Holamundo de Data Science tiene que tener,

¿ Cómo leer un archivo y cargar un dataset ?
¿ Cómo ploter la info para arrancar un análisis exploratorio ?


"""
print(__doc__)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Frecuencia de sampleo 128 Hz

print('Hello Python Scientific World')

print('Objetivo: leer tensores y poder plotear sus valores...')

signals = pd.read_csv('data/blinking.dat', delimiter=' ', names = ['timestamp','counter','eeg','attention','meditation','blinking'])

print('Estructura de la informacion:')
print(signals.head())

print('Filtrar segun informacion especifica:')
print(signals[signals.counter > 45])

data = signals.values

print('Ahora tienen un tensor de numpy (data)')
print (data)

print('Forma %2d,%2d:' % (signals.shape))

print('Python slicing...[:,].  El \':\' sirve para indicar el rango desde hasta.  Los indices son posiciones segun la forma del tensor.')
eeg = data[:,2]

print(eeg)

# Ojo con el filtro OR.
eeg[eeg>50]
eegfiltered = np.logical_or(eeg>10,eeg<-40) 



#t = np.linspace(-0.02, 0.05, 1000)
#plt.plot(t, 325 * np.sin(2*np.pi*50*t));
plt.plot(eeg,'r', label='EEG')
plt.xlabel('t');
plt.ylabel('eeg(t)');
#plt.title(r'Plot of CT signal $x(t)=325 \sin(2\pi 50 t)$');
plt.title(r'EEG Signal')
plt.ylim([-2000, 2000]);
plt.xlim([0,len(eeg)])
plt.show()

import seaborn as sns
sns.set(style="darkgrid")
sns.lineplot(x="timestamp", y="eeg", hue="attention", data=signals)
import matplotlib.pyplot as plt
plt.show()



# ¿ Qué pueden hacer ? 

# 1- Verifiquen que el campo counter en el archivo es consecutivo.  Este campo está asociado
# a la frecuencia de sampleo del dispositivo.  Si todos los número están presentes entonces está ok.

# 2- Traten de identificar los picos.

