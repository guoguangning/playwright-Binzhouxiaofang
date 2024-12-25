"""
-*- coding: utf-8 -*-
@File    : TestAssigningInspectors.py
@Date    : 2024/11/13 16:26
@Author  : ggn
"""
import pytest
from BasePage.logger import Logger
from Pages.AssigningInspectorsPage import AssigningInspectorsPage
from TestCases.Base import Base
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("TestAssigningInspectors").get_log()


class TestAssigningInspectors(object):
    yaml_data = load_and_validate_yaml(r'..\TestDatas\ParamData\Login.yaml')
    login_data = yaml_data[1]

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = Base(page)
        self.login.login(self.login_data)
        self.test_AssigningInspectors = AssigningInspectorsPage(page)

    @pytest.mark.run(order=3)
    def test_assigning_inspectors_acceptance(self):
        """
        测试分配查验人员 消防验收
        """
        try:
            self._navigate_to_assigning_inspectors()
            self._assigning_inspectors_acceptance()
            if self._assert_assigning_inspectors():
                logger.info('分配查验人员完成')
        except Exception as e:
            logger.error(f"分配查验人员失败: {e}")
            raise

    @pytest.mark.run(order=3)
    def test_assigning_inspectors_record(self):
        """
        测试分配查验人员 消防验收备案
        """
        try:
            self._navigate_to_assigning_inspectors()
            self._assigning_inspectors_record()
            if self._assert_assigning_inspectors():
                logger.info('分配查验人员完成')
        except Exception as e:
            logger.error(f"分配查验人员失败: {e}")
            raise

    def _navigate_to_assigning_inspectors(self):
        self.test_AssigningInspectors.goto_assigning_inspectors_page()
        self.test_AssigningInspectors.click_xf()

    def _assigning_inspectors_acceptance(self):
        self.test_AssigningInspectors.click_construction_acceptance_list()
        self.test_AssigningInspectors.click_enter_project_page()
        self.test_AssigningInspectors.click_assigning_inspectors_acceptance()
        self.test_AssigningInspectors.click_assign_personnel()
        self.test_AssigningInspectors.click_assigned()

    def _assigning_inspectors_record(self):
        self.test_AssigningInspectors.click_record_list()
        self.test_AssigningInspectors.click_enter_project_page()
        self.test_AssigningInspectors.click_assigning_inspectors_records()
        self.test_AssigningInspectors.click_assign_personnel()
        self.test_AssigningInspectors.click_assigned()

    def _assert_assigning_inspectors(self):
        try:
            self.test_AssigningInspectors.assert_assigning_inspectors()
            return True
        except Exception as e:
            logger.error(f"断言失败: {e}")
            return False


if __name__ == '__main__':
    pytest.main(['-v', __file__])
