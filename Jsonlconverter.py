
@author: Yasir hussain
"""

import glob



#Path of jsonl file
File_path = input("Path of Directory containing Jsonl files: ")

#path to destination folder for created json files
dest_path=input("Destinataion folder: " )

files = [f for f in glob.glob( File_path + "**/*.jsonl", recursive=True)]

for f in files:

    with open(f, 'rb') as F:
        i = 1
        for row in F:
#saving every line as new json file
            with open(dest_path+"/file-"+str(i)+".json", 'wb') as f:
                print(f)
                f.write(row)
                i+=1
