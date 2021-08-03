#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

fn='data.txt'
r=np.genfromtxt(fn,unpack=True)
print(r)
plt.hist(r,bins=[5.1,5.2,5.3,5.4,5.5])
plt.xlabel(r"R ($\Omega$)")
plt.show()
