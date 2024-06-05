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

###### 使用 pytest 遇到的问题
 - 1.版本不兼容时，运行脚本显示的时 ，waring.需要跟新版本。pytest 8.0.1 与 pytest 8.2.1不兼容
 - 2.使用命令， 执行 pytest + alluer 脚本 pytest.main(['-s', '-v', '--alluredir=./report'])
 - 3.使用 allure 是，会生成 json 文件。 命令可查看 allure serve ./report