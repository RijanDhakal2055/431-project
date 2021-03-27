import os # one of the libraries that I needs

def main():
    list_of_files = os.listdir() # this make a list of the files in the main folder
    list_of_files.remove('BioFolderMasterPro.py') # This makes it  so that the code won't count itself
    print(list_of_files) # just testing for now

main()