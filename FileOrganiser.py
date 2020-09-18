# importing the required libraries
import os
import sys
import shutil
import ntpath

# Dictionary to store the types of extenions key ( Folder name)  : Value (Extension Type)
DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd", ".jfif"
               ],
    "FILE": ["File"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"
               ],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"
                  ],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"
                 ],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"
              ],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"],
    "JS": ["javaScript File"],
    "torrent": ["TORRENT File"],
    "JSON": ["JSON File"]
}
FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}


#  Function to organize the files as per extension.
def OrganizeByExtension():
    #   returns the Current Working Directory(CWD) of the file.
    inputFilePath = os.getcwd()
    for eachFile in os.scandir():
        if not eachFile.is_dir():
            # storing the path in a variable
            filePath = os.path.abspath(eachFile)
            # storing the extension of file inside a variable
            fileExtension = os.path.splitext(filePath)[1].lower()
            # checking the extension with the File_Formats
            if fileExtension in FILE_FORMATS:
                destParentFolder = os.path.join(inputFilePath, "Organized")
                # checking if the directory is present if not then
                # creating the directory named as Organized
                if not os.path.exists(destParentFolder):
                    os.mkdir(destParentFolder)
                # creating the new folders as naming
                # inside the dictionary above
                destFolder = os.path.join(
                    destParentFolder, FILE_FORMATS[fileExtension])
                # checking if already present
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                # moving the file to the created directory
                shutil.copy2(filePath, destFolder)
                Destination = os.path.join(destFolder, eachFile)
                # removing the older path of file
                if os.path.exists(Destination):
                    os.remove(filePath)


# Function to organize the files as per Alphabetical Order.
def OrganizeByAlphabet():
    # gets the present directory path
    inputFilePath = os.getcwd()
    for eachFile in os.scandir():
        if not eachFile.is_dir():
            #  gets the path of each file inside the directory
            filePath = os.path.abspath(eachFile)
            # creating a new directory named Organized
            destParentFolder = os.path.join(inputFilePath, "Organized")
            # checking if the directory already exists
            # if not then create the directory named as Organized
            if not os.path.exists(destParentFolder):
                os.mkdir(destParentFolder)
            # code for checking each file by the alphabets
            # pylint: disable=unused-argument
            _, tail = ntpath.split(filePath)
            # head = head+1
            alp = tail[0].upper()
            destFolder = os.path.join(destParentFolder, alp)
            # making new directory according to the alphabet
            if not os.path.exists(destFolder):
                os.mkdir(destFolder)
            #  moving the files to the new directory created
            shutil.copy2(filePath, destFolder)
            Destination = os.path.join(destFolder, eachFile)
            # removing the old file path
            if os.path.exists(Destination):
                os.remove(filePath)


# Function to organize the files as per size of the Files.
def OrganizeBySize():
    inputFilePath = os.getcwd()
    for eachFile in os.scandir():
        if not eachFile.is_dir():
            filePath = os.path.abspath(eachFile)
            # the size of the file in bytes.
            size = os.stat(eachFile).st_size
            destParentFolder = os.path.join(inputFilePath, "Organized")
            if not os.path.exists(destParentFolder):
                os.mkdir(destParentFolder)
            # For the files sized in Bytes
            if 0 <= size < 1000:
                destFolder = os.path.join(destParentFolder, "BYTES")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath, destFolder)
                Destination = os.path.join(destFolder, eachFile)
                if os.path.exists(Destination):
                    os.remove(filePath)
            # For the files sized in KB's only
            elif 1000 < size < 1000000:
                destFolder = os.path.join(destParentFolder, "KB")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath, destFolder)
                Destination = os.path.join(destFolder, eachFile)
                if os.path.exists(Destination):
                    os.remove(filePath)
            # For the files size uptil 100 MB
            elif 1000000 < size < 100000000:
                destFolder = os.path.join(destParentFolder, "100MB")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath, destFolder)
                Destination = os.path.join(destFolder, eachFile)
                if os.path.exists(Destination):
                    os.remove(filePath)
            # For files size uptil 500 MB
            elif 100000000 < size < 500000000:
                destFolder = os.path.join(destParentFolder, "500MB")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath, destFolder)
                Destination = os.path.join(destFolder, eachFile)
                if os.path.exists(Destination):
                    os.remove(filePath)
            # For files more than a GB
            elif size > 1000000000:
                destFolder = os.path.join(destParentFolder, "GB")
                if not os.path.exists(destFolder):
                    os.mkdir(destFolder)
                shutil.copy2(filePath, destFolder)
                Destination = os.path.join(destFolder, eachFile)
                if os.path.exists(Destination):
                    os.remove(filePath)


if __name__ == '__main__': # Taking the input from Command line using Command line parsing.
    if len(sys.argv) == 1:
        OrganizeByAlphabet()
    elif len(sys.argv) == 2:
        Organize = sys.argv[1]
        if Organize == "ext":
            OrganizeByExtension()
        elif Organize == "size":
            OrganizeBySize()
        elif Organize == "alpha":
            OrganizeByAlphabet()