# @Time : 2021/2/18 10:36 
# @Author : qiulingfeng
# @File : setup.py.py
from setuptools import setup
setup(
    name='pytest_encode',
    url='https://github.com/xxx/pytest-encode',
    version='1.0',
    author="qiulingfeng",
    author_email='2298294181@qq.com',
    description='set your encoding',
    long_description='Show Chinese for your mark.parametrize().',
    classifiers=[# 分类索引 ，pip 对所属包的分类
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.8',
    ],
    license='proprietary',
    packages=['pytest_encode'],
    keywords=[
        'pytest', 'py.test', 'pytest_encode',
    ],

    # 需要安装的依赖
    install_requires=[
        'pytest'
    ],
    # 入口模块 或者入口函数
    entry_points={
        'pytest11': [
            'pytest-encode = pytest_encode',
        ]
    },
    zip_safe=False
)