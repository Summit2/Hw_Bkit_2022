import requests
def make_url(obj):
    base_url='http://127.0.0.1:5000/'
    result_url=base_url+str(obj)
def get_url(obj):
    url=make_url(obj)
    r=requests.get(url)
    return r
