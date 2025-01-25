import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

# Taking user input for frequencies and amplitude
try:
    fc = float(input('Enter the frequency of the Sine Wave carrier (Hz): '))
    fp = float(input('Enter the frequency of the Binary pulse message (Hz): '))
    amp = float(input('Enter the amplitude (for Carrier & Binary Pulse Message): '))
except ValueError:
    print("Invalid input! Please enter numeric values for frequencies and amplitude.")
    exit()

# Time array for 1 second sampled at 1 kHz
t = np.arange(0, 1, 0.001)

# Generating the Carrier Sine Wave
c = amp * np.sin(2 * np.pi * fc * t)

# Plotting the Carrier Wave
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t, c)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Carrier Wave')

# Generating the Square Wave Message (Binary Pulse)
try:
    m = (square(2 * np.pi * fp * t) + 1) / 2  # Normalize to 0 and 1
    m = m * amp  # Scale to amplitude
except Exception as e:
    print(f"Error generating square wave: {e}")
    exit()

# Plotting the Binary Message Pulses
plt.subplot(3, 1, 2)
plt.plot(t, m)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Binary Message Pulses')

# Generating the Amplitude Shift Keyed Wave
try:
    w = c * m
except Exception as e:
    print(f"Error generating ASK signal: {e}")
    exit()

# Plotting the Amplitude Shift Keyed Wave
plt.subplot(3, 1, 3)
plt.plot(t, w)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Amplitude Shift Keyed Signal')

# Show the plots
plt.tight_layout()
plt.show()
