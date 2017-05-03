"""
author: Fang Ren (SSRL)

5/3/2017
"""
import numpy as np
import matplotlib.pyplot as plt

Q = np.arange(0.5, 6, 0.01)
chi = np.arange(-60, 60, 1)

cake = np.zeros((len(chi), len(Q)))

def isTextured(a, b, c):
    if a >= 66:
        return True
    else:
        return False

for

Q, chi = np.meshgrid(Q, chi)
plt.pcolormesh(Q, chi, cake)
plt.xlabel('Q')
plt.ylabel('ch')
plt.show()