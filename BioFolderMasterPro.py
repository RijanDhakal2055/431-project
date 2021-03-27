import os

def main():
    list_of_files = os.listdir()
    list_of_files.remove('BioFolderMasterPro.py') # This makes it  so that the code won't count itself
    print(list_of_files)

main()