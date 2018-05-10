import numpy as np
import matplotlib.pyplot as plt



def chev(a, b, n, f):
    # compute xs in segment [-1, 1]
    xs = [np.cos((2*i + 1) * np.pi/(2*(n + 1))) for i in range(n + 1)]

    # project to segment [a, b]
    ts = [((a + b) / 2) + (((b - a) / 2) * xs[i]) for i in range(n + 1)]

    return np.poly1d(np.polyfit(ts, f(ts), n))


x = np.arange(0, np.pi, 0.1)
s = chev(0, np.pi, 3, np.cos)
plt.plot(x, s(x))
plt.show()









