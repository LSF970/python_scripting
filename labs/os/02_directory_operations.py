import os
import shutil

# # 1. Create Directory

# # Directory
# directory = "test_dir"

# # Path to parent dir
# parent_dir = "C:/Users/Luke"

# # Path
# path = os.path.join(parent_dir, directory)

# # Create the DIR
# os.mkdir(path)
# print ("Directoy '% s' created"  % directory)

# # Make a file in the directory
# filepath = os.path.join(parent_dir,)
# # 2. Delete Directory
# os.rmdir('empty_dir_path') # for empty directories
# shutil.rmtree('dir_path') # for non-empty directories. Note this requires shutil module. Not in os

# 3. List Directory
arr = os.listdir()
print(arr)

# 4. List total number of folder in a Directory#
howmany = len(os.listdir('C:/Users/Luke'))
print('Directory count:', howmany)

# 5. List total numbers of files in a Directory
# folder path
dir_path = r'C:/Users/Luke'
count = 0
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print('File count:', count)