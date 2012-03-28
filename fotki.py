import sys, os, urllib2;
import xml.etree.ElementTree as ET;
import re;

class FotkiAlbum:
    
    def __init__(self, name):
        self.images = []

        response = urllib2.urlopen('http://public.fotki.com/edisongustavo/' + name)
        
        xmlFile = self.__findRssFile(response.read())
        self.__loadRss(urllib2.urlopen(xmlFile))
        
    def __save(self, file_name, url):
        try:
            u = urllib2.urlopen(url, None, 5)
        
            meta = u.info()
            file_size = int(meta.getheaders("Content-Length")[0])
            
            if os.path.exists(file_name) and os.path.getsize(file_name) == file_size:
                print("File %s already exists with same size, skipping.." % file_name)
                return
            else:
                print "Downloading: %s (%s KB)" % (url, file_size / 1024)
                
            f = open(file_name, 'wb')
            
            block_sz = 8192
            while True:
                buff = u.read(block_sz)
                if not buff:
                    break
                f.write(buff)
            
            f.close()
        except urllib2.HTTPError, e:
            print "HTTP Error:", e.code , url
        except urllib2.URLError, e:
            print "URL Error:", e.reason , url 
        
    def saveTo(self, dirName):
        if not os.path.exists(dirName):
            os.makedirs(dirName)
            
        for imgurl in self.images:
            self.__save(dirName + '/' + imgurl.split('/')[-1], imgurl)
            
    def __findRssFile(self, html):
        pattern = re.compile('http://feeds\.fotki\.com/edisongustavo/album_[a-zA-Z]+\.rss')
        return pattern.findall(html)[0]
        
    def __loadRss(self, response):
        data = response.read()
        tree = ET.fromstring(data)
        for elementItem in tree.iter(tag="item"):
            
            #HACK: I think that if I  use XPath it will be better, this is a really ugly way of fetching the children
            imgurl = [item.get('url') for item in elementItem.getchildren() if item.tag.endswith("content")][0]
            self.images.append(imgurl)
                
def main(args):
    if (len(args) <= 1):
        raise "Need the name to parse"
    
    albumName = args[1]
    fotki = FotkiAlbum(albumName)
    fotki.saveTo(albumName)
    
if __name__ == '__main__':
    main(sys.argv)
