# @Time : 2021/2/18 10:32 
# @Author : qiulingfeng
# @File : __init__.py.py
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode_escape')
