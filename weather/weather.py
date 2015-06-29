#coding:utf-8

import urllib
import urllib2
import json
import sys

AK = '8a47b6b4cfee5e398e63df510980697e'

BASE_URL = 'http://api.map.baidu.com/telematics/v3/weather?output=json&ak={0}&location='.format(AK)


class BaiduWeather(object):
    def __init__(self,city):
        self.city = city

    #　如果提供了　回调函数　,则由回调函数处理返回的　json　数据
    def query(self,callback=None):
        url = BASE_URL + urllib.quote(self.city)
        html = urllib2.urlopen(url).read()

        json_data = json.loads(html)
        # print json_data.keys()

        if callback:
            callback(json_data)
        else:
            if json_data.get('error') == 0:
                date = json_data.get('date')
                results = json_data.get('results')

                for r in results:
                    print 'pm 2.5 :',r.get('pm25')
                    weather_data = r.get('weather_data')
                    for item in weather_data:
                        print '-'*15
                        print item.get('weather')
                        print item.get('temperature')
                        print item.get('date')
            else:
                print json_data.get('status')


def help():
    print u'\tUsage: python weather.py city_name'
    print u'\texample: python weather.py 天津'



def main():
    if len(sys.argv) != 2:
        help()
    else:
        city = sys.argv[1]
        weather = BaiduWeather(city.decode(sys.stdin.encoding).encode('utf-8'))
        weather.query()

if __name__ == '__main__':
    main()