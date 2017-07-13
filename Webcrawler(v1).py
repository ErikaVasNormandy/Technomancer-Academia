import os
import subprocess

#takes a string and checks to see if it exists in the directory
def create_project_dir(directory):
    if os.path.exists(directory):
        print("Directory Already Exists")
    else:
        os.mkdir(directory)
        subprocess.call('ls')


def main():
    print "slow down"
    create_project_dir('redditfrontpage')

if __name__=="__main__":
    main();
