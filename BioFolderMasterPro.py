import os # one of the libraries that I needs

def main():
    top =os.getcwd()
    print(top)
    #exclude = set(['.git'])
    for root,dirs, files in os.walk(top,topdown=False): # this make a list of the files in the main folder
        #dirs[:] = [d for d in dirs if d not in exclude]
        print(files)
main()