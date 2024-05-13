import struct
import csv
import numpy as np

def decode_scale_data(binary_path, output_csv_path, header_offset=0, trailer_offset=0):
    """
    Decodes the binary data for the 'Scale' dataset into CSV format, skipping header and trailer data.

    :param binary_path: Path to the binary file containing the raw data.
    :param output_csv_path: Path to the CSV file where decoded data will be stored.
    :param header_offset: Number of bytes to skip at the start of the file (default is 0).
    :param trailer_offset: Number of bytes to skip at the end of the file (default is 0).
    """
    with open(binary_path, 'rb') as file:
        # Skip the header by seeking past the header_offset
        file.seek(header_offset)

        # Read the binary data, stopping before the trailer
        binary_data = file.read()[:-trailer_offset] if trailer_offset else file.read()

    # each record size has 23 columns
    # first column is float
    # next 22 columns can be signed or unsigned integers    
    record_size = 92

    # Determine the number of pairs
    num_pairs = len(binary_data) // record_size

    decoded_data = []
    nan_rows = []
    for i in range(num_pairs):
        time_value = struct.unpack('<f', binary_data[i*record_size:(i*record_size)+4])[0]
        if np.isnan(time_value):
            time_value = 0
            nan_rows.append(i)
        row_data = [round(time_value, 5)]
        row_data.extend(struct.unpack('<iiiiiiiiiiiiiiiiiiiiii', binary_data[(i*record_size)+4:(i+1)*record_size]))
        decoded_data.append(row_data)

    # Write decoded data to the output CSV file
    with open(output_csv_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Time (min)","190","200","210","220","230","240","250","260","270","280","290","300","310","320","330","340","350","360","370","380","390","400"])
        writer.writerows(decoded_data)
    
    return nan_rows

if __name__ == "__main__":
    header_bytes_to_skip = 0
    trailer_bytes_to_skip = 0
    nan_rows = decode_scale_data('Data/scale', 'decoded_scale.csv', header_offset=header_bytes_to_skip, trailer_offset=trailer_bytes_to_skip)