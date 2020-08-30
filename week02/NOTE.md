学习笔记
###HTTP 协议
1. Url是Uri的子集 （Uniform Resource Identifier)
2. Http 是无状态的协议， 后来加入了COOKIE技术 用于管理用户状态
3. 持久链接 Http keep-alive 减少建立与断开通信量的开销。那么规模爬虫 对应需要模拟 对应的会话 用于保存对应的session。
以减少服务器以及爬虫建立链接时的开销。
4. 压缩传输的内容编码：GZIP，COMPRESS，DEFLATE，INDENTITY
5. 分割传输编码
6. 发送多种数据的多部分对象集合：
```text
    6.1  multipart/form-data ， 在web表单上传时使用
    6.2 multipart/byteranges ， 状态206 响应包含了多个范围的内容           
    6.3 在http报文使用多部分对象集合时，需要在首部字段里加上Content-Type
    6.4 使用boundary 字符串来划分多部分对象集合知名的各类实体。 boundary字符串知道的各个实体起始行之前插入“--”标记，而在多部分集合对应的字符串后
    插入“--”标记
```
7. 获取部分内容的范围请求
```text
Range requests
```
 8.内容协商返回最合适的内容
 ```text
Accept
accept-charset
accept-Encoding
accept-Language
Content-Language
 ```
9.状态码类别
```text
1XX Informational 接受请求正在处理
2XX Success 请求正常处理完毕
    200 OK
    204 No Content  无内容更新
    206 Parital Content  响应保温中包含由Content-Range 指定范围的实体内容
3XX Redirection 重定向状态码 需要进行附加操作以完成请求
    301 Moved Permanently  永久性重定向，URI 发生改变 或者 客户端保存的URI不是最新的，或是需要跳转到默认主页,客户端在这里会更新书签的链接吗？
    302 Found 临时重定向 与上条相比不会更新书签的链接
    303 See Other 303 与302功能相同，只是303明确指示 客户端应用Get请求访问对于内容
    备注：301-303, 状态码返回时，机会所有的浏览器的都会把Post改成Get，并删除请求保温内的主题，之后请求会自动再次发送
    304： Not Modified（资源找到，但未符合条件请求）这里比较迷
    307： Temporary Redirect 临时重定向，与302相同，不同的是，不会要求post变成GET
4XX Client Error 服务器无法处理请求
    400 Bad Request 表示请求报文中存在语法错误。当错误发生时，需要修改请求的内容后再次发送请求。浏览器会像200OK一样对待该状态码
    401 Unauthorized 需要通过HTTP认证(basic认证，digest认证）的认证信息
    403 Forbidden 请求资源的访问被服务器拒绝了。
    404 Not Found

5XX server error 服务器处理请求出错
    500 Internal Server Error  服务器在执行请求时发生了错误，也有可能是web应用存在BUG或某些临时故障
    503 Unavailable 该状态码表明服务器暂时处于超负载或正在进行停机维护，现在无法处理请求。如果事先的之接触以上状况需要的时间，最好写入retryAfter首部
再返回给客户端段
```
10 Http/1.1通用首部字段
```text
    1. Cache-Control: no-cache
            缓存需要向源服务器进行有效期确认后处理资源，
            no-cache = Location 有赋值时，不缓存。只能在响应指令中指定该参数
    2. Cache-Control: no-store
            这才是不缓存
    3. Cache-Control: 用于控制代理与客户端 服务器之间的交互，可以控制他们访问时，缓存的行为。不过这种一般由谁来设置呢？ 服务器吗？
    4. Connection:
        a. 控制代理不再转发首部字段，代理再转发过程中删除对应的首部字段
        b. 管理持久链接: close, keep-alive
    5. Date: Http 报文的日期与时间
    6. Upgrade: 用于检测是否可以使用一个完全不同的通信协议： 因为Upgrade仅限于客户端和邻接服务器之间，因此Upgrade 还需要额外指定Connection :Upgrade
    7. Via 追踪客户端与服务器之间的请求和响应保温的传输路径？ 这里比较奇怪，结果给服务器吗？
    8. Warning : 警告码：通常会告知用户一些与换成相关的问题的警告 
```

