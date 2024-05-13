import struct
import csv
import numpy as np


def decode_pear_data(binary_path, output_csv_path, header_offset=0, trailer_offset=0):
    """
    Decodes the binary data for the 'pear' dataset into CSV format, skipping header and trailer data.

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

    # The size of each record (pair of integers) is 8 bytes
    record_size = 8

    # Determine the number of pairs
    num_pairs = len(binary_data) // record_size

    # Decode binary data into (time, intensity) pairs
    decoded_data = [
        struct.unpack('<ii', binary_data[i*record_size:(i+1)*record_size])
        for i in range(num_pairs)
    ]

    # Write decoded data to the output CSV file
    with open(output_csv_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Time (ms)', 'Intensity'])
        writer.writerows(decoded_data)



if __name__ == "__main__":
    # 320 bytes to skip at the start and 480 at the end
    header_bytes_to_skip = 320
    trailer_bytes_to_skip = 480
    decode_pear_data('Data/pear', 'decoded_pear.csv', header_offset=header_bytes_to_skip, trailer_offset=trailer_bytes_to_skip)