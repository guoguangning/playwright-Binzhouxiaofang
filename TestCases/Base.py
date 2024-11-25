"""
-*- coding: utf-8 -*-
@File    : Base.py
@Date    : 2024/11/7 10:35
@Author  : ggn
"""
from BasePage.BasePage import BasePage
from Pages.LoginPage import LoginPage
from BasePage.logger import Logger

logger = Logger("Base").get_log()


class Base(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_page = LoginPage(page)  # 在 __init__ 中创建 LoginPage 实例

    def login(self, login_data):
        """登录函数"""
        try:
            # 进行登录操作
            self.login_page.goto_login()
            self.login_page.fill_username(login_data['username'])
            self.login_page.fill_password(login_data['password'])
            self.login_page.click_login_button()
            if self.login_page.ele_assert_login():
                logger.info("登录成功")
        except Exception as e:
            logger.error(f"登录失败: {e}")
            raise
