import numpy as np
import matplotlib.pyplot as plt

# Clear console output and close all previous plots (Not applicable in Python directly)
# In Python, there's no equivalent `clc` or `close all` commands, but we can clear outputs in Jupyter notebooks or use plt.close('all') to close all plots.

# Taking user input for frequencies and amplitude
fc1 = float(input('Enter the freq of 1st Sine Wave carrier: '))
fc2 = float(input('Enter the freq of 2nd Sine Wave carrier: '))
fp = float(input('Enter the freq of Periodic Binary pulse (Message): '))
amp = float(input('Enter the amplitude (For Both Carrier & Binary Pulse Message): '))
amp = amp / 2  # Scaling the amplitude

# Time array for 1 second sampled at 1kHz
t = np.arange(0, 1, 0.001)

# Generating the sine wave carriers
c1 = amp * np.sin(2 * np.pi * fc1 * t)  # 1st Carrier Sine wave
c2 = amp * np.sin(2 * np.pi * fc2 * t)  # 2nd Carrier Sine wave

# Plotting the Carrier Waves
plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)
plt.plot(t, c1)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Carrier 1 Wave')

plt.subplot(4, 1, 2)
plt.plot(t, c2)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Carrier 2 Wave')

# Generating the Square Wave message (Binary Pulse)
m = amp * (2 * (np.mod(t * fp, 1) < 0.5))  # Creating a square wave message signal
plt.subplot(4, 1, 3)
plt.plot(t, m)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Binary Message Pulses')

# Modulating the carriers based on the message signal
mm = np.where(m == 0, c2, c1)  # If message is 0, use c2; if message is 1, use c1

plt.subplot(4, 1, 4)
plt.plot(t, mm)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Modulated Wave')

# Show the plots
plt.tight_layout()
plt.show()
