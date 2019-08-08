#-*- coding:utf-8 -*-
from jpype import *

startJVM(getDefaultJVMPath(), "-Djava.class.path=e:/anaconda/lib/site-packages/pyhanlp/static/hanlp-1.7.4.jar;e:/anaconda/lib/site-packages/pyhanlp/static",
        "-Xms1g",
     "-Xmx1g") # 启动JVM，Linux需替换分号;为冒号:



print("=" * 30 + "HanLP分词" + "=" * 30)
HanLP = JClass('com.hankcs.hanlp.HanLP')
# 中文分词
print(HanLP.segment('你好，欢迎在Python中调用HanLP的API'))
print("-" * 70)