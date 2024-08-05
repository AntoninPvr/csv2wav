import csv
import wave
import numpy as np
    
def get_sample_rate(time_values):
    time_diff = np.diff(time_values)
    sample_rate = 1 / np.mean(time_diff)
    return int(sample_rate)

# get file name
file_name = input("Enter the file name (default record.csv): ") or "record.csv"

with open(file_name, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    fields = reader.fieldnames

column_dict = {field: [] for field in fields}
        
with open(file_name, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for field in fields:
            column_dict[field].append(float(row[field]))

# select time field
for i, field in enumerate(fields):
    print(f"{i} - {field}")
time_field = int(input("Enter the field number for time (default 0): ") or 0)

# select value to convert to wav
for i, field in enumerate(fields):
    print(f"{i} - {field}")
value_field = int(input("Enter the field number for value (default 1): ") or 1)

# output wav file
output_file = input("Enter the output file name (default record.wav): ") or "record.wav"

time_values = np.array(column_dict[fields[time_field]])
values = np.array(column_dict[fields[value_field]])
normalized_values = np.int16(values / np.max(np.abs(values)) * 32767)

sample_rate = get_sample_rate(time_values)
print(f"Sample rate: {sample_rate}")
n_channels = 1
sampwidth = 2

with wave.open(output_file, 'w') as wf:
    wf.setnchannels(n_channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(sample_rate)
    wf.writeframes(normalized_values.tobytes())