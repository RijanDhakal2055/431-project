import os

def main():
    list_of_files = os.listdir()
    list_of_files.remove('BioFolderMasterPro.py')
    print(list_of_files)

main()