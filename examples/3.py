# /usr/bin/env python3
# -*- coding: utf-8 -*-


fileptr = open("file2.txt", "r")
content1 = fileptr.readline()
content2 = fileptr.readline()
print(content1)
print(content2)
fileptr.close()
