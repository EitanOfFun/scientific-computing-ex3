import numpy as np
import matplotlib.pyplot as plt


def chev(a, b, n, f):
    xs = [np.cos((2 * i + 1) * np.pi / (2 * (n + 1))) for i in range(n + 1)]
    ts = [((a + b) / 2) + (((b - a) / 2) * xs[i]) for i in range(n + 1)]

    p = np.poly1d(np.polyfit(ts, f(ts), n))
    x = np.arange(0, np.pi, 0.1)
    plt.plot(ts, f(ts), 'ro')
    plt.plot(x, p(x))
    plt.show()
    return p


def show_p3a():
    xs = [0, np.pi / 4, (3 * np.pi) / 4, np.pi]
    p = np.poly1d(np.polyfit(xs, np.cos(xs), 3))
    x = np.arange(0, np.pi, 0.1)
    plt.plot(xs, np.cos(xs), 'ro')
    plt.plot(x, p(x))
    plt.title("A")
    plt.show()


def show_p3b():
    p = np.poly1d([4 / (np.pi * np.pi * np.pi), - 6 / (np.pi * np.pi), 0, 1])
    x = np.arange(0, np.pi, 0.1)
    plt.plot(x, p(x))
    plt.title("B")
    plt.show()


def show_p3c():
    plt.title("C")
    chev(0, np.pi, 3, np.cos)


def show_p3d():
    p = np.poly1d([-0.5, 0, 1])
    x = np.arange(0, np.pi, 0.1)
    plt.plot(x, p(x))
    plt.title("D")
    plt.show()


# 3
show_p3a()
show_p3b()
show_p3c()
show_p3d()

# 4
# print chev(0, np.pi, 3, np.cos)
# output:
#         3          2
# 0.1471 x - 0.6933 x + 0.09508 x + 0.9912