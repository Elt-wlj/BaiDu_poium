###### 项目说明
 - page:是基础元素 定位的页面
 - report:生成测试报告的地方
 - testcase:是存放用能用例的地方
 - conftest.py：文件名不能出错，存放配置文件的地方 


###### poium说明
- 现在定位方式的改变,如以下的表达方式

| 定位    | **kwargs | selector |
|-------|-------|------|
| id    |id_="id" | "id=id" |
| class |class_name="class" | "class=class" |
| link_text    |link_text="文字链接" | "text=文字链接" |
| xpath   |xpath="//*[@id='11']" | "//*[@id='11']" |

- 详细使用说明：https://github.com/SeldomQA/poium/tree/master/sample/selenium_sample

