作业一：

安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。

作业二：

使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
猫眼电影网址： https://maoyan.com/films?showType=3
要求：必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。

##学习笔记
### 1.requests笔记
#### 1.1 能力范围
        python简单的http库.
#### 1.2 请求注意事项
#####1.2.1 请求头
#####     1.2.2 cookies如何处理
#####     1.2.3 如果请求失败如何处理
           超时如何处理
           被反爬如何处理
#####     1.2.4 代理如何写
#####1.2.5 中文字符显示问题
##### 1.2.6 常用user-agent 设置
######1.2.6.1 android 
 ```json
Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19
Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
```     
######1.2.6.2 Firefox 
 ```json
Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0
Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0
```   

######1.2.6.3 GoogleChrome
 ```json
Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36
Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19
```
######1.2.6.4 IOS
```json
Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3
Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3
```

### 2. BeauifulSoup
#### 2.1 能力范围
分析html
#### 2.2 需要注意的点
##### 2.2.1 元素兄弟遍历时，找的是下一个节点
##### 还需要再过一边。。。

### 3. XPATH
先用用看 不明白的再说吧

### 4. scrapy
### 4.1 command  line tool
#### 4.1.1 在不同的项目录中，可以配置相同的setting文件
#### 4.1.2 Creating Project :   scrapy startproject myproject [project_dir] . project_dir 如果不写 项目dir有 myproject 相同
#### 4.1.3 create a new spider:  scrapy genspider mydomain mydomain.com
#### 4.1.4 check: 运行时检查
#### 4.1.5 list:  列出所有可用爬虫
### 4.2 spider
### 4.2.1  说明：定义如何抓取数据，打包数据的地方
### 4.2.2 scrapy.Spider 类型1
### 4.2.2.1 logging 如何使用，配置成项目能用的方式 
self.logger 使用 
    https://docs.scrapy.org/en/latest/topics/logging.html#topics-logging-from-spiders
### 4.2.2.2 可以设置变量 
scrapy crawl myspider -a category=electronics 
在__init__ 中函数中使用 
### 4.2.3 Generic Spiders
### 4.2.3.1  CrawlSpider
### 4.2.3.2  XMLFeedSpider
### 4.2.3.3  CSVFeedSpider
### 4.3 Selector
```text
一般用法：response.xpath('//title/text()')
也可以：Selector(response=response).xpath('//span/text()').get()
getall 与 get 区别

如果是查询class 用CSS selector
sel.css('.shout').xpath('./time/@datetime').getall()

```

