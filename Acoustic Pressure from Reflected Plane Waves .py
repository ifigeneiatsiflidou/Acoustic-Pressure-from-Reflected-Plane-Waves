# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Given parameters
c = 350                 # Speed of the acoustic plane wave (m/s)
f = 500                 # Frequency (Hz)
x1 = -4                 # Distance 1 from the reflection surface (m)
x2 = -7                 # Distance 2 from the reflection surface (m)
A_1 = 1                 # Amplitude of the incident wave
R = -0.5 * np.exp(0.3j) # Reflection coefficient (complex)

# Derived parameters
T = 1/f             # Period (s)
l = c/f             # Wavelength (m)
omega = 2*np.pi*f   # Angular frequency (rad/s)
k = 2*np.pi/l       # Wavenumber (1/m)

# Time array over 3 periods
time = np.linspace(0, 3 * T, 1000)  # From 0 to 3 periods

# Amplitude of the reflected wave
A_2 = A_1 * R

# Acoustic pressures at x1
p_x1_1 = A_1 * np.exp((k * x1 + omega * time)*1j)       # Incident wave
p_x1_2 = A_2 * np.exp((k * x1 + omega * time)*1j)       # Reflected wave
p_x1_total = p_x1_1 + p_x1_2                            # Total wave

# Acoustic pressures at x2
p_x2_1 = A_1 * np.exp((k * x2 + omega * time)*1j)
p_x2_2 = A_2 * np.exp((k * x2 + omega * time)*1j)
p_x2_total = p_x2_1 + p_x2_2

# -- Plots for x1 and x2 --
plt.figure()

# At distance x1
plt.subplot(2, 1, 1)
plt.plot(time, np.real(p_x1_1))
plt.plot(time, np.real(p_x1_2))
plt.plot(time, np.real(p_x1_total))
plt.legend(['Incident', 'Reflected', 'Total'])
plt.title("Acoustic pressure at x₁ = " + str(x1) + " m")
plt.ylabel("Pressure (Pascal)")
plt.grid()

# At distance x2
plt.subplot(2, 1, 2)
plt.plot(time, np.real(p_x2_1))
plt.plot(time, np.real(p_x2_2))
plt.plot(time, np.real(p_x2_total))
plt.legend(['Incident', 'Reflected', 'Total'])
plt.title("Acoustic pressure at x₂ = " + str(x2) + " m")
plt.xlabel("Time (s)")
plt.ylabel("Pressure (Pascal)")
plt.grid()

plt.show()