from os import listdir
from os.path import isfile, join
from getpass import getpass

path = input("Location of config files: ")
usr = input("Auth username: ")
pwd = getpass("Password: ")

if path[-1] != '/':
    path = path + '/'

f = open(path + "login.conf", "w")
f.write(usr + "\n")
f.write(pwd + "\n")
f.close()

config_files = [f for f in listdir(path) if isfile(join(path, f))]

for fname in config_files:
   f = open(path + fname, "a") 
   f.write("\nauth-user-pass login.conf")
   f.close()

