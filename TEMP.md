# 接口参数说明  /kettle/executeTrans/

文档地址：https://help.pentaho.com/Documentation/8.2/Developer_Center/REST_API/Carte/020

源码地址：https://github.com/pentaho/pentaho-kettle/blob/master/engine/src/main/java/org/pentaho/di/www/ExecuteTransServlet.java

看源码猜测，会到物理磁盘地址去找转换文件。

根据源码反向推测，需要 rep 这个库的名称，没有库用 ""

rep: '',
trans: '/home/santa/test.ktr',
level: 'Debug',
orgId: '9996',
month: '2018-03'

参数说明：
rep：库id
trans：转换的地址（真实的物理地址，如：file:////home/santa/test.ktr）
orgId，month 为转换使用的参数
