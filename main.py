from pyscript import display # type: ignore
import numpy as np
import matplotlib
matplotlib.use('Agg')  # type: ignore
import matplotlib.pyplot as plt

display(f"Testing, hello world!", target="output")

test_array = np.array([1, 2, 3])
display(f"NumPy is working! Array: {test_array}", target="output")