11 Http/1.1 请求首部字段: 用体育补充请求的附加信息、客户端信息、对想要内容相关的优先级等内容
```text
    1.Accept:  通知服务器，用户代理能够处理的媒体类型及媒体类型的相对优先级
    2.Accept-Charset:用户代理支持的字符集及字符集的相对优先顺序。
    3.Accept-Enconding:告知服务器5用户代理支持的内容编码及内容编码的优先级顺序。
        a.gzip GNU zip 生成的编码格式
        b.compress 由UNIX文件压缩程序compress生成的编码格式，采用Lempel-ziv-welch算法
        c.deflate 组合使用zlib格式(RFC1950)及由deflate压缩算法生成的编码格式
        d.identity:不执行压缩或不会变化的默认编码格式
    4. Accept-Language: 响应语言
    5. Authorization : 用户代理的认证信息
    6. Expect：100-continue
    7. Host: 首部字段Host会告知服务器，在请求的资源所处的互联网主机名和端口号。（解决虚拟主机运行在统一个IP上的问题）
    8. If-Match : If 类型的都是称为条件请求。只有 If-Match 字段与Etag值匹配一致时，服务器才会接受请求。
        还有其他各种If-*** 知道就好吧，用到时再来查询
    9. Max-Forwards : 指定可经过服务器的最大数目？？？ 服务器概念是什么？ 用于检查代理服务器 是否出现故障？
    10. proxy-authorization  客户端与代理服务器之间的认证
    11. Range: 指定获取部分资源的范围请求
    12. Referer : 告知服务器请求的原始资源的URI。
    13. TE 指定传输编码方式
    14. User-Agent: 用于传达浏览器的种类。
```
##### 既然有标准的头部信息，那么可以写个脚本用于检查非标准的头部信息。看下服务器加了那些内容？

12. 响应首部字段
```text
   1. Accept-Ranges: 当不能处理范围请求时， Accept-Ranges:none
   2. Age: 源服务器多久前创立了响应
   3. ETag: 由服务器对资源进行分配对应的ETag 指定资源吗？
   4. Location: 重定向。 配置3xx: redirect的相应，提供重定向的URI。几乎所有浏览器接受到包含首字段的想以后，都会强制性地尝试对已提示的重定向资源的访问
   5. Proxy-Authenticate : 会把由代理服务器所要求的认真信息发送给客户端
   6. Retry-After: 客户端应该在多久之后再次发送请求。
   7. Server: 告知客户端服务器上安装的HTTP服务器应用程序的信息
   8. Vary: 
```

13 实体首部字段
```text
    1.Allow: 用于通知客户端能够支持的request-Uri 指定的资源的所有HTTP方法
    2.Content-Encoding: gzip
    3.Content-Location: 与Head的 Location 不同这里的作用是，content 内容对应的链接，比如访问不同语言版本时，所对应的页面
    4.Content-MD5:加密字段
    5.Content-Length:
    6.Content-Range:
    7.Content-Type:text/html; charset=Utf-8
    8.Expires: 资源失效的日期告知客户端
    9.Last-modified: 资源最终修改的时间
```

14 为Cookie 服务的首部字段
```text
1.Set-Cookie
    a.Name :  赋予Cookie的名称和字符
    b.expires: 发送Cookie的有效期
    c.path:  知道Cookie的发送范围的文件目录
    d.domain:
    e: secure 属性： https安全链接时，才可以发送COOKIE
    f: httponly: cookie不能通过js获得，防止XSS中利用JAVASCRIPT劫持Cookie
2.cookie
    cookie:status = enable?

```

15 其他首部字段
```text
1.X-Frame-Options: deny 拒绝， Sameorigin 同源页面匹配时许可： web服务器端预先设定好
2.X-XSS-Protection：1 控制浏览器XSS防护机制的开关
3.DNT Do Not Track 拒绝个人信息被手机，0同意被追踪，1拒绝被中追踪
4.p3p
```

16 https
```text
   ssl 认证方式是通过 一个认证机构来做验证
   顺序:
    1. 服务器向公钥认证机构申请证书
    2. 浏览器开发厂家将公钥认证机构的公钥放在浏览器的客户端中
    3. 客户端申请访问服务器
    4. 服务器下发证书
    5. 客户端将拿到的证书与第三方认证机构进行认证,认证通过有进行加密,并访问服务
    (公钥谁都可以获得,私钥只有自己有)

协议成面:http ssl tcp ip 这样的结构组成了https
也可以使用客户端验证,比如银行的U盾等
另外一种是:自签名证书
--------------------------------------------
    但是:这个验证机制也很容易被破坏,比如浏览器存储的验证机构的密钥破坏,或者认证机构本身出问题.都会导致客户端这边访问不了对应的界面
不过这样好歹,在客户端进行的操作都进行了加密,在流程上并会会出现什么问题.
```
17  确认客访问用户身份
```text
1.基于身份验证
2.基于表单
```



