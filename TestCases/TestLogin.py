"""
-*- coding: utf-8 -*-
@File    : TestLogin.py
@Date    : 2024/10/15 10:56
@Author  : ggn
"""
import pytest
from BasePage.logger import Logger
from TestCases.Base import Base
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("TestLogin").get_log()


class TestLogin:
    param_data = load_and_validate_yaml(r'..\playwright-Binzhouxiaofang\TestDatas\ParamData\TestLogin.yaml')

    @pytest.mark.parametrize('login_data', param_data)
    def test_login(self, login_data, page):
        """测试登录功能"""
        self.login = Base(page)
        self.login.login(login_data)


if __name__ == '__main__':
    pytest.main(['-v', __file__])
