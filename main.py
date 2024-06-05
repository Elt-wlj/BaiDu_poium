# 执行函数
import pytest, shutil
import time
import click
import os

# shutil 是删除目录下有文件的库
file_path = os.path.join(os.getcwd(), 'report')
if os.path.exists(file_path):
    shutil.rmtree(file_path)
else:
    os.mkdir(file_path)


@click.command()
def run():
    # 方法一：只执行 pytest
    # now_time = time.strftime("%Y_%m_%d")
    # if os.path.exists(now_time):
    #     os.remove(now_time)
    # print(now_time)
    # html_report = os.getcwd()+'/report/'+now_time + '.html'
    # pytest.main(['-s', '-v', './testcase', '--html=' + html_report])

    # 方法二：通过pytes + allure 的方式，生成json 的文件,
    # 使用这个命令可以打开：allure serve ./report

    pytest.main(['-s', '-v', '--alluredir=./report'])


if __name__ == '__main__':
    run()
