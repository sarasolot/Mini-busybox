import os
import sys

def echoFunction(command):
    length = len(command)
    new_line = bytes('\n', "utf-8")
    space = bytes(" ", "utf-8")
    if (command[2] == '-n'):
        try:
            for i in range(3,length):
                rc = 0
                line = command[i]
                b_line = bytes(line, "utf-8")
                while rc < len(b_line):
                    rc = rc + os.write(1, b_line[rc:])
                    if(i != length -1):
                        os.write(1,space)
        except Exception as e:
            print ("Error: {}".format(e))
    else:
        try:
            for i in range(2,length):
                rc = 0
                line = command[i]
                b_line = bytes(line, "utf-8")
                while rc < len(b_line):
                    rc = rc + os.write(1, b_line[rc:])
                    if(i != length-1):
                        os.write(1,space)
            os.write(1,new_line)
        except Exception as e:
            print ("Error: {}".format(e))
def pwdFunction():
        currentDirectory = os.getcwd()
        print(currentDirectory)

def mkdirFunction(command):
    if len(command) < 3:
         print('Invalid command', flush = True)
    length = len(command) -2 
    i = 2
    while length != 0:
        path = command[i]
        try:
            os.mkdir(path)
            length = length - 1
            i = i + 1
        except IOError:
            sys.exit(226)
def rmdirFunction(command):
    length = len(command) - 2
    i = 2
    while length != 0:
        path = command[i]
        try:
            os.rmdir(path)
        except IOError:
            sys.exit(196)
        length = length - 1
        i = i + 1
        
def defaultTouch(command):
    length = len(command)
    path = command[length-1]
    open(path,'w')

def touchFunction(command):
    length = len(command)
    if (length < 2 or length > 4):
        sys.exit(156)
    try:
        if os.path.exists(command[length -1]) == True:
            os.utime(command[length-1], None)
        else:      
            defaultTouch(command)
    except Exception:
        sys.exit(156)
def catFunction(command):
    BUFSIZE = 10
    new_line = bytes('\n', "utf-8")
    argc = len (command)
    #print(argc)
    if (argc < 3 or argc > 5):
        sys.exit(255)
    for i in range(2,argc):
        file = command[i]
        try:
            fd1 = os.open(file, os.O_RDWR, 0o644)
            b_msg = os.read(fd1,BUFSIZE)
            rc = 0
            while (rc < len(b_msg)):
                rc = rc + os.write(1, b_msg[rc:])
            while (len (b_msg) != 0):
                b_msg = os.read(fd1,BUFSIZE)
                rc = 0
                while (rc < len(b_msg)):
                    rc = rc + os.write(1, b_msg[rc:])   
        except Exception:
            sys.exit(236)

def mvFunction(command):
    argc = len(command)
    if ( argc != 4):
        sys.exit(216)
    try:
        src = os.path.abspath(command[2])
        des = os.path.abspath(command[3])
        os.rename(src,des)
    except Exception:
        sys.exit(216)

def lnFunction(command):
    argc = len(command)
    if(argc < 4 or argc > 5):
        sys.exit(255)
    try:
        if command[2] == '-s' or command[2] == '--symbolic':
            os.symlink(command[3], command[4])
        else:
            os.link(command[2], command[3])
    except IOError:
        sys.exit(206)

