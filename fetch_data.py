# -*- coding: utf-8 -*-
import json
from FileUtl import getFileList

import numpy as np
import pylab as pl


result = []
fres = open('result.txt', 'w+')

def getCurList():
	file_name_list = getFileList('.')
	for f in file_name_list:
		print str(f)
		if str(f)[0:4] == 'vote':
			print "file: ", f, " prcessing..."
			fetch_dic(f)


def fetch_dic(file_name):
	# file_name = 'vote_2017_03_12__11_17_25.html'
	with open(file_name, 'r') as fr:
		lnum = 0
		for line in fr:
			lnum += 1
			if lnum == 816:
				# print line
				stri = line[17:-2]
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
				print temp
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

	idx = 0
	for epoch in result:
		# x1.append(epoch['time'])
		# x2.append(epoch['time'])
		x1.append(idx)
		x2.append(idx)
		idx +=1
		for op in epoch['options']:
			if op['name'] == u'\u738b\u854a':
				y1.append(op['cnt'])
			elif op['name'] == u'\u9646\u6021\u513f':
				y2.append(op['cnt'])
			elif op['name'] == u'\u6881\u777f':
				y3.append(op['cnt'])
			elif op['name'] == u'\u4f59\u6b22\u5e86':
				y4.append(op['cnt'])
			elif op['name'] == u'\u9648\u9e23\u79c0':
				y5.append(op['cnt'])
			elif op['name'] == u'\u51af\u7965\u541b':
				y6.append(op['cnt'])
			elif op['name'] == u'\u9b4f\u6587\u5353':
				y7.append(op['cnt'])
			elif op['name'] == u'\u8521\u5723\u6770':
				y8.append(op['cnt'])
			elif op['name'] == u'\u9648\u96c5\u73fa':
				y9.append(op['cnt'])
			elif op['name'] == u'\u6731\u6021':
				y10.append(op['cnt'])
			elif op['name'] == u'\u5218\u73ba\u6726':
				y11.append(op['cnt'])
			elif op['name'] == u'\u5f20\u9e23\u9633':
				y12.append(op['cnt'])
			elif op['name'] == u'\u987e\u94ed\u8f69':
				y13.append(op['cnt'])
			elif op['name'] == u'\u7fdf\u73a5':
				y14.append(op['cnt'])
			elif op['name'] == u'\u4faf\u6210\u6eaa':
				y15.append(op['cnt'])
			elif op['name'] == u'\u5468\u4f73\u73ae':
				y16.append(op['cnt'])


	pl.plot(x1, y1, label=u'\u738b\u854a')# use pylab to plot x and y
	pl.plot(x2, y2, label=u'\u9646\u6021\u513f')
	pl.plot(x2, y3, label=u'\u6881\u777f')
	pl.plot(x2, y4, label=u'\u4f59\u6b22\u5e86')
	pl.plot(x2, y5, label=u'\u9648\u9e23\u79c0')
	pl.plot(x2, y6, label=u'\u51af\u7965\u541b')
	pl.plot(x2, y7, label=u'\u9b4f\u6587\u5353')
	pl.plot(x2, y8, label=u'\u8521\u5723\u6770')
	pl.plot(x2, y9, label=u'\u9648\u96c5\u73fa')
	pl.plot(x2, y10, label=u'\u6731\u6021')
	pl.plot(x2, y11, label=u'\u5218\u73ba\u6726')
	pl.plot(x2, y12, label=u'\u5f20\u9e23\u9633')
	pl.plot(x2, y13, label=u'\u987e\u94ed\u8f69')
	pl.plot(x2, y14, label=u'\u7fdf\u73a5')
	pl.plot(x2, y15, label=u'\u4faf\u6210\u6eaa')
	pl.plot(x2, y16, label=u'\u5468\u4f73\u73ae')

	pl.legend(loc='best')

	pl.title(u'2017年3月12日 11:17:35 - 00:12:13 投票折线图')# give plot a title
	pl.xlabel(u'采样点（次／10s）')# make axis labels
	pl.ylabel(u'投票数')

	pl.show()


def main():
	# fetch_dic('vote_2017_03_12__11_17_25.html')
	getCurList()
	print '-------\n\n\n\n'
	print result

	# for epoch in result:
	plt(result)

	fres.close()



if __name__ == '__main__':
	main()







