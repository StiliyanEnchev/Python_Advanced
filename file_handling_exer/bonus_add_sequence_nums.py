import os

directory = input('Please enter a directory: ')
number = 0

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)

    if os.path.isfile(file):
        number += 1
        filename_without_path = os.path.basename(file)
        new_name = str(number) + '_' + filename_without_path
        os.rename(file, os.path.join(directory, new_name))