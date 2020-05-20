''' 
================================================================================================
The main file will iterate through this dictionary and use a random user-agent to stay undetected.
No need to touch this unless you know what you are doing.

=====================================================================
'''
header_dict =  {0:  {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}, 
                1:  {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}, 
                2:  {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}, 
                3:  {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)'}, 
                4:  {'User-Agent':'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)'}, 
                5:  {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'}, 
                6:  {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0;  Trident/5.0)'}, 
                7:  {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MDDCJS)'}, 
                8:  {'User-Agent':'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}, 
                9:  {'User-Agent':'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4'}, 
                10: {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}, 
                11: {'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}, 
                12: {'User-Agent':'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)'}, 
                13: {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G570Y Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36'}, 
                14: {'User-Agent':'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900 Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36'}, 
                15: {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-N910F Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36'}, 
                16: {'User-Agent':'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7'}, 
                17: {'User-Agent':'Mozilla/5.0 (Linux; Android 7.0; HTC 10 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36'}, 
                18: {'User-Agent':'curl/7.35.0'}, 
                19: {'User-Agent':'Wget/1.15 (linux-gnu)'},
                20: {'User-Agent':'Lynx/2.8.8pre.4 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.12.23'},
                21: {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                22: {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                23: {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                24: {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                25: {'User-Agent':'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                26: {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                27: {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0;  Trident/5.0)', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                28: {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MDDCJS)', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                29: {'User-Agent':'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                30: {'User-Agent':'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                31: {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                32: {'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                33: {'User-Agent':'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                34: {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G570Y Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                35: {'User-Agent':'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900 Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                36: {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-N910F Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                37: {'User-Agent':'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                38: {'User-Agent':'Mozilla/5.0 (Linux; Android 7.0; HTC 10 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                39: {'User-Agent':'curl/7.35.0', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                40: {'User-Agent':'Wget/1.15 (linux-gnu)', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                41: {'User-Agent':'Lynx/2.8.8pre.4 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.12.23', 'Referer': 'https://bing.com/', 'Accept-Encoding': 'gzip,deflate,br'},
                42: {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'},
                43: {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                44: {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                45: {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                46: {'User-Agent':'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                47: {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                48: {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0;  Trident/5.0)', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                49: {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MDDCJS)', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                50: {'User-Agent':'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                51: {'User-Agent':'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                52: {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                53: {'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                54: {'User-Agent':'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                55: {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G570Y Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                56: {'User-Agent':'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900 Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                57: {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-N910F Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                58: {'User-Agent':'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                59: {'User-Agent':'Mozilla/5.0 (Linux; Android 7.0; HTC 10 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                60: {'User-Agent':'curl/7.35.0', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                61: {'User-Agent':'Wget/1.15 (linux-gnu)', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'}, 
                62: {'User-Agent':'Lynx/2.8.8pre.4 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.12.23', 'Referer': 'https://google.com/', 'Accept-Encoding': 'gzip,deflate,br'},
}