"""
-*- coding: utf-8 -*-
@File    : DeputyPage.py
@Date    : 2024/10/17 11:15
@Author  : ggn
"""
import time
from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("DeputyPage").get_log()


class DeputyPage(BasePage):
    """帮办页面操作"""
    data = load_and_validate_yaml(r'..\TestDatas\EleData\DeputyPage.yaml')

    def goto_deputy_page(self):
        try:
            self._goto_url(self.data['path'])
            logger.info("Navigating to DeputyPage")
        except Exception as e:
            logger.error(f"Failed to open DeputyPage: {e}")
            raise

    def click_xf(self) -> None:
        try:
            self._click(self.data['xf'])
            logger.info("Clicking xf")
        except Exception as e:
            logger.error(f"Failed to click xf: {e}")
            raise

    def click_construction_design_review_list(self) -> None:
        """建设工程消防设计审查项目列表"""
        try:
            self._click(self.data['construction_design_review_list'])
            logger.info("Clicking construction_design_review_list")
        except Exception as e:
            logger.error(f"Failed to click construction_design_review_list: {e}")
            raise

    def click_enter_project_page(self) -> None:
        """进入项目页面"""
        try:
            self._click(self.data['enter_project_page'], self.data['iframe'])
            logger.info("Clicking enter_project_page")
        except Exception as e:
            logger.error(f"Failed to click enter_project_page: {e}")
            raise

    def click_deputy(self) -> None:
        """点击帮办S1"""
        try:
            self._hover(self.data['deputy'], self.data['iframe'])
            self._click(self.data['deputy'], self.data['iframe'])
            logger.info("Clicking deputy")
        except Exception as e:
            logger.error(f"Failed to click deputy: {e}")
            raise

    def click_upload_file_configuration(self) -> None:
        """上传文件配置"""
        try:
            self._click(self.data['upload_file_configuration'], self.data['iframe2'])
            self._click(self.data['no_upload_required'], self.data['iframe2'])
            self._click(self.data['no_upload_required2'], self.data['iframe2'])
            self._click(self.data['no_upload_required3'], self.data['iframe2'])
            self._click(self.data['no_upload_required4'], self.data['iframe2'])
            self._click(self.data['no_upload_required_button'], self.data['iframe2'])
            logger.info("Clicking upload_file_configuration")
        except Exception as e:
            logger.error(f"Failed to click upload_file_configuration: {e}")
            raise

    def click_deputy_suggestion(self, value) -> None:
        """帮办建议"""
        try:
            self._click(self.data['deputy_suggestion'], self.data['iframe2'])
            self._fill(self.data['deputy_suggestion_input'], value, self.data['iframe2'])
            self._click(self.data['sure_button'], self.data['iframe2'])
            self._click(self.data['ok_button'], self.data['iframe2'])
            logger.info("Clicking deputy_suggestion")
        except Exception as e:
            logger.error(f"Failed to click deputy_suggestion: {e}")
            raise

    def click_deputy_service_completed(self) -> None:
        """帮办服务完成"""
        try:
            self._click(self.data['deputy_service_completed'], self.data['iframe2'])
            if self._ele_to_be_expect(self.data['expected'], self.data['expected_text'], self.data['iframe2']):
                self._click(self.data['confirm_button'], self.data['iframe2'])
            logger.info("Clicking deputy_service_completed")
        except Exception as e:
            logger.error(f"Failed to click deputy_service_completed: {e}")
            raise

    def ele_assert_deputy(self):
        """帮办完成断言"""
        try:
            self._ele_to_be_expect(self.data['expected_'], self.data['expected_text_'], self.data['iframe2'])
            logger.info("ele_assert_deputy")
            return True
        except Exception as e:
            logger.error(f"Failed to ele_assert_deputy: {e}")
            return False
