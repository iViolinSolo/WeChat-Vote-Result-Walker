# -*- coding: utf-8 -*-
from tornado_fetcher import Fetcher
import threading
import time


def fetch():

	fetcher=Fetcher(
	user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1', # 模拟浏览器的User-Agent
	phantomjs_proxy='http://localhost:12366', # phantomjs的地址
	pool_size=10, # 最大的httpclient数量
	async=False # 同步还是异步
	)

	url = "http://mp.weixin.qq.com/mp/newappmsgvote?action=show&__biz=MzIwMjcxMDkzNQ==&supervoteid=444598550&uin=&key=&pass_ticket=&wxtoken=&mid=2247484332&idx=1"


	temp = fetcher.phantomjs_fetch(url, js_script='function(){setTimeout("window.scrollTo(0,100000)}", 1000)')

	# print temp

	print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), " captured!", " -- coat time:", temp['time'], "s. "

	file_name = "vote_"+time.strftime("%Y_%m_%d__%H_%M_%S", time.localtime())+".html"
	f =open(file_name, 'w')
	f.write(str(temp['content'].encode('utf-8')))
	f.close()

	global timer
	timer = threading.Timer(10.0-temp['time'], fetch, [])
	timer.start()


def main():
	timer = threading.Timer(10.0, fetch, [])
	timer.start()

if __name__ == '__main__':
	main()