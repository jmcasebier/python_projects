#!/usr/bin/env python3

import zipfile
import re

file = zipfile.ZipFile("channel.zip")
print(f.read("readme.txt").decode("utf-8"))

num = '90052'

comments = []

while True:
    content = file.read(num + ".txt").decode("utf-8")
    comments.append(file.getinfo(num + ".txt").comment.decode("utf-8"))
    print(content)
    match = re.search("Next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)

print("".join(comments))

# ANSWER: oxygen
