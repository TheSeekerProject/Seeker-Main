import numpy as np
import matplotlib.pyplot as plt
import csv
import argparse

def read_acceleration_data(filename):
    with open(filename, 'r') as input_file:
        csv_reader = csv.reader(input_file)
        header_row = next(csv_reader)
        acceleration_data = []
        for row in csv_reader:
            if len(row) < 3:
                print("Error: File does not contain acceleration data.")
                return None
            try:
                acceleration_data.append([float(row[-3]), float(row[-2]), float(row[-1])])
            except ValueError:
                print("Error: File contains invalid acceleration data.")
                return None
            if len(acceleration_data) >= 1000:
                break
    return np.array(acceleration_data)

# def plot_acceleration_data(acceleration_data, sampling_frequency):
    # # Compute magnitude of acceleration data for each axis
    # magnitude_data_x = np.sqrt(np.sum(np.square(acceleration_data[:, 0]), axis=0))
    # magnitude_data_y = np.sqrt(np.sum(np.square(acceleration_data[:, 1]), axis=0))
    # magnitude_data_z = np.sqrt(np.sum(np.square(acceleration_data[:, 2]), axis=0))

    # # Compute time vector
    # time_vector = np.arange(int(len(magnitude_data_x))) / sampling_frequency


    # # Plot acceleration data for each axis
    # fig, axs = plt.subplots(nrows=3, sharex=True, figsize=(8, 6))
    # axs[0].plot(time_vector, magnitude_data_z)
    # axs[0].set_ylabel('Acceleration Z')
    # axs[1].plot(time_vector, magnitude_data_y)
    # axs[1].set_ylabel('Acceleration Y')
    # axs[2].plot(time_vector, magnitude_data_x)
    # axs[2].set_ylabel('Acceleration X')
    # axs[2].set_xlabel('Time (s)')
    # axs[0].set_title('Acceleration Data')

    # # Perform FFT on acceleration data for each axis
    # fft_data_x = np.fft.fft(magnitude_data_x)
    # fft_data_y = np.fft.fft(magnitude_data_y)
    # fft_data_z = np.fft.fft(magnitude_data_z)

    # # Compute frequency vector
    # frequency_vector = np.fft.fftfreq(len(magnitude_data_x), 1 / sampling_frequency)

   # # Plot FFT data for each axis
    # fig, axs = plt.subplots(nrows=3, sharex=True, figsize=(8, 6))
    # frequency_vector = np.fft.fftfreq(len(magnitude_data_x), 1 / sampling_frequency)
    # positive_frequencies = frequency_vector[:int(len(frequency_vector) / 2)]
    # axs[0].plot(positive_frequencies, np.abs(fft_data_z)[:len(fft_data_z) // 2])
    # axs[0].set_ylabel('FFT Magnitude Z')
    # axs[1].plot(positive_frequencies, np.abs(fft_data_y)[:len(fft_data_y) // 2])
    # axs[1].set_ylabel('FFT Magnitude Y')
    # axs[2].plot(positive_frequencies, np.abs(fft_data_x)[:len(fft_data_x) // 2])
    # axs[2].set_ylabel('FFT Magnitude X')
    # axs[2].set_xlabel('Frequency (Hz)')
    # axs[0].set_title('FFT Data')
    
    # plt.show()
   
def plot_acceleration_data(acceleration_data, sampling_frequency):
    # Extract acceleration data for each axis
    acceleration_data_z = acceleration_data[:, 2]
    acceleration_data_y = acceleration_data[:, 1]
    acceleration_data_x = acceleration_data[:, 0]

    # Compute magnitude data for each axis
    magnitude_data_z = np.abs(acceleration_data_z)
    magnitude_data_y = np.abs(acceleration_data_y)
    magnitude_data_x = np.abs(acceleration_data_x)

    # Compute FFT data for each axis
    fft_data_z = np.fft.fft(acceleration_data_z)
    fft_data_y = np.fft.fft(acceleration_data_y)
    fft_data_x = np.fft.fft(acceleration_data_x)

    # Plot FFT data for each axis
    fig, axs = plt.subplots(nrows=3, sharex=True, figsize=(8, 8))
    time_vector = np.arange(len(fft_data_x)) / sampling_frequency
    axs[0].plot(time_vector, np.abs(fft_data_z)[:len(fft_data_z) // 2])
    axs[0].set_ylabel('FFT Magnitude Z')
    axs[1].plot(time_vector, np.abs(fft_data_y)[:len(fft_data_y) // 2])
    axs[1].set_ylabel('FFT Magnitude Y')
    axs[2].plot(time_vector, np.abs(fft_data_x)[:len(fft_data_x) // 2])
    axs[2].set_xlabel('Time (s)')
    axs[2].set_ylabel('FFT Magnitude X')
    axs[2].set_xlim([time_vector[1000], time_vector[-1]])
    axs[0].set_title('FFT Data for Acceleration')

    plt.show()





def main():
    parser = argparse.ArgumentParser(description='Plot acceleration data and FFT')
    parser.add_argument('input_file', type=str, help='Path to input CSV file')
    parser.add_argument('sampling_frequency', type=int, choices=[100, 200], help='Sampling frequency of the acceleration data (either 100 or 200 Hz)')
    args = parser.parse_args()

    # Read acceleration data from CSV file
    acceleration_data = read_acceleration_data(args.input_file)
    if acceleration_data is None:
        return

    # Plot acceleration data and FFT
    plot_acceleration_data(acceleration_data, args.sampling_frequency)

if __name__ == '__main__':
    # Run some code
    main()