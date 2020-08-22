from bs4 import BeautifulSoup
import requests
import csv
import week01.conf as conf
import re

target_url = 'https://maoyan.com/films?showType=3'
result_path = 'result.csv'

cookies = '__mta=218871718.1597917137613.1597984898829.1597984991743.5; uuid_n_v=v1; uuid=D1BE6B10E2CA11EABDF7A52DEC86ABCD95ACFDA7100F49ED9A5286AFB64AF17C; _csrf=4f63ccde404e0d66385bf72119ce437ce1b57a5254c5d0cedb2747ef27230587; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _lxsdk_cuid=1740b487fbdc8-0e988eae82de67-38710758-1fa400-1740b487fbec8; _lxsdk=D1BE6B10E2CA11EABDF7A52DEC86ABCD95ACFDA7100F49ED9A5286AFB64AF17C; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597917135; mojo-uuid=2a44fad21737999981e39807e1e9c368; mojo-session-id={"id":"f42f3886660dd8815fb71756048090c7","time":1598009667656}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598009669; __mta=218871718.1597917137613.1597984991743.1598009669317.6; _lxsdk_s=17410cc7185-cb-535-ca1%7C%7C2'


def header_create():
    # header_create也可能会有不一样的地方。如果不需要登录的可以用这种方法
    # 需要保留cookies则不能这样干
    send_headers = {
        "User-Agent": conf.get_random_agent(),
        "Cookie": cookies
    }
    return send_headers


from requests.cookies import RequestsCookieJar

cookie_jar = RequestsCookieJar()
cookie_jar.set


def http_get_requests_regular(url):
    r = requests.get(url, headers=header_create())
    print(r.text)
    if r.status_code != 200:
        print("requsts err code is {0}".format(r.status_code))
    return r.text


# 分析文本。这里暂时用test.html来测试
def parse_html_by_soup():
    soup = BeautifulSoup(open("test.html"), 'lxml')
    # soup = BeautifulSoup(http_get_requests_regular(target_url), 'lxml')
    requirement_count = 10
    #     所有需要信息都在dd中
    move_info = soup.find_all('div', class_='movie-info')
    hover_info = soup.find_all('div', class_='movie-hover-info')
    single_func = None

    if move_info is not None and len(move_info) != 0:
        print("frontpage type is move_info")
        single_func = get_single_move_info
        pass
    elif hover_info is not None and len(hover_info) != 0:
        print("frontpage type is hove_info")
        move_info = hover_info
        single_func = get_single_hover_info
        pass
    else:
        print("move_info and hover_info items are none")
        return

    if requirement_count > len(move_info):
        requirement_count = len(move_info)

    # result = [single_func(move_info[i]) for i in range(0, requirement_count) if single_func(move_info[i]) is not None]
    result = []
    for i in range(0, requirement_count):
        single_move_info = single_func(move_info[i])
        if single_move_info is None:
            continue
        result.append(single_move_info)

    return result


def get_single_hover_info(hover_item):
    # 以“movie-hover-title为关键字”
    name = hover_item.find('span',class_="name").string.strip()
    hover_titles = hover_item.find_all('span', class_='hover-tag')
    if hover_titles is None or len(hover_titles) < 3 :
        return None
    categroy = hover_titles[0].next_sibling.string.strip()
    show_date = hover_titles[2].next_sibling.string.strip()
    return [name, show_date, categroy]

def get_single_move_info(movie_item):
    name = movie_item.find('div', class_='title').string.strip()
    # 在hover_info中有我需要的所有信息， “movie-hover-title” 子元素里面有需要的所有信息
    # 找名字在可用class=name來
    categroy = movie_item.find('div', class_='actors').string.strip()
    show_date = movie_item.find('div', class_='show-info').string.strip()
    pattern = re.compile('[-0-9]+')
    re_result = pattern.match(show_date)
    if re_result is None:
        return None
    show_date = pattern.match(show_date).group(0)
    return [name, show_date, categroy]


def store_result_to_csv(result):
    if result is None:
        print("reuslt is none when restore ")
        return
    with open(result_path, 'w') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(['title', 'show_date', 'category'])
        csv_write.writerows(result)


store_result_to_csv(parse_html_by_soup())
