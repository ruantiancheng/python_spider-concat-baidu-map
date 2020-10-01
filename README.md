# python_spider-gets-the-grayscale-image
通过旧版百度地图编辑器获取自定义样式各精细度的瓦片地图
======
基本步骤可以划分为以下3个步骤：
--------
1.找到未加密入口提取瓦片地图URL<br> 
2.确定URL的变化规律<br> 
3.利用确定的URL变化规律通过Python循环爬取瓦片地图<br> 
4.对于爬取的瓦片地图进行拼接<br> 

一、找到未加密入口提取瓦片地图URL
--------------
  1.由于标准版百度地图对于源文件的URL的加密导致其URL规律难以确定，因此建议是从未加密的入口选定需获取地图的位置，以下提供四个比较不错的入口<br> 
    A.进入旧版百度地图个性在线编辑器（⭐推荐，自定义样式多，提取图片可直接用）https://developer.baidu.com/map/custom/<br> 
    B.通过限制带宽在进入百度地图的时候，通过弹出的切换为简化版提示进入简化版百度地图 https://map.baidu.com<br> 
    C.利用外部调用百度地图的网页（也就是已经对百度地图加密URL进行解密的地图网页）https://hotel.qunar.com/<br> 
    D.百度的坐标拾取系统（可以依据坐标精确定位范围，适用后续应用需要坐标锚定的）http://api.map.baidu.com/lbsapi/getpoint/index.html<br> 
  2.获取目标瓦片地图的URL<br> 
    1.浏览器通过【F12】打开开发者模式<br> 
    2.在顶部选项卡选择【Network】，缩放或移动地图让新的瓦片图加载<br> 
    3.在左侧窗格【Name】里找到含“tile”字样且格式为图片格式的项，点击并在右侧窗格【Preview】里进行预览(见下图1)<br> 
    4.将右侧窗格的【Preview】切换至【Headers】，提取红框圈出的【Request URL】<br> 
    

