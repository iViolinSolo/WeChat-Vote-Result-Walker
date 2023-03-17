# -*- coding: utf-8 -*-
import json
from FileUtl import getFileList
import os
import natsort
import matplotlib
matplotlib.use('Agg')

import numpy as np
import pylab as pl


result = []
fres = open('result.txt', 'w+')

def getCurList():
	return getdir()

def getdir():
	file_list = os.listdir("./vote")
	file_name_list = sorted(file_list, key=lambda x:os.path.getmtime(os.path.join("./vote",x)))
	for f in file_name_list:
		if str(f)[0:4] == 'vote':
			print "file: ", f, " prcessing..."
			fetch_dic(f)


def fetch_dic(file_name):
	# file_name = 'vote_2017_03_12__11_17_25.html'
	file_name = "./vote/" + file_name
	with open(file_name, 'r') as fr:
		lnum = 0
		for line in fr:
			lnum += 1
			if lnum == 866:
				# print line
				stri = line[19:-2]
				# print stri
				dicts = json.loads(stri)
				# print dicts
				# print dicts['vote_subject'][0]['options']
				temp={}
				temp['time'] = file_name[5:-5]
				temp['options'] = []
				for item in dicts['vote_subject'][0]['options']:
					ite = {}
					# print item
					ite['name'] = item['name']
					ite['cnt'] = item['cnt']
					temp['options'].append(ite)
				#print temp
				result.append(temp)
				fres.write(str(temp)+'\n')


def plt(result):
	print 'result...'
	x1 = []
	y1 = []
	x2 = []
	y2 = []
	y3 = []
	y4 = []
	y5 = []
	y6 = []
	y7 = []
	y8 = []
	y9 = []
	y10 = []
	y11 = []
	y12 = []
	y13 = []
	y14 = []
	y15 = []
	y16 = []
	y17 = []
	y18 = []

	idx = 0
	for epoch in result:
		# x1.append(epoch['time'])
		# x2.append(epoch['time'])
		x1.append(idx)
		x2.append(idx)
		idx +=1
		for op in epoch['options']:
			if op['name'] == u'\u73af\u5de5\u5b66\u9662 \u5218\u5b50\u8000':
				y1.append(op['cnt'])
			elif op['name'] == u'\u98df\u751f\u5b66\u9662 \u738b\u6668\u5b87':
				y2.append(op['cnt'])
			elif op['name'] == u'\u5316\u5de5\u5b66\u9662 \u738b\u82e5\u742a':
				y3.append(op['cnt'])
			elif op['name'] == u'\u5316\u5de5\u5b66\u9662 \u5f6d\u7a0b':
				y4.append(op['cnt'])
			elif op['name'] ==  u'\u7406\u5b66\u9662 \u95eb\u5b50\u7487':
				y5.append(op['cnt'])
			elif op['name'] == u'\u7ecf\u7ba1\u5b66\u9662 \u5468\u65b0\u6960':
				y6.append(op['cnt'])
			elif op['name'] == u'\u7535\u6c14\u5b66\u9662 \u90b1\u8fd1\u7ff0':
				y7.append(op['cnt'])
			elif op['name'] == u'\u7406\u5b66\u9662 \u5f20\u96c5\u9759':
				y8.append(op['cnt'])
			elif op['name'] == u'\u4fe1\u606f\u5b66\u9662 \u5f20\u535a\u5b87':
				y9.append(op['cnt'])
			elif op['name'] == u'\u4e2d\u6fb3\u5b66\u9662 \u76f8\u4f73\u670b':
				y10.append(op['cnt'])
			elif op['name'] == u'\u5efa\u5de5\u5b66\u9662 \u5434\u6768':
				y11.append(op['cnt'])
			elif op['name'] == u'\u827a\u672f\u5b66\u9662 \u674e\u6668':
				y12.append(op['cnt'])
			elif op['name'] == u'\u4fe1\u606f\u5b66\u9662 \u5218\u9e3f\u6bc5':
				y13.append(op['cnt'])
			elif op['name'] == u'\u98df\u751f\u5b66\u9662 \u90ed\u6587\u9756':
				y14.append(op['cnt'])
			elif op['name'] == u'\u673a\u68b0\u5b66\u9662 \u675c\u6625\u6656':
				y15.append(op['cnt'])
			elif op['name'] == u'\u5916\u56fd\u8bed\u5b66\u9662 \u8d75\u6021':
				y16.append(op['cnt'])
			
			elif op['name'] == u'\u7406\u5b66\u9662 \u77f3\u7f8e':
				y17.append(op['cnt'])
			elif op['name'] == u'\u98df\u751f\u5b66\u9662 \u738b\u827a\u83b9':
				y18.append(op['cnt'])



	pl.rcParams["font.sans-serif"]=["SimHei"] #设置字体
	pl.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题


	pl.plot(x1, y1, label=u'\u73af\u5de5\u5b66\u9662 \u5218\u5b50\u8000')# use pylab to plot x and y
	pl.plot(x2, y2, label=u'\u98df\u751f\u5b66\u9662 \u738b\u6668\u5b87')
	pl.plot(x2, y3, label=u'\u5316\u5de5\u5b66\u9662 \u738b\u82e5\u742a')
	pl.plot(x2, y4, label=u'\u5316\u5de5\u5b66\u9662 \u5f6d\u7a0b')
	pl.plot(x2, y5, label=u'\u7406\u5b66\u9662 \u95eb\u5b50\u7487')
	pl.plot(x2, y6, label=u'\u7ecf\u7ba1\u5b66\u9662 \u5468\u65b0\u6960')
	pl.plot(x2, y7, label=u'\u7535\u6c14\u5b66\u9662 \u90b1\u8fd1\u7ff0')
	pl.plot(x2, y8, label=u'\u7406\u5b66\u9662 \u5f20\u96c5\u9759')
	pl.plot(x2, y9, label=u'\u4fe1\u606f\u5b66\u9662 \u5f20\u535a\u5b87')
	pl.plot(x2, y10, label=u'\u4e2d\u6fb3\u5b66\u9662 \u76f8\u4f73\u670b')
	pl.plot(x2, y11, label=u'\u5efa\u5de5\u5b66\u9662 \u5434\u6768')
	pl.plot(x2, y12, label=u'\u827a\u672f\u5b66\u9662 \u674e\u6668')
	pl.plot(x2, y13, label=u'\u4fe1\u606f\u5b66\u9662 \u5218\u9e3f\u6bc5')
	pl.plot(x2, y14, label=u'\u98df\u751f\u5b66\u9662 \u90ed\u6587\u9756')
	pl.plot(x2, y15, label=u'\u673a\u68b0\u5b66\u9662 \u675c\u6625\u6656')
	pl.plot(x2, y16, label=u'\u5916\u56fd\u8bed\u5b66\u9662 \u8d75\u6021')
	
	pl.plot(x2, y17, label=u'\u7406\u5b66\u9662 \u77f3\u7f8e')
	pl.plot(x2, y18, label=u'\u98df\u751f\u5b66\u9662 \u738b\u827a\u83b9')
	pl.legend(loc='best')

	pl.title(u'2023年3月16日 最美的你投票统计图')# give plot a title
	pl.xlabel(u'采样点（次／10s）')# make axis labels
	pl.ylabel(u'投票数')

	print("-----------------")
	pl.savefig('./vote.jpg')
	pl.show()


def main():
	# fetch_dic('vote_2017_03_12__11_17_25.html')
	getCurList()
	print '-------\n\n\n\n'
	# print result

	# for epoch in result:
	plt(result)

	fres.close()



if __name__ == '__main__':
	main()







