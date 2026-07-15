import datetime
import os
import sys


dir_idx = -1
file_idx = -1
file = ""

if "-d" in sys.argv:
    dir_idx = sys.argv.index("-d")
if "-f" in sys.argv:
    file_idx = sys.argv.index("-f")
    file = sys.argv[file_idx + 1]

dirs = []
if dir_idx > -1:
    if file_idx > -1:
        if dir_idx < file_idx:
            dirs = sys.argv[dir_idx + 1:file_idx]
        else:
            dirs = sys.argv[dir_idx + 1:]
    else:
        dirs = sys.argv[dir_idx + 1:]

if dirs:
    os.makedirs(os.path.join(*dirs))
if file:
    file_contents = ""
    line_num = 1
    while True:
        file_input = input("Enter content line: ")
        if file_input == "stop":
            break
        else:
            file_contents = f"{file_contents}{line_num} {file_input}\n"
            line_num += 1
    with open(os.path.join(*dirs, file), "a") as f:
        f.write(f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")
        f.write(f"{file_contents}")
