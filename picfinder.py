#coding:utf-8
import urllib
import urllib2
import cookielib
import re
import os
import random


#获取一个保存cookie的对象
cj = cookielib.LWPCookieJar()
#将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
cookie_support = urllib2.HTTPCookieProcessor(cj)
#创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的URL的打开
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
#将包含了cookie、http处理器、http的handler的资源和urllib2对象板顶在一起
urllib2.install_opener(opener)

def save_file(path,filename,data):
	if data ==None:
		return
	if (not os.path.exists(path)):
		print "path does not exists!"
		return
	file=open(path+filename,"wb")
	file.write(data)
	file.flush()
	file.close()

class picFinder(object):
	def __init__(self,path):
		if os.path.exists(path):
			self.path=path
		else:
			self.path="/tmp/"

	def getGroupBigPic(self,picID):#picid is a int with 8 number
		headers={
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"
		}
		url="http://img3.douban.com/view/group_topic/large/public/p"+str(picID)+".jpg"
		req=urllib2.Request(url)
		for n in headers:
			req.add_header(n,headers[n])
		try:
			html=urllib2.urlopen(req).read()
			save_file(self.path,"p"+str(picID)+".jpg",html)
		except urllib2.URLError,e:
			print "404error"
		else:
			print "others"

	def getPhotoPic(self,picID):
		postdata=urllib.urlencode({

			})
		headers={
		"Accept":"image/webp,*/*;q=0.8",
		"Accept-Encoding":"gzip,deflate,sdch",
		"Accept-Language":"zh-CN,zh;q=0.8",
		"Connection":"keep-alive",
		"Host":"img3.douban.com",
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
		}

		url="http://img3.douban.com/view/photo/photo/public/p"+str(picID)+".jpg"

		req=urllib2.Request(url,data=postdata)
		for n in headers:
			req.add_header(n,headers[n])
		try:
			html=urllib2.urlopen(req).read()
			save_file(self.path,"p"+str(picID)+".jpg",html)
		except urllib2.URLError,e:
			print "404error"
		else:
			print "others"


	def getLargePic(self,picID):
		postdata=urllib.urlencode({

			})
		headers={
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
		}

		url="http://img3.douban.com/view/photo/large/public/p"+str(picID)+".jpg"

		req=urllib2.Request(url,data=postdata)
		for n in headers:
			req.add_header(n,headers[n])
		try:
			html=urllib2.urlopen(req).read()
			save_file(self.path,"p"+str(picID)+".jpg",html)
		except urllib2.URLError,e:
			print "404error"
		else:
			print "others"

	def getRandomPic(self,picnum,pickind):
		# picidlist=[]
		if pickind==0:
			for i in range(picnum):
				# picidlist.append(int(random.uniform(10,30)*1000000))
				self.getGroupBigPic(int(random.uniform(10,20)*1000000))
		elif pickind==1:
			for i in range(picnum):
				# picidlist.append(int(random.uniform(10,30)*1000000))
				self.getPhotoPic(int(random.uniform(2212,2213)*100000))
		else:
			for i in range(picnum):
				# picidlist.append(int(random.uniform(10,30)*1000000))
				self.getLargePic(int(random.uniform(22,23)*10000000))


	def getContinuePic(self,startid,picnum,pickind):
		if pickind==0:
			for i in range(picnum):
				# picidlist.append(int(random.uniform(10,30)*1000000))
				self.getGroupBigPic(startid+i)
		elif pickind==1:
			for i in range(picnum):
				# picidlist.append(int(random.uniform(10,30)*1000000))
				self.getPhotoPic(startid+i)
		else:
			for i in range(picnum):
				self.getLargePic(startid+i)

	def getSinglePic(self,picID,pickind):
		if pickind==0:
			self.getGroupBigPic(picID)
		elif pickind==1:
			self.getPhotoPic(picID)
		else:
			self.getLargePic(picID)


if __name__=="__main__":
	picFinder=picFinder("/Volumes/Macintosh HD  1/pic/")
	#picFinder.getRandomPic(20,2)
	#picFinder.getSinglePic(2208041884)
	picFinder.getContinuePic(2208041654,2,2)



