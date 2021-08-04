#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

fn='data.txt'
r=np.genfromtxt(fn,unpack=True)
bins=[5.3,5.4,5.5,5.6]
#print(r)
plt.hist(r,bins=bins)
plt.xlabel(r"R ($\Omega$)")
def bins_labels(bins, **kwargs):
    bin_w = (max(bins) - min(bins)) / (len(bins) - 1)
    plt.xticks(np.arange(min(bins)+bin_w/2, max(bins), bin_w), bins, **kwargs)
    plt.xlim(bins[0], bins[-1])

bins_labels(bins)
plt.show()
