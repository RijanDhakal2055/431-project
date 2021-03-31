import os # one of the libraries that I needs

def main():
    top =os.getcwd
    for root,dirs, files in os.walk(top, topdown=False): # this make a list of the files in the main folder
        print(root)
main()