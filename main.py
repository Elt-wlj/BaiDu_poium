# 执行函数
import pytest
import time
import click
import os


@click.command()
def run():

    now_time = time.strftime("%Y_%m_%d")
    if os.path.exists(now_time):
        os.remove(now_time)
    print(now_time)
    html_report = os.getcwd()+'/report/'+now_time + '.html'
    pytest.main(['-s','-v', './testcase', '--html=' + html_report])


if __name__ == '__main__':
    run()
