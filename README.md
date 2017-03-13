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

首先这是为了解决什么的需求呢？微信现在公众号文章中自带投票插件，但是存在一些问题，比如当有人刷票时，你无法确定究竟是

谁刷票的，因为后台数据只能看到投票的一些数据，但是没有投票数据增长曲线。对于一些明显的刷票行为，比如10min内暴涨1000票

这种的，其实你是没办法判断的，要么只能平时一只监控数据，截图统计数据增长模式，要么就只能发呆了。

所以这个repo是为了解决微信公众号推文内置vote插件的数据实时爬取问题，其实主要是其中解决问题的思想需要记录一下。

1.首先我们确定我们需要爬取的数据，以文章 [投票 | GamTalk演讲大赛作品公示欢迎投票！](http://mp.weixin.qq.com/s?__biz=MzIwMjcxMDkzNQ==&mid=2247484332&idx=1&sn=ee27b7ae03c9d881418615c96069c3fe&chksm=96dbc954a1ac40421777f00571982fb7b9ceab7c0a2fab6b9e470e9ef423ae33aa39702d196b&mpshare=1&scene=1&srcid=0312k3JRDNp5tZYLH3ZtbVGQ#rd) 为例进行讲解。

我们发现，其实对于url`http://mp.weixin.qq.com/s?__biz=MzIwMjcxMDkzNQ==&mid=2247484332&idx=1&sn=ee27b7ae03c9d881418615c96069c3fe&chksm=96dbc954a1ac40421777f00571982fb7b9ceab7c0a2fab6b9e470e9ef423ae33aa39702d196b&mpshare=1&scene=1&srcid=0312k3JRDNp5tZYLH3ZtbVGQ#rd` 来说

可以直接在chrome中进行浏览，只是我们由于没有在微信浏览器中，我们的投票已经被禁止了：

![投票插件截图](https://github.com/BigDipper7/WeChat-Vote-Result-Walker/raw/master/doc/ss1.png)

但是不慌，其实我们已经拿到投票数据了，只是被微信隐藏掉了。右键 inspect，查看源码：

![微信插件数据](https://github.com/BigDipper7/WeChat-Vote-Result-Walker/raw/master/doc/ss2.png)

然而很尴尬的是，查看network下的请求的response，发现其实我们直接用上面那个url，是没有拿到数据的，果然微信是异步加载的投票插件，又是后期js渲染的：

![请求截图1](https://github.com/BigDipper7/WeChat-Vote-Result-Walker/raw/master/doc/ss3.png)

所以查看了后期那大段耗时操作，很容易找到了对应的插件的真实url：

![真实请求截图2](https://github.com/BigDipper7/WeChat-Vote-Result-Walker/raw/master/doc/ss4.png)

那么这个时候获取投票插件的真实url应该是`http://mp.weixin.qq.com/mp/newappmsgvote?action=show&__biz=MzIwMjcxMDkzNQ==&supervoteid=444598550&uin=&key=&pass_ticket=&wxtoken=&mid=2247484332&idx=1`:

但是这个时候问题又来了，虽然这个url是对的，但是查看对应response并不是数据，又是一大堆js。然而你把这个url直接用浏览器访问的时候，确实直接渲染出投票插件的：

![请求截图2的response](https://github.com/BigDipper7/WeChat-Vote-Result-Walker/raw/master/doc/ss5.png)

![获取投票插件](https://github.com/BigDipper7/WeChat-Vote-Result-Walker/raw/master/doc/ss6.png)

那么说明是js渲染的，然而我比较懒，懒得去读js代码了，所以直接找个可以渲染成html的包最开心啦～（虽然后面证明自己懒造成了好多不良结果）

那么能渲染js的话，就不能简简单单urllib get response了，突然发现了神器`PhantomJS`，碰巧有个po主结合`tornado`和`PhantomJS`，实现了一个直接fetch的小模块，方便多了hhh

果断参考 [Python利用Phantomjs抓取渲染JS后的网页](http://guoze.me/2015/01/19/python-phantomjs-crawler/) 这个文章，和对应repo [PhantomjsFetcher](https://github.com/2shou/PhantomjsFetcher) ，分分钟撸个代码出来，也就是`test.py`

![代码](https://github.com/BigDipper7/WeChat-Vote-Result-Walker/raw/master/doc/ss7.png)

在po主demo的例子上，加入了timer，定时循环调用的我的爬取函数，同时按照时间依次存储每次的结果（目前是10s左右调用一次），同时改变一下UA，强行伪装一下，终于撸完了

本以为成功的交差了，尼玛，坑爹呢这是！

![细节response](https://github.com/BigDipper7/WeChat-Vote-Result-Walker/raw/master/doc/ss8.png)

让我们仔细的再看一遍撸到的真实网址，突然发现：1.微信你不是取消了必须关注微信号才能投票这个功能么，为什么还有判断（我们要吸粉啊啊）2.这个voteInfo。。。包含了所有的投票结果数据。。。

坑爹呢这是，早知道仔细看代码了！

总结：其实最大的收获是，找到了一个自动渲染js的python轮子，2.不看代码真坑爹 😢


# 更新
------
新添加了一个画图代码，将所有处理的`html`文件，处理成`dict`，并存储在当前目录下的`result.txt`中。同时利用`matplotlib`进行画图，至于import的`numpy`的包，可以删掉

1. 安装依赖：

`$ pip install matplotlib` 

2. run：

`$ python fetch_data.py`

其中有个坑就是`matplotlib`对中文支持不好，所以全部设置成`unicode`的了，最后结果如下图，利用`matplotlib`导出的图片文字不显示出来，貌似是因为没有设置字体，所以直接截图了：

![导出结果](https://github.com/BigDipper7/WeChat-Vote-Result-Walker/raw/master/doc/figure_res.png)

![mac自带截图](https://github.com/BigDipper7/WeChat-Vote-Result-Walker/raw/master/doc/figure_vote_res.png)


#Thanks to
----------

- [Python利用Phantomjs抓取渲染JS后的网页](http://guoze.me/2015/01/19/python-phantomjs-crawler/)

- GitHub Repository : [PhantomjsFetcher](https://github.com/2shou/PhantomjsFetcher)

- [PhantomJS](http://phantomjs.org/download.html)

- [Tornado](https://github.com/tornadoweb/tornado)


# License
---------

[LICENSE.MIT](https://github.com/BigDipper7/WeChat-Vote-Result-Walker/blob/master/LICENSE)