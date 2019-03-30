import os
if True:
    os.remove("OLD_SONG.txt")
    op = open("OLD_SONG.txt",'w')
    for root, dirs, files in os.walk("."):  
        for filename in files:
            if filename != "file_reader.py":
                print(filename)
                op.write(filename+"\n")
    op.close()
