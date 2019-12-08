import matplotlib.pyplot as plt
import numpy as np

def f(n):
    if n <= 9:
        return (n**2)-7;
    else:
        return (n-10)**2-7;

n = np.arange(0, 99)

plt.stem(n, list(map(f, n)))