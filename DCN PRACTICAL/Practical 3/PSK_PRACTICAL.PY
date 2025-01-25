import numpy as np
import matplotlib.pyplot as plt

# Parameters
bit_rate = 1   # Bit rate (bps)
fc = 5         # Carrier frequency (Hz)
amplitude = 1  # Amplitude of the signal
fs = 100       # Sampling frequency (samples per second)
duration = 1   # Duration of each bit in seconds

# Generate a random bit sequence
data = np.random.choice([0, 1], size=8)  # 8-bit sequence
print("Transmitted data:", data)

# Time array for one bit duration
t_bit = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Generate BPSK signal
bpsk_signal = np.array([])
for bit in data:
    # Phase shift of 0 for bit '1' and π for bit '0'
    phase = 0 if bit == 1 else np.pi
    signal = amplitude * np.sin(2 * np.pi * fc * t_bit + phase)
    bpsk_signal = np.concatenate((bpsk_signal, signal))

# Time array for the full signal
t = np.linspace(0, len(data) * duration, len(bpsk_signal), endpoint=False)

# Plot the data and BPSK signal
plt.figure(figsize=(12, 6))

# Plot the bit sequence
plt.subplot(2, 1, 1)
plt.step(range(len(data)), data, where='post', color='blue', label='Input Data')
plt.ylim(-0.5, 1.5)
plt.xlabel("Bit Index")
plt.ylabel("Bit Value")
plt.title("Input Data")
plt.grid()
plt.legend()

# Plot the BPSK signal
plt.subplot(2, 1, 2)
plt.plot(t, bpsk_signal, color='red', label='BPSK Signal')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("BPSK Modulated Signal")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
