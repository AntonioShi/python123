import scrapy

class quote(scrapy.Spider):
    name = "quote"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
            'http://www.budejie.com/text/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log("Saved file %s" %filename)


    # def parse(self, response):
    #     lies = response.css('div.j-r-list >ul >li')
    #     for li in lies:
    #         username = li.css('a.u-user-name::text').extract()
    #         content = li.css('div.j-r-list-c-desc a::text').extract()
    #         yield {'username': username, 'content': content}
    #
    #     page = response.url.split("/")[-1]
    #     filename = 'quotes-%s.json' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log("Saved file %s" % filename)


# 这是一个典型的客户端http请求示例：请求行、请求头部、空行、请求数据
# GET https://www.baidu.com/ HTTP/1.1 请求方法get
# Host: www.baidu.com 请求主机和端口号
# Connection: keep-alive 客户端请求服务器的链接类型
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36
# 浏览器名称

# Accept: text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8
# 传输文件类型Accept: */*：表示什么都可以接收。
#
# Accept：image/gif：表明客户端希望接受GIF图像格式的资源；
#
# Accept：text/html：表明客户端希望接受html文本。
#
# Accept: text/html, application/xhtml+xml;q=0.9, image/*;q=0.8：表示浏览器支持的 MIME 类型分别是 html文本、xhtml和xml文档、所有的图像格式资源。
#
# q是权重系数，范围 0 =< q <= 1，q 值越大，请求越倾向于获得其“;”之前的类型表示的内容。
# 若没有指定q值，则默认为1，按从左到右排序顺序；若被赋值为0，则用于表示浏览器不接受此内容类型。
#
# Text：用于标准化地表示的文本信息，文本消息可以是多种字符集和或者多种格式的；
# Application：用于传输应用程序数据或者二进制数据。详细请点击



# Referer: http://www.baidu.com/ 页面跳转处
# Referer：表明产生请求的网页来自于哪个URL，用户是从该 Referer页面访问到当前请求的页面。
# 这个属性可以用来跟踪Web请求来自哪个页面，是从什么网站来的等。
# 有时候遇到下载某网站图片，需要对应的referer，否则无法下载图片，那是因为人家做了防盗链，
# 原理就是根据referer去判断是否是本网站的地址，如果不是，则拒绝，如果是，就可以下载；


# Accept-Encoding: gzip, deflate, sdch, br 文件编解码格式，指出浏览器可以接受的编码方式
# Accept-Language: zh-CN,zh;q=0.8,en;q=0.6 语言种类 en或en-us指英语，zh或者zh-cn指中文
# Cookie: BAIDUID=04E4001F34EA74AD4601512DD3C41A7B:FG=1; BIDUPSID=04E4001F34EA74AD4601512DD3C41A7B; PSTM=1470329258; MCITY=-343%3A340%3A; H_PS_PSSID=1447_18240_21105_21386_21454_21409_21554; BD_UPN=12314753; sug=3; sugstore=0; ORIGIN=0; bdime=0; H_PS_645EC=7e2ad3QHl181NSPbFbd7PRUCE1LlufzxrcFmwYin0E6b%2BW8bbTMKHZbDP0g; BDSVRTM=0
#cookie浏览器用这个属性向服务器发送cookie

# # 服务器http响应：状态行、消息报头、空行、响应正文
# HTTP/1.1 200 OK  状态码
# Server: Tengine
# Connection: keep-alive
# Date: Wed, 30 Nov 2016 07:58:21 GMT
# Cache-Control: no-cache
# Content-Type: text/html;charset=UTF-8
# Keep-Alive: timeout=20
# Vary: Accept-Encoding
# Pragma: no-cache
# X-NWS-LOG-UUID: bd27210a-24e5-4740-8f6c-25dbafa9c395
# Content-Length: 180945
#
# <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" ....