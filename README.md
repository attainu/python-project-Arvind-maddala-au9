Junk file Organizer

•The Primary idea to develop a Junk File Organizer is to simplify the work for a Lazy developer. 
•Think of searching out for food in a loaded fridge at late night food carvings, Developers frustrate the same way when they try to find out the Necessary document in an unorganized folder.
•Just to overcome the manual work to keep the required files in the desired folder, one can use the Junk File Organizer to achieve this. 
•When we run this program in the destination directory, all the files* in that particular directory would be moved to folders of their file types, if they do not exist new Folders with the desired name will be created. Similar action can be performed based on the size of the files and the Starting alphabet of the files.

Approach Used:

Below listed system libraries were imported to handle the files and to get the input in command line interface

import os - to get, create, scan all the files from the directories
import sys - to achieve the list of command line arguments passed to a Python script
import shutil - to move the files from one directory to another
import ntpath - to get the exact path of the file

•	To Organise as per Alphabet of the Files:
Initially, the total files would be accessed from the current directory (os.getcwd())
 and then the files are arranged into their subdirectories, which were created and named according to the first name of the files. All the directories are stored under a root directory named as “Organized”.
•	To Organise as per extension of the Files:
A dictionary was created with “key” as target directory and “values” which comprises the list of extension. The path of the file would be scanned and the extension of the file in the computer directory would be compared to the dictionary comprising of extensions. If matched, then a new directory named Organized would be created and files would be pushed into sub folders created already.
•	To Organise as per size of the Files:
A variable (named “size”) was created to store the size of the file. All the files in particular directory would be scanned and as per the size of the file, they would be moved into the designated sub folders (BYTES, KB, MB, GB), under the root directory “Organized


Instructions to run
The inputs can be given using CLI, you have to paste the fileOrganizer.py file inside that folder where all the junk files are present and then open the CLI and pass the following commands:
	The default format would be: Python “Filename” “Argument name”
•	To organize as per Alphabet		: 	python fileOrganizer.py alpha
•	To organize as per Extension	: 	python fileOrganizer.py ext
•	To organize as per size		: 	python fileOrganizer.py size
The default option was made to “alpha”, If no organizing argument was chosen, the directory would be organized by alphabets
