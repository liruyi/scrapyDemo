# -*- coding: utf-8 -*-
import os
import urllib
import urllib2

from jiandan import settings

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JiandanPipeline(object):
    def process_item(self, item, spider):
        dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)  # 存储路径
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
            'Cookie': 'AspxAutoDetectCookieSupport=1',
        }

        print 'dir_path', dir_path
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for image_url in item["image_urls"]:
            print 'image_url',image_url
            list_name = image_url.split('/')
            file_name = list_name[len(list_name) - 1]  # 图片名称
            print 'filename', file_name
            file_path = '%s/%s' % (dir_path, file_name)
            print 'filepath', file_path
            if os.path.exists(file_name):
                continue

            with open(file_path,'wb') as file_writer:
                #request = urllib2.Request("http:" + image_url,None,header)
                request = urllib2.Request(image_url, None, header)
                response = urllib2.urlopen(request)
                file_writer.write(response.read())
                file_writer.close();

        return item
