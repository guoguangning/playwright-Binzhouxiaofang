"""
-*- coding: utf-8 -*-
@File    : ChangePasswordPage.py
@Date    : 2024/10/15 11:07
@Author  : ggn
"""
from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Util_verify import verify
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("ChangePasswordPage").get_log()


class ChangePasswordPage(BasePage):
    data = load_and_validate_yaml(r'..\TestDatas\EleData\ChangePasswordPage.yaml')
    image_path = r'..\TestFiles\code_images.png'

    def goto_change_password(self):
        try:
            self._goto_url(self.data['path'])
            logger.info("Navigating to ChangePassword page")
        except Exception as e:
            logger.error(f"Failed to open ChangePassword page: {e}")
            raise

    def click_forget_password(self) -> None:
        try:
            self._click(self.data['forget_password'])
            logger.info("Clicking forget_password")
        except Exception as e:
            logger.error(f"Failed to Clicking forget_password: {e}")
            raise

    def fill_username(self, value: str) -> None:
        try:
            self._fill(self.data['username_selector'], value)
            logger.info("Filling in username")
        except Exception as e:
            logger.error(f"Failed to fill username: {e}")
            raise

    def fill_graphic_verification_code(self) -> None:
        try:
            # 截图保存验证码图片
            self._screenshot(self.image_path, full_page=False, locator=self.data['graphic_verification_code_image'])
            # 调用 verify 方法获取验证码
            value = verify(self.image_path)
            if value:  # 检查验证码是否成功获取
                self._fill(self.data['graphic_verification_code'], value)
                logger.info("Filling in graphic_verification_code")
            else:
                logger.error("Failed to retrieve the verification code.")
        except Exception as e:
            logger.error(f"Failed to fill graphic_verification_code: {e}")
            raise

    def fill_sms_verification_code(self, value: str) -> None:
        try:
            self._click(self.data['send_SMS_button'])
            self._click(self.data['send_SMS_button_ok'])
            self._fill(self.data['SMS_verification_code'], value)
            logger.info("Filling in SMS_verification_code")
        except Exception as e:
            logger.error(f"Failed to fill SMS_verification_code: {e}")
            raise

    def fill_new_password(self, value: str) -> None:
        try:
            self._fill(self.data['new_password'], value)
            logger.info("Filling in new_password")
        except Exception as e:
            logger.error(f"Failed to fill new_password: {e}")
            raise

    def fill_enter_again_new_password(self, value: str) -> None:
        try:
            self._fill(self.data['enter_again_new_password'], value)
            logger.info("Filling in enter_again_new_password")
        except Exception as e:
            logger.error(f"Failed to fill enter_again_new_password: {e}")
            raise

    def click_submit_button(self) -> None:
        try:
            self._click(self.data['submit_button'])
            self._click(self.data['submit_confirm_button'])
            logger.info("Clicking submit button")
        except Exception as e:
            logger.error(f"Failed to click submit button: {e}")
            raise
