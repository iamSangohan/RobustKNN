from django.test import TestCase

from test_systematique import falsify

# Create your tests here.

"""TESTTT"""

from sklearn.datasets import load_iris
import numpy as np

X, y = load_iris(return_X_y=True)

# Create a list of pairs (x, y) from X and y
data = list(zip(X, y))

# Initialize counters
falsification = 0
certificat = 0
inconnu = 0

# Set the poisoning threshold
seuil_poisoning = 3

# Select 15 random data points
i = 0
data_input = []
while i < 15:
    index = np.random.randint(0, len(data))
    data_input.append(data[index])

    # Remove the selected data point from the list
    data.pop(index)

    i += 1

# Classify each data point
for element in data_input:
    print(element)
    result = falsify.main(data, seuil_poisoning, element[0])
    if result == 'Falsified':
        falsification += 1
    elif result == 'Certified':
        certificat += 1
    else:
        inconnu += 1

# Print the results
print('Falsified:', falsification)
print('Certified:', certificat)
print('Unknown:', inconnu)