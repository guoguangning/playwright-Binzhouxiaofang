"""
-*- coding: utf-8 -*-
@File    : TestAddProjects.py
@Date    : 2024/10/16 10:40
@Author  : ggn
"""
import time
import pytest
from BasePage.logger import Logger
from Pages.AddProjectsPage import AddProjectsPage
from TestCases.Base import Base
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("TestAddProjects").get_log()


class TestAddProjects(object):
    yaml_data = load_and_validate_yaml(r'..\TestDatas\ParamData\Login.yaml')
    login_data = yaml_data[0]

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = Base(page)
        self.login.login(self.login_data)
        self.test_AddProjects = AddProjectsPage(page)

    # @pytest.mark.run(order=1)
    @pytest.mark.sc
    @pytest.mark.skip(reason="Not Implemented")
    def test_add_design_review(self):
        """
        测试新建建设工程消防设计审查
        """
        try:
            self._navigate_to_add_design_review()
            self._add_design_review()
            self._save_design_review()
            if self._assert_design_review():
                logger.info('新建建设工程消防设计审查成功')
        except Exception as e:
            logger.error(f"新建建设工程消防设计审查失败: {e}")
            raise

    def _navigate_to_add_design_review(self):
        self.test_AddProjects.goto_add_projects()
        self.test_AddProjects.click_xf()

    def _add_design_review(self):
        self.test_AddProjects.click_new_construction_design_review()
        time.sleep(1)
        self.test_AddProjects.select_project_name()
        self.test_AddProjects.select_engineering_name()
        self.test_AddProjects.select_category()
        self.test_AddProjects.select_using_properties()
        self.test_AddProjects.click_related_matters()

    def _save_design_review(self):
        self.test_AddProjects.click_add_construction_design_review_button()
        self.test_AddProjects.click_ok_button()

    def _assert_design_review(self):
        try:
            self.test_AddProjects.assert_design_review()
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False

    @pytest.mark.skip(reason="Not Implemented")
    def test_add_inspection(self):
        """
        测试新建建设工程消防验收
        """
        try:
            self._navigate_to_add_inspection()
            self._add_inspection()
            self._save_inspection()
            if self._assert_inspection():
                logger.info('新建建设工程消防验收成功')
        except Exception as e:
            logger.error(f"新建建设工程消防验收失败: {e}")
            raise

    def _navigate_to_add_inspection(self):
        self.test_AddProjects.goto_add_projects()
        self.test_AddProjects.click_xf()

    def _add_inspection(self):
        self.test_AddProjects.click_new_inspection()
        time.sleep(1)
        self.test_AddProjects.select_project_name()
        self.test_AddProjects.select_engineering_name()
        self.test_AddProjects.select_category2()
        self.test_AddProjects.select_using_properties()

    def _save_inspection(self):
        self.test_AddProjects.click_added_button()
        self.test_AddProjects.click_ok_inspection_button()

    def _assert_inspection(self):
        try:
            self.test_AddProjects.assert_inspection()
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False

    @pytest.mark.skip(reason="Not Implemented")
    def test_add_record(self):
        """
        测试新建建设工程消防备案-非一般项目
        """
        try:
            self._navigate_to_add_record()
            self._add_record()
            self._save_record()
            if self._assert_record():
                logger.info('新建建设工程消防备案成功')
        except Exception as e:
            logger.error(f"新建建设工程消防备案失败: {e}")
            raise

    def _navigate_to_add_record(self):
        self.test_AddProjects.goto_add_projects()
        self.test_AddProjects.click_xf()

    def _add_record(self):
        self.test_AddProjects.click_new_record()
        time.sleep(1)
        self.test_AddProjects.select_project_name()
        self.test_AddProjects.select_engineering_name()
        self.test_AddProjects.select_category2()
        self.test_AddProjects.select_using_properties()
        self.test_AddProjects.click_no_general_project()

    def _save_record(self):
        self.test_AddProjects.click_added_button()
        self.test_AddProjects.click_ok_record_button()

    def _assert_record(self):
        try:
            self.test_AddProjects.assert_record()
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False

    @pytest.mark.skip(reason="Not Implemented")
    def test_add_record_method(self):
        """
        测试新建建设工程消防备案-一般项目
        """
        try:
            self._navigate_to_add_record_method()
            self._add_record_method()
            self._save_record_method()
            if self._assert_record():
                logger.info('新建建设工程消防备案成功')
        except Exception as e:
            logger.error(f"新建建设工程消防备案失败: {e}")
            raise

    def _navigate_to_add_record_method(self):
        self.test_AddProjects.goto_add_projects()
        self.test_AddProjects.click_xf()

    def _add_record_method(self):
        self.test_AddProjects.click_new_record()
        time.sleep(1)
        self.test_AddProjects.select_project_name()
        self.test_AddProjects.select_engineering_name()
        self.test_AddProjects.select_category2()
        self.test_AddProjects.select_using_properties()
        self.test_AddProjects.click_is_general_project()
        self.test_AddProjects.click_general_project_types()
        self.test_AddProjects.click_application_method()

    def _save_record_method(self):
        self.test_AddProjects.click_added_button()
        self.test_AddProjects.click_ok_record_button()


if __name__ == '__main__':
    pytest.main(['-v', '-s', __file__])
