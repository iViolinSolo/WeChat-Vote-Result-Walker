# WeChat-Vote-Result-Walker
---------------------------

对微信（WeChat）公众号文章内置投票插件的实时数据抓取的Python爬虫


#Before Use
-----------

1. dowload and install [PhantomJS](http://phantomjs.org/download.html) and start `PhantomJS` with:

  `$ phantomjs phantomjs_fetcher.js [port]`

  BTW, if your are in `MacOS` enviroment, you can easyily Unzip `phantomjs-2.1.1-macosx.zip` in 

  current directory, you can find an executable file in `bin` sub-directory.


2. install python dependences:

  tornado:

  `$ pip install tornado`

  pycurl:

  `$ pip install pycurl`

  I really recommend you use `VirtualEnv` to install the dependences, easy, effective and clean!


#How to use
-----------
1. firstly, run `PhantomJS`:

  `$ phantomjs phantomjs_fetcher.js [port]` , you can use a port like '12306', when you run this 

  command in terminal, you may get something like a dialog, showing you that this action need a 

  permission to connect to internet. Just permit it.

2. change the `port` in the `test.py` python file:
  
  Line 11 in `test.py`, change the proxy url correctly with the port you set in step 1.

2. run my main python file: `test.py` in another window of terminal:

  `$ python run test.py`

  All Done!


#Docs
-----



#Thanks to
----------

- [Python利用Phantomjs抓取渲染JS后的网页](http://guoze.me/2015/01/19/python-phantomjs-crawler/)

- GitHub Repository : [PhantomjsFetcher](https://github.com/2shou/PhantomjsFetcher)

- [PhantomJS](http://phantomjs.org/download.html)

- [Tornado](https://github.com/tornadoweb/tornado)


# License
---------

[LICENSE.MIT](https://github.com/BigDipper7/WeChat-Vote-Result-Walker/blob/master/LICENSE)