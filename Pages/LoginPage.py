"""
-*- coding: utf-8 -*-
@File    : LoginPage.py
@Date    : 2024/10/15 10:45
@Author  : ggn
"""
from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("LoginPage").get_log()


class LoginPage(BasePage):
    data = load_and_validate_yaml(r'..\playwright-Binzhouxiaofang\TestDatas\EleData\LoginPage.yaml')

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

    def ele_assert_login(self):
        try:
            # 验证第一个期望元素
            if self._ele_to_be_expect(self.data['expected']):
                logger.info("Expected element found.")
                return True

            # 验证第二个期望元素及其文本
            if self._ele_to_be_expect(self.data['expected_no'], self.data['expected_text']):
                logger.info("Expected element with text found.")
                return True

            # 验证第三个期望元素及其文本
            if self._ele_to_be_expect(self.data['expected_no'], self.data['expected_text_2']):
                logger.info("Expected element with text2 found.")
                return True

            # 如果所有期望元素都未找到
            logger.warning("None of the expected elements found.")
            return False

        except Exception as e:
            logger.error(f"Failed to ele_assert_login: {e}")
            return False
