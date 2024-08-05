import csv
import wave
import numpy as np
from src.arguments import parse_arguments
    
def get_sample_rate(time_values):
    time_diff = np.diff(time_values)
    sample_rate = 1 / np.mean(time_diff)
    return int(sample_rate)

def main():
    args = parse_arguments()
    # get file name
    file_name = args.input_file
    output_file = args.output_file
    time_field = args.time_field
    value_field = args.value_field
    
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        fields = reader.fieldnames

    column_dict = {field: [] for field in fields}
            
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for field in fields:
                column_dict[field].append(float(row[field]))

    time_values = np.array(column_dict[fields[time_field]])
    values = np.array(column_dict[fields[value_field]])
    normalized_values = np.int16(values / np.max(np.abs(values)) * 32767)

    sample_rate = get_sample_rate(time_values)
    print(f"Sample rate: {sample_rate}")
    
    with wave.open(output_file, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(normalized_values.tobytes())
    
if __name__ == "__main__":
    main()