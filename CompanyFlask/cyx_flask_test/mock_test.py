#coding=UTF-8
#remark= mock 2.2APP精选推荐/ext/ws/p2p/wealth/app

from unittest.mock import Mock
import requests,json
import unittest

url = 'http://172.30.2.17:30317/p2p/ext/ws/p2p/wealth/app'
data = {
	"params": {
		"userId": "U2539995091711557640"
	}
}
header = {
    'Content-Type':'application/json',
    'charset':'UTF-8'
          }
def post_request(url,data):
    res = requests.post(url,json=data)
    return res.text

print(post_request(url,data))