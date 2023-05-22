import os
from demo import DEMO_DATA
from demo.utils.load_file import load_file

def test_load_file():
    file_path = os.path.join(DEMO_DATA, 'example.txt')
    x, y, dy = load_file(file_path)
    print(x, y, dy)