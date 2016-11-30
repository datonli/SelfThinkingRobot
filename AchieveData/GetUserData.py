from wcrawler import *
from jsondb.db import Database

if __name__ == '__main__':
    crawler = WCrawler(cookie = 'UOR=www.baidu.com,blog.sina.com.cn,; U_TRS1=0000004f.32c845f.5733e2d5.ad9108a6; U_TRS2=0000004f.32d445f.5733e2d5.b5716a19; SINAGLOBAL=61.135.169.79_1463018197.192534; Apache=61.135.169.79_1463018197.747655; SessionID=le113sggcdf7l11jsc6ohnlbu6; vjuids=4315adb9d.154a2ae19f0.0.b49484ff; ULV=1463038075786:2:2:2:61.135.169.79_1463018197.747655:1463018197886; SGUID=1464491184077_71168201; SCF=AqWXSdmqnlZXOZ97qJXfDPFH_LP7xOPjPIZ2KgmJLs5u4s9NUbHH-hKLtGyy6BSDgQjhOgDOgUaK_NW8PGgl_Js.; lxlrtst=1476689468_o; lxlrttp=1477565169; sso_info=v02m6alo5qztaSYlrmunpKZtZqWkL2Ms4C4jaOEtoyzlLWMgMDA; SINABLOGNUINFO=3086163550.b7f31e5e.; vjlast=1477628269.1478053154.11; tgc=TGT-MzA4NjE2MzU1MA==-1478097882-xd-C3E6ED5F3591D09ECDBF1C1870E7F2D7; SUB=_2A251HYuKDeTxGeVO41QQ9i3JzjyIHXVWavpCrDV_PUNbm9AKLUbFkW8Nc4Jp5aiyZ60bFPZlskjv-8lyRA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5aIE.ERRyKAcZffYlVQ4195NHD95Q0ehnceKq0SK-7Ws4Dqcji-GS4-GLXIsvV; ALC=ac%3D2%26bt%3D1478097882%26cv%3D5.0%26et%3D1509633882%26scf%3DAqWXSdmqnlZXOZ97qJXfDPFH_LP7xOPjPIZ2KgmJLs5u4s9NUbHH-hKLtGyy6BSDgQjhOgDOgUaK_NW8PGgl_Js.%26uid%3D3086163550%26vf%3D0%26vs%3D0%26vt%3D0%26es%3Da2a19c21b755058448fa2428ee17b3fe; ALF=1509633882; LT=1478097882',\
             max_num_weibo = 100, \
             max_num_fans = 100, \
             max_num_follow = 100, \
             wfilter = 'all', \
             return_type = 'string')
    luyi_data = crawler.crawl(url = 'http://weibo.cn/luyi')
    db = Database("luyi_data.db")
    db.data(key = "luyi_data", value = luyi_data)
    ''' TODO: Font support for Chinese '''
    print(db.data(key = "luyi_data"))
