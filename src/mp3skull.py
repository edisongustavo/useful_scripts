'''
Created on Sep 5, 2011

@author: Guga
'''
import re
import operator

def songs(contents):
    xed_re = re.compile(r'&#(\d+);')
    def usub(m):
        return unichr(int(m.group(1)))
    
    songNames = set()
    for match in re.finditer(r'<div style="font-size:15px;"><b>(.+)</b></div>', contents, re.M | re.I):
        songName = xed_re.sub(usub, match.group(1))[:-4]
        #TODO [edison]: do case insensitive comparation
        songNames.add(songName)
     
    links = []
    for match in re.finditer(r'<div style="margin-left:8px; float:left;"><a href="http://(.*)\.mp3.*>Download</a>', contents, re.M|re.I):
        links.append(match.group(1) + ".mp3")
        
    return sorted(zip(songNames, links), key=operator.itemgetter(0))
