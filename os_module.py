import os as os

current_working_directory = os.getcwd()
group_id = os.getgid()
user_id = os.getuid()
process_id = os.getpid()
operating_system = os.uname()
print(current_working_directory)
print(process_id)
print(user_id)
print(operating_system, '\n')

path = 'path'
new = 'new'
src, dst = path, new

os.mkdir(path)  # creates a directory
# this can be repeated with os.mkdirs()
#os.remove()  # removes a file
os.removedirs(path)  # recursively removes a directory
os.mkdir(path)
os.rename(src, dst)  # renames and moves a path
os.rmdir(new)  # removes the directory path


os.mkdir(path)  # makes a new folder in wd
os.rename(src, dst)  # renames and moves a folder
os.rmdir(new)  # removes the folder

try:
    filename = 'something.txt'
    f = open(filename, 'r')
    text = f.read()
    f.close()
except IOError:
    print('Problem reading: ' + filename)