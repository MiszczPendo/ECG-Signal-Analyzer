import wfdb
import numpy as np
import matplotlib.pyplot as plt

# Importing data from file
signals, fields = wfdb.rdsamp("data/100")
fs = fields["fs"]

### IN FUTURE: ADD OPTION TO VIEW DESCRIPTION FOR CHOSEN MEASUREMENT METHOD
# Choosing MLII measurement method (+ electrode on the left hand and - electrode on the right foot)
ecg_signal = signals[:, 0]

# Setting x axis size in seconds (whole file is 30:06 long)
seconds = 10

# Plotting ECG signal
plt.plot(ecg_signal)
plt.title('Wykres EKG')
plt.xlabel('Czas [s]')

# Fixing x axis labels (from ticks to seconds)
plt.xlim(0, fs * seconds)
x_ticks = np.linspace(0, seconds * fs, seconds + 1)
x_labels = np.arange(0, seconds + 1)
plt.xticks(x_ticks, x_labels)

plt.ylabel(f"Amplituda [mV]")
plt.ylim(-2, 2)
plt.show()