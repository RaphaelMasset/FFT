import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('sin_values.csv')

# Extract the 'x' and 'sin(x)' columns
x_values = data['x']
sin_values = data['sin(x)']

# Apply FFT to the sin(x) values
fft_values = np.fft.fft(sin_values)

# Compute the corresponding frequencies
frequencies = np.fft.fftfreq(len(x_values), d=(x_values[1] - x_values[0]))  # Assuming uniform spacing of x

# Plot the original sin(x) data
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(x_values, sin_values, label='sin(x)')
plt.title('Original sin(x) Values')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid()

# Plot the magnitude of the FFT
plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(fft_values), label='FFT Magnitude', color='r')
plt.title('FFT of sin(x) Values')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid()

plt.tight_layout()
plt.show()