def lsFunction(command):
    new_line = bytes('\n', "utf-8")
    argc = len(command)
    if(argc < 2 or argc > 4):
        sys.exit(255)
    try:  
        if argc == 2:
            file_list = os.listdir()
            file_list.sort()
            for element in file_list:
                if not element.startswith('.'):
                    rc = 0
                    b_element = bytes(element, "utf-8")
                    while rc < len(b_element):
                        rc = rc + os.write(1, b_element[rc:])
                        os.write(1,new_line)
        elif argc == 3:
            if command[2] == '-a' or command[2] == '--all':
                result = [os.curdir, os.pardir] + os.listdir()
                result.sort()
                for element in result:
                    rc = 0
                    b_element = bytes(element, "utf-8")
                    while rc < len(b_element):
                        rc = rc + os.write(1, b_element[rc:])
                        os.write(1,new_line)
            elif command[2] == '-R' or command == '--recursive':
                for root,files,dirs in os.walk(os.getcwd()):
                    for dir in dirs:
                        if not dir.startswith('.'):
                            rd = 0
                            b_dirs = bytes(dir, "utf-8")
                            while rd < len(b_dirs):
                                rd = rd + os.write(1, b_dirs[rd:])
                            os.write(1,new_line)
            else:
                fpath = os.path.abspath(command[2])
                if (os.path.isfile(fpath) == True):
                    b_element = bytes(command[2],"utf-8")
                    rc = 0
                    while rc < len(b_element):
                        rc = rc + os.write(1, b_element[rc:])
                    os.write(1,new_line)
                else:
                    file_list = os.listdir(command[2])
                    file_list.sort()
                    for element in file_list:
                        if not element.startswith('.'):
                            rc = 0
                            b_element = bytes(element, "utf-8")
                            while rc < len(b_element):
                                rc = rc + os.write(1, b_element[rc:])
                            os.write(1,new_line)
        else: 
            if command[2] == '-a' or command[2] == '--all':
                result = [os.curdir, os.pardir] + os.listdir(command[3])
                result.sort()
                for element in result:
                    rc = 0
                    b_element = bytes(element, "utf-8")
                    while rc < len(b_element):
                        rc = rc + os.write(1, b_element[rc:])
                    os.write(1,new_line)
            elif command[2] == '-R' or command == '--recursive':
                for root,files,dirs in os.walk(command[3]):
                    for dir in dirs:
                        if not dir.startswith('.'):
                            rd = 0
                            b_dirs = bytes(dir, "utf-8")
                            while rd < len(b_dirs):
                                rd = rd + os.write(1, b_dirs[rd:])
                            os.write(1,new_line)
    except IOError: 
        sys.exit(176)
def rmFunction(command):
    argc = len(command)
    if (argc < 2):
        print('Invalid command',flush= True)
        sys.exit(255)
    try:
        if(command[2] == '--dir' or command[2]== '-d'):
            for i in range(3, argc):
                if os.path.exists(command[i]) == True:
                    os.rmdir(command[i])
                else:
                    sys.exit(186)
        elif command[2] == '-R' or command[2] == '-r' or command[2] == '--recursive':
            for i in range(3,argc):
                if os.path.exists(command[i]) == True:
                    for root,dirs,files in os.walk(command[i]):
                        for elem in files:
                            os.remove(os.path.join(root,elem))
                        for dir in dirs:
                            os.rmdir(os.path.join(root,dir))
                    os.rmdir(command[i])
                else:
                    sys.exit(186)
        else:
            for i in range(2, argc):
                if (os.path.isfile(command[i]) == True):
                    os.remove(command[i])
                else: 
                    sys.exit(186)
    except Exception:
        sys.exit(186)
def copyobj(source, dest, BUFFER=1024*1024):
    while True:
        copy_buffer = source.read(BUFFER)
        if not copy_buffer:
            break
        dest.write(copy_buffer)
def copyfile(source, dest):
    with open(source, 'rb') as src, open(dest,'wb') as dst:
        copyobj(src,des)
def cpFunction(command):
    argc = len(command)
    if (argc < 4 or argc > 5):
        sys.exit(166)
    try:
        copyfile(command[2],command[3])
    except Exception:
        sys.exit(166)
def chmodFunction(command):
    argc = len(command)
    if (argc != 4):
        print("Invalid command", flush= True)
        sys.exit(255)
    status = os.stat(command[argc-1])
    try:
            status_nr = int(command[2],base=8)
            os.chmod(command[argc-1],status_nr)
    except:
        sys.exit(231)
command = sys.argv
op = command[1]
if op == 'mkdir':
    mkdirFunction(command)
elif op == 'rmdir':
    rmdirFunction(command)
elif op == 'touch':
    touchFunction(command)
elif op == 'cat':
    catFunction(command)
elif op == 'echo':
    echoFunction(command)
elif op == 'pwd':
    pwdFunction()
elif op == 'cp':
    cpFunction(command)
elif op == 'chmod':
    chmodFunction(command)
elif op == 'mv':
    mvFunction(command)
elif op == 'ln':
    lnFunction(command)
elif op == 'ls':
    lsFunction(command)
elif op == 'rm':
    rmFunction(command)
else:
    print("Invalid command",flush =True)
    sys.exit(255)