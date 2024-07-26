import os
#파일 찾기


def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        if os.path.isdir(full_filename):
           search(full_filename) 
        else:
            ext = os.path.splitext(full_filename)[-1]
        if ext ==".py":
            print(full_filename)

search("/Users/iwon/woncoding")