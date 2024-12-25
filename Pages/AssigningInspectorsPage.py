"""
-*- coding: utf-8 -*-
@File    : AssigningInspectorsPage.py
@Date    : 2024/11/13 16:19
@Author  : ggn
"""
from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("AssigningInspectorsPage").get_log()


class AssigningInspectorsPage(BasePage):
    """分配检查人员页面操作"""
    data = load_and_validate_yaml(r'..\TestDatas\EleData\AssigningInspectorsPage.yaml')
    data_acceptance = data[0]
    data_record = data[1]

    def goto_assigning_inspectors_page(self):
        try:
            self._goto_url(self.data_acceptance['path'])
            logger.info("Navigating to AssigningInspectorsPage")
        except Exception as e:
            logger.error(f"Failed to open AssigningInspectorsPage: {e}")
            raise

    def click_xf(self) -> None:
        try:
            self._click(self.data_acceptance['xf'])
            logger.info("Clicking xf")
        except Exception as e:
            logger.error(f"Failed to click xf: {e}")
            raise

    def click_construction_acceptance_list(self) -> None:
        """建设工程消防验收项目列表"""
        try:
            self._click(self.data_acceptance['construction_acceptance_list'])
            logger.info("Clicking construction_acceptance_list")
        except Exception as e:
            logger.error(f"Failed to click construction_acceptance_list: {e}")
            raise

    def click_record_list(self) -> None:
        """建设工程消防验收备案项目列表"""
        try:
            self._click(self.data_record['record_list'])
            logger.info("Clicking record_list")
        except Exception as e:
            logger.error(f"Failed to click record_list: {e}")
            raise

    def click_enter_project_page(self) -> None:
        """进入项目页面"""
        try:
            self._click(self.data_acceptance['enter_project_page'], self.data_acceptance['iframe'])
            logger.info("Clicking enter_project_page")
        except Exception as e:
            logger.error(f"Failed to click enter_project_page: {e}")
            raise

    def click_assigning_inspectors_acceptance(self) -> None:
        """分配检查人员-Y4"""
        try:
            self._click(self.data_acceptance['assigning_inspectors'], self.data_acceptance['iframe'])
            logger.info("Clicking assigning_inspectors")
        except Exception as e:
            logger.error(f"Failed to click assigning_inspectors: {e}")
            raise

    def click_assigning_inspectors_records(self) -> None:
        """分配检查人员-BJ1"""
        try:
            self._click(self.data_record['assigning_inspectors_record'], self.data_record['iframe'])
            logger.info("Clicking assigning_inspectors_record")
        except Exception as e:
            logger.error(f"Failed to click assigning_inspectors_record: {e}")
            raise

    def click_assign_personnel(self) -> None:
        """分配人员"""
        try:
            self._click(self.data_acceptance['assign_personnel'], self.data_acceptance['iframe2'])
            logger.info("Clicking assign_personnel")
        except Exception as e:
            logger.error(f"Failed to click assign_personnel: {e}")
            raise

    def click_assigned(self) -> None:
        """分配完毕"""
        try:
            self._click(self.data_acceptance['assigned'], self.data_acceptance['iframe2'])
            logger.info("Clicking assigned")
        except Exception as e:
            logger.error(f"Failed to click assigned: {e}")
            raise

    def assert_assigning_inspectors(self):
        """分配完成断言"""
        try:
            self._ele_to_be_expect(self.data_acceptance['expect'], self.data_acceptance['expected_text'], self.data_acceptance['iframe2'])
            return True
        except Exception as e:
            logger.error(f"Failed to click deputy_service_completed: {e}")
            return False

