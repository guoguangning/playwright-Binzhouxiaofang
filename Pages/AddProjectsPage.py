"""
-*- coding: utf-8 -*-
@File    : AddProjectsPage.py
@Date    : 2024/10/16 10:02
@Author  : ggn
"""
import time
from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("AddProjectsPage").get_log()


class AddProjectsPage(BasePage):
    """新建建设工程页面操作"""
    data = load_and_validate_yaml(r'C:\case\playwright_BinZhouXiaoFang\TestDatas\EleData\AddProjectsPage.yaml')

    def goto_add_projects(self):
        try:
            self._goto_url(self.data['path'])
            logger.info("Navigating to AddDesignReviewPage")
        except Exception as e:
            logger.error(f"Failed to open AddDesignReviewPage: {e}")
            raise

    def click_xf(self) -> None:
        try:
            self._click(self.data['xf'])
            logger.info("Clicking xf")
        except Exception as e:
            logger.error(f"Failed to click xf: {e}")
            raise

    def click_new_construction_design_review(self) -> None:
        """新建建设工程消防设计审查"""
        try:
            self._click(self.data['new_construction_design_review'])
            logger.info("Clicking new_construction_design_review")
        except Exception as e:
            logger.error(f"Failed to click new_construction_design_review: {e}")
            raise

    def click_new_inspection(self) -> None:
        """新建建设工程消防验收"""
        try:
            self._click(self.data['new_inspection'])
            logger.info("Clicking new_inspection")
        except Exception as e:
            logger.error(f"Failed to click new_inspection: {e}")
            raise

    def click_new_record(self) -> None:
        """新建建设工程消防备案"""
        try:
            self._click(self.data['new_record'])
            logger.info("Clicking new_record")
        except Exception as e:
            logger.error(f"Failed to click new_record: {e}")
            raise

    def select_project_name(self) -> None:
        """选择项目"""
        try:
            self._click(self.data['select_project_name'], self.data['iframe'])
            time.sleep(1)
            self._click(self.data['select_project'], self.data['iframe'])
            time.sleep(1)
            self._click(self.data['confirm_button'], self.data['iframe'])
            logger.info("select_project_name")
        except Exception as e:
            logger.error(f"Failed to select_project_name: {e}")
            raise

    def select_engineering_name(self) -> None:
        """选择工程"""
        try:
            self._click(self.data['select_engineering_name'], self.data['iframe'])
            time.sleep(1)
            self._click(self.data['select_engineering'], self.data['iframe'])
            time.sleep(1)
            self._click(self.data['confirm_engineering_button'], self.data['iframe'])
            logger.info("select_engineering_name")
        except Exception as e:
            logger.error(f"Failed to select_engineering_name: {e}")
            raise

    def select_category(self) -> None:
        """选择类别"""
        try:
            self._select_options(self.data['category'],
                                 *self.data['select_category'], frame_locator=self.data['iframe'])
            logger.info("Selector category")
        except Exception as e:
            logger.error(f"Failed to Selector category：{e}")
            raise

    def select_category2(self) -> None:
        """选择类别"""
        try:
            self._select_options(self.data['category'],
                                 *self.data['select_category2'], frame_locator=self.data['iframe'])
            logger.info("Selector category")
        except Exception as e:
            logger.error(f"Failed to Selector category：{e}")
            raise

    def select_using_properties(self) -> None:
        """建筑工程使用属性"""
        try:
            self._fill_select(self.data['using_properties'],
                              self.data['select_using_properties'], frame_locator=self.data['iframe'])
            logger.info("Selector using_properties")
        except Exception as e:
            logger.error(f"Failed to Selector using_properties：{e}")
            raise

    def click_is_general_project(self) -> None:
        """选择是否为一般项目：是"""
        try:
            self._click(self.data['is_general_project'], self.data['iframe'])
            logger.info("Clicking is_general_project")
        except Exception as e:
            logger.error(f"Failed to click is_general_project: {e}")
            raise

    def click_no_general_project(self) -> None:
        """选择是否为一般项目：否"""
        try:
            self._click(self.data['no_general_project'], self.data['iframe'])
            logger.info("Clicking no_general_project")
        except Exception as e:
            logger.error(f"Failed to click no_general_project: {e}")
            raise

    def click_general_project_types(self) -> None:
        """选择一般项目类型"""
        try:
            self._click(self.data['general_project_types'], self.data['iframe'])
            logger.info("Clicking general_project_types")
        except Exception as e:
            logger.error(f"Failed to click general_project_types: {e}")
            raise

    def click_application_method(self) -> None:
        """选择申报方式"""
        try:
            self._click(self.data['application_method'], self.data['iframe'])
            logger.info("Clicking application_method")
        except Exception as e:
            logger.error(f"Failed to click application_method: {e}")
            raise

    def click_related_matters(self) -> None:
        """选择关联政务网事项"""
        try:
            self._click(self.data['related_matters'], self.data['iframe'])
            logger.info("Clicking related_matters")
        except Exception as e:
            logger.error(f"Failed to click related_matters: {e}")
            raise

    def click_add_construction_design_review_button(self) -> None:
        """新建建设工程消防设计审查 创建按钮"""
        try:
            self._click(self.data['add_construction_design_review_button'], self.data['iframe'])
            logger.info("Clicking 创建完毕并发送至帮办")
        except Exception as e:
            logger.error(f"Failed to click 创建完毕并发送至帮办: {e}")
            raise

    def click_added_button(self) -> None:
        """
        新建建设工程消防验收 创建按钮
        新建建设工程消防备案 创建按钮
        :return:
        """
        try:
            self._click(self.data['added'], self.data['iframe'])
            logger.info("Clicking 创建完毕")
        except Exception as e:
            logger.error(f"Failed to click 创建完毕: {e}")
            raise

    def click_ok_button(self):
        try:
            if self._ele_to_be_expect(self.data['expected'], self.data['expected_text'], self.data['iframe']):
                self._click(self.data['ok_button'], self.data['iframe'])
                logger.info("Clicking 创建完毕并发送至帮办提示：二次确认按钮")
                return True
        except Exception as e:
            logger.error(f"Failed to click 创建完毕并发送至帮办提示：二次确认按钮: {e}")
            return False

    def click_ok_inspection_button(self):
        """新建建设工程消防验收"""
        try:
            if self._ele_to_be_expect(self.data['expected'], self.data['expected_text_inspection'], self.data['iframe']):
                self._click(self.data['ok_button'], self.data['iframe'])
                logger.info("Clicking 创建完毕提示：二次确认按钮")
                return True
        except Exception as e:
            logger.error(f"Failed to click 创建完毕提示：二次确认按钮: {e}")
            return False

    def click_ok_record_button(self):
        """新建建设工程消防备案"""
        try:
            if self._ele_to_be_expect(self.data['expected'], self.data['expected_text_record'], self.data['iframe']):
                self._click(self.data['ok_button'], self.data['iframe'])
                logger.info("Clicking 创建完毕提示：二次确认按钮")
                return True
        except Exception as e:
            logger.error(f"Failed to click 创建完毕提示：二次确认按钮: {e}")
            return False
