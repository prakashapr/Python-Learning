### Count how many lines contains crashed
### Find time difference between all all the lines starting with crashed

import re
from datetime import datetime


file_path = 'C:\\Users\\Nithon\\Python-Learning\\files\\logcat.txt'
keyword = 'crashed'
encodings = ['cp1252', 'utf-8', 'latin-1']
timestamp_format = '%m-%d %H:%M:%S.%f'
lines = 0

for encoding in encodings:
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            lines = file.readlines()
        break
    except UnicodeDecodeError:
        print(f"Failed to read with {encoding} encoding, trying next...")
    except Exception as e:
        print(f"Error reading the file with {encoding} encoding: {e}")
        break

if lines is None:
    print("Failed to read the file with all attempted encodings.")
else:
    crashed_lines = []

    for line in lines:
        if keyword.lower() in line.lower():
            crashed_lines.append(line.strip())

    line_count = len(crashed_lines)

    print(f'The word "{keyword}" appeared in {line_count} times in the file.\n')
    for line in crashed_lines:
        print(line )
    for line in crashed_lines:
        data =line[0:17]
        with open(file_path, 'r', encoding=encoding) as file:
            lines = file.readlines()

            timestamps = []

            for line in crashed_lines:

                timestamp_str = line[0:17].strip()

                try:
                    timestamp = datetime.strptime(timestamp_str, timestamp_format)
                    timestamps.append(timestamp)
                except ValueError:
                    print(f"Skipping line with invalid format: {timestamp_str}")

            for i in range(len(timestamps) - 1):
                time1 = timestamps[i]
                time2 = timestamps[i + 1]
                difference = time2 - time1
                print(f"Difference between line {i + 1} and line {i + 2}: {difference}")
            else:
                break


