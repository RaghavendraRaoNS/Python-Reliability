# -*- coding: utf-8 -*-
"""Reliability analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g9ZbO1tZM3QQdPoEbP-fa6BsZWmn9brk
"""

import numpy as np
import matplotlib.pyplot as plt
def plotter(lam, hour):
    t = np.arange(0,hour+0.1,0.1)
    reliability = np.exp(-lam*t)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 0.9)
    ax.grid(which='major', color='black', linestyle='--')
    ax.grid(which='minor', color='black', linestyle=':')
    plt.plot(t,reliability,'-',label='Reliability')
    csfont={'fontname':'Times New Roman'}
    plt.xlabel('years', fontsize=20.0, fontweight='bold')
    plt.xlabel('years',**csfont)
    plt.ylabel('Failure Rate', fontsize=20.0, fontweight='bold')
    plt.ylabel('Failure Rate',**csfont)
    plt.legend(prop={'size': 12})
    plt.tick_params(labelsize=12, pad=0);
    plt.tight_layout()
plotter(0.154,15)
plt.savefig("sa.tif", dpi=100)