"""
-*- coding: utf-8 -*-
@File    : OnSiteAssessmentPage.py
@Date    : 2024/11/14 10:58
@Author  : ggn
"""
from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("OnSiteAssessmentPage").get_log()


class OnSiteAssessmentPage(BasePage):
    """分配检查人员页面操作"""
    data = load_and_validate_yaml(r'..\TestDatas\EleData\OnSiteAssessmentPage.yaml')

    def goto_on_site_assessment_page(self):
        try:
            self._goto_url(self.data['path'])
            logger.info("Navigating to OnSiteAssessmentPage")
        except Exception as e:
            logger.error(f"Failed to open OnSiteAssessmentPage: {e}")
            raise

    def click_xf(self) -> None:
        try:
            self._click(self.data['xf'])
            logger.info("Clicking xf")
        except Exception as e:
            logger.error(f"Failed to click xf: {e}")
            raise

    def click_construction_acceptance_list(self) -> None:
        """建设工程消防验收项目列表"""
        try:
            self._click(self.data['construction_acceptance_list'])
            logger.info("Clicking construction_acceptance_list")
        except Exception as e:
            logger.error(f"Failed to click construction_acceptance_list: {e}")
            raise

    def click_enter_project_page(self) -> None:
        """进入项目页面"""
        try:
            self._click(self.data['enter_project_page'], self.data['iframe'])
            logger.info("Clicking enter_project_page")
        except Exception as e:
            logger.error(f"Failed to click enter_project_page: {e}")
            raise

    def click_on_site_assessment(self) -> None:
        """现场评定-Y5"""
        try:
            self._click(self.data['on_site_assessment'], self.data['iframe'])
            logger.info("Clicking on_site_assessment")
        except Exception as e:
            logger.error(f"Failed to click on_site_assessment: {e}")
            raise

    def click_spot_check(self) -> None:
        """建设工程消防验收现场抽查情况"""
        try:
            self._click(self.data['spot_check'], self.data['iframe2'])
            logger.info("Clicking spot_check")
        except Exception as e:
            logger.error(f"Failed to click spot_check: {e}")
            raise

    def click_to_pre_generated_documents(self) -> None:
        """转预生成文书"""
        try:
            self._click(self.data['to_pre_generated_documents'], self.data['iframe2'])
            self._ele_to_be_expect(self.data['expect'], self.data['expect_text'], self.data['iframe2'])
            self._click(self.data['sure_button'], self.data['iframe2'])
            logger.info("Clicking to_pre_generated_documents")
        except Exception as e:
            logger.error(f"Failed to click to_pre_generated_documents: {e}")
            raise
