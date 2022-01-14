import zipfile as zipfile
import os
import sys

"""
Looks at all files in same directory and zips it into an archive, or asks to overwrite if it already exists.
"""


read = os.scandir('.')
filecount = 0
samefile = 0

for file in os.listdir():
    if 'test.zip' in file:
        overwrite = input('Zip file of the same name exists. Continue adding copies? Y/N\n')
        if overwrite == 'Y' or overwrite == 'y':
            print('Continuing...')
            samefile += 1
            pass
        if overwrite == 'N' or overwrite == 'n':
            print('Quitting.')
            quit()
testzip = zipfile.ZipFile('test.zip', mode='a')
zipfile_contents = zipfile.ZipFile.namelist(testzip)
for entry in read:
    try:
        testzip.write(entry.name)
    except Exception as e:
        print(e)
print('Done.')
if samefile > 0:
    print('Files of the same copy exist. Please check.')