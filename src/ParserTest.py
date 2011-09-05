'''
Created on Sep 5, 2011

@author: Guga
'''
import unittest
import mp3skull


class Test(unittest.TestCase):
    def testName(self):
        songs = mp3skull.songs("mp3skull.html")
#        self.assertEquals(
#                          (u"Fogo no P\u00E9 - Vai ser Comida de Bicho", "dc152.4shared.com/img/767778345/cf9db145/dlink__2Fdownload_2FU9acExuS_3Ftsid_3D20110905-125857-25868840/preview.mp3"),
#                          songs[0])
        for i in songs:
            print (i[0] + " >< " + i[1])
