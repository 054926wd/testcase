使用方法：
1、通过excel实现数据驱动
browser：浏览器，通过传入不同的浏览器，启动相应的浏览器，当浏览器启动失败时，默认启动谷歌浏览器
max_web：将浏览器界面最大化，该方法不需要传入参数
open：该方法通过传入的ip地址打开相应的网站，传入的地址一定要是完整，如http://www.baidu.com
locator:该方法为元素定位，不需要通过excel传值
    1）定位方法：id,name,xpath,class
    2）定位值：在浏览器通过f12查找
input：该方法为输入操作，需要传入三个值，除了定位方法和定位值外，还需要传入一个输入的值
click：该方法为点击操作，只需要传入定位方法和定位值
table：该方法为切换标签页，直接调用即可，不需要传值
mouse：该方法为鼠标悬停操作，只需要传入定位方法和定位值
scroll：该方法为屏幕滚动，只需要传入定位方法和定位值
screenshot：该方法为屏幕截图操作，直接调用即可，不需要传值
refresh：该方法为页面刷新，直接调用即可，不需要传值
back：该方法为返回上一页，直接调用即可，不需要传值
quit：该方法为关闭浏览器，直接调用即可，不需要传值
wait：该方法为强制等待，该需要传入等待时间




上传git：
    git branch -M main
    git push -u origin main
