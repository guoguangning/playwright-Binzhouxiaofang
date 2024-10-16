"""
-*- coding: utf-8 -*-
@File    : LoginPage.py
@Date    : 2024/10/15 10:45
@Author  : ggn
"""
from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Util_yaml import load_yaml

logger = Logger("LoginPage").get_log()


class LoginPage(BasePage):
    data = load_yaml(r'C:\case\playwright_BinZhouXiaoFang\TestDatas\EleData\LoginPage.yaml')

    def goto_login(self):
        try:
            self._goto_url(self.data['path'])
            logger.info("Navigating to login page")
        except Exception as e:
            logger.error(f"Failed to open login page: {e}")
            raise

    def fill_username(self, value: str) -> None:
        try:
            self._fill(self.data['username_selector'], value)
            logger.info("Filling in username")
        except Exception as e:
            logger.error(f"Failed to fill username: {e}")
            raise

    def fill_password(self, value: str) -> None:
        try:
            self._fill(self.data['password_selector'], value)
            logger.info("Filling in password")
        except Exception as e:
            logger.error(f"Failed to fill password: {e}")
            raise

    def click_login_button(self) -> None:
        try:
            self._click(self.data['login_button_selector'])
            logger.info("Clicking login button")
        except Exception as e:
            logger.error(f"Failed to click login button: {e}")
            raise
