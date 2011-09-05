'''
Created on Sep 5, 2011

@author: Guga
'''
import mp3skull
import sys, codecs

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

if __name__ == '__main__':
    songs = mp3skull.songs(read_file(sys.argv[1]))
    
    contents = ""
    for songAndLink in songs:
        contents = contents + songAndLink[0] +" >>> " + songAndLink[1] + "\n"

    print("Opening " + sys.argv[2] + " for writing")        
    with codecs.open(sys.argv[2], 'w', encoding="UTF-8") as f:
        f.write(contents)
