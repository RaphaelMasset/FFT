
import csv
import math

# Define the range and step size
start = 0
end = 100
step = 0.1

# Open a CSV file to write
with open('sin_values.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'sin(x)'])  # Header

    # Generate values
    x = start
    while x <= end:
        writer.writerow([round(x, 1), round(math.sin(x)+math.sin(4*x), 6)])
        x += step

print("CSV file 'sin_values.csv' created successfully.")

'''
With x ranging from 0 to 100 and a step size of 0.1,
 -> sampling frequency is 1/0.1 = 10 Hz

the highest frequency component detectable (based on the Nyquist theorem) is 5 Hz

The function sin(x) has a period of approximately 6.28 (2pi)
The frequency of the sine wave is 1/6.28 ≈ 0.159 Hz

'''