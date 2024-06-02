import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def test_for_mac(x):
    if x == 'max':
        print('this is test for mac')
    else:
        print('hello world')


if __name__ == "__main__":
    input_text = 'mac'
    test_for_mac(input_text)
