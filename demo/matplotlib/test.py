import numpy as np
import matplotlib.pyplot as plt

def generate_data():
    X = np.linspace(-3, 3, 200).reshape(200, 1)
    y = 2 ** X + 3 + (np.random.rand(200, 1) - 0.5)
    return X, y

X, y = generate_data()

fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(1,1,1)
ax.scatter(X, y, c= 'r')
ax.plot(X, 2 ** X + 3, c='g', linewidth=2)
plt.show()