### python 语言学习
1. 参数
```python
   # 可变参数
    def func1(*k, **kw):
        print(k, kw)
```

2. 装饰器
```python
   ## 装饰器语法
    import functools
    def log(func):
        @functools.wrapper(func) 
        def wrapper(*args, **kw):
            print('call() %s:' % func.__name__)
            # 可以将run下载这里
            return func(*args, **kw)
        return wrapper
```
3. @staticmethod和@classmethod装饰器
```text
#理论上是理解了 cls 与 self 面对不同.
#测试发现cls属性 与  self的属性哪怕同名也不是一个东西.
这里有如下一个问题
为什么classmatheod 采用print(Class.classmethod()) 生成一个对象时打印的地址是相同的, 但是id(object1) id(object2)
赋值后他们地址不同?

``` 

4.把函数视作对象
```text
函数是一等公民
1.高阶函数
a.用法记录:
颠倒
def reverse(word):
    return word[::-1]

b.lambda 表达式中不能赋值,也不能使用while和try等Python语句

c.可调用对象: 如果想判断对象是否能调用,可以使用内置的callbale()函数
    1) 用户定义的函数.def lambda表达式
    2) 内置函数 使用C语言实现的函数,如len或time.strftime
    3) 内置方法 使用C语言实现的方法,如dict.get()
    4) 方法: 在类的定义提中定义函数
    6) 类. 调用类时会运行类的__new__方法创建一个实力,然后运行__init__方法,初始化实力,最后把实例返给调用方.因为Python没有new运算符
   ,随意调用类相当于调用函数,通常调用类会创建那个类的实例,不过覆盖__new__方法的话,也可能出现其他行为
    6) 类的实例, 如果类定义了__call__方法,那么他的实例可以作为函数调用.
    7)生成器函数:使用yield关键字的函数或方法.调用生成器函数返回的是生成器对象
```

5.装饰器
```python
#假设有个装饰器
@decorate
def target(): 
    print("running target")
```
与下面这种写法意思相同
```python
def target():
    print('running target()')
target = decorate(target)
```
```text
装饰器两大特性:1.被装饰的函数替换成其他函数
2.装饰器在加载模块时立即执行.
```

5.1 何时执行装饰器
```text
他们在被装饰的函数定义之后立即运行.这通常是在导入时(python moudles 加载)
函数装饰器在导入模块时立即执行,而被装饰的函数只在明确调用时运行,在突出了python程序员所说的导入时和运行时之间的区别
```
5.2 使用策略模式改进"策略"模式
```python
promos = []
def promotion(promo_func):
    promos.append(promo_func)
    return promo_func
```
5.3 变量作用域规则
(和多人把闭包和匿名函数弄混),其实 闭包指延伸了作用域的函数,其中包含函数定义体中的引用
#####在函数体中对变量赋值(= 会修改变量的作用域 为本地), 用global避免, 在闭包中用nonlocal
functools.wrps(func) 保存函数原来的名称

 
###scrapy笔记

1. 自带的CookiesMiddelware中间件, 需要配置COOKIES_ENABLED 与 COOKIES_DEBUG 属性, 使用是观察一下用法
2. errback 这个的使用方式是怎样的? 如果发现报错如何进行区分.直接在这里吗?  如果用这个机制是可以避免用retry
可以直接重新发起请求
Using errbaks to catch exceptions in request processing
3. CrawlerRunner 和 CrawlerProcess 有什么区别? 
4. spider middleware 的好处是什么, 返回的还是response 吗?
5. Mutiple cookies seeions per spider, 用cookiejar Request meta key实现
6. 请求的失败的流程如何来模拟, 比如最终response 返回的界面 并不是需要的. middleware 抛出异常后可以直接返回request
request这里如何告知middleware 代理需要更换,如何来告知呢? 
a. 不同的爬虫middleware过滤,可以在middle里面写
b. 可以给request对象里面添加新的变量来说明. 还有没有其他更好的方式呢? 
c. 另外为了节约IP,减少代理IP的请求次数, 需要用retry. retry 多少次以后,才抛出异常吗? retry的判断标准是怎样? 
d. retry 如何修改retry的条件 (继承吗). 还是需要修改retry


```text
CREATE TABLE IF NOT EXISTS `douban_movie`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `title` VARCHAR(40) NOT NULL,
   `category` VARCHAR(40) NOT NULL,
   `show_date` VARCHAR(40) NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

```