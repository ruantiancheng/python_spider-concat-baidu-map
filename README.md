# python_spider-gets-the-grayscale-image
通过旧版百度地图编辑器获取自定义样式各精细度的瓦片地图
======
基本步骤可以划分为以下3个步骤：
--------
    1.找到未加密入口提取瓦片地图URL
    2.确定URL的变化规律
    3.利用确定的URL变化规律通过Python循环爬取瓦片地图
    4.对于爬取的瓦片地图进行拼接

一、找到未加密入口提取瓦片地图URL
--------------
  由于标准版百度地图对于源文件的URL的加密导致其URL规律难以确定，因此建议是从未加密的入口选定需获取地图的位置，以下提供四个比较不错的入口
  -------
    A.进入旧版百度地图个性在线编辑器（⭐推荐，自定义样式多，提取图片可直接用）https://developer.baidu.com/map/custom/
    B.通过限制带宽在进入百度地图的时候，通过弹出的切换为简化版提示进入简化版百度地图 https://map.baidu.com
    C.利用外部调用百度地图的网页（也就是已经对百度地图加密URL进行解密的地图网页）https://hotel.qunar.com/
    D.百度的坐标拾取系统（可以依据坐标精确定位范围，适用后续应用需要坐标锚定的）http://api.map.baidu.com/lbsapi/getpoint/index.html
二、确定URL的变化规律
  -------
    1.浏览器通过【F12】打开开发者模式
    2.在顶部选项卡选择【Network】，缩放或移动地图让新的瓦片图加载
    ![preview](https://github.com/ruantiancheng/python_spider-gets-the-grayscale-image/blob/master/IMage/network_preview.jpg)
    3.在左侧窗格【Name】里找到含“tile”字样且格式为图片格式的项，点击并在右侧窗格【Preview】里进行预览
    4.将右侧窗格的【Preview】切换至【Headers】，提取红框圈出的【Request URL】
    ![preview](https://github.com/ruantiancheng/python_spider-gets-the-grayscale-image/blob/master/IMage/URL.jpg)
    其中直接获取的URL中可以发现使用‘&’符号进行分隔的四段信息&x=789&y=294&z=12&udt=20200928，包括了
    x=789(瓦片图沿横坐标轴（经度）的编号)
    y=294(瓦片图沿纵坐标轴（纬度）的编号)
    z=12（地图缩放尺度，19级最大（能看清室内地图），0级最小（整个地球在一张瓦片图里），18、19级显示建筑轮廓）
    udt=20200928（地图更新的时间）
    基于这四个参数也就可以确定包含所需要提取的地图范围的URL变化规律
三、利用确定的URL变化规律通过Python循环爬取瓦片地图
-------
    1.确定瓦片地图URL变化范围
      A.将地图缩放至需要的地图精细度的前一级（如需要缩放到15级则先调整至14级）
      B.在控制台中的上方清除已经加载的所有内容
      ![preview](https://github.com/ruantiancheng/python_spider-gets-the-grayscale-image/blob/master/IMage/clear.jpg)
      C.通过控制台的previewer找到所需提取的地图范围左上和右下两个顶角的URL（重点就是通过两个顶角地图的x,y属性来确定获取的地图范围）
    2.通过python的request库对于所需提取的瓦片地图进行爬取

