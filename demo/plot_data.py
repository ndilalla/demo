import os
import matplotlib.pyplot as plt

from demo import DEMO_DATA
from demo.utils.load_file import load_file

file_path = os.path.join(DEMO_DATA, 'example.txt')
x, y, dy = load_file(file_path)

plt.figure('Figure name')
plt.errorbar(x, y, dy, fmt='o', label='Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()