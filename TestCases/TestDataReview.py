"""
-*- coding: utf-8 -*-
@File    : TestDataReview.py
@Date    : 2024/11/13 14:23
@Author  : ggn
"""
import pytest
from BasePage.logger import Logger
from Pages.DataReviewPage import DataReviewPage
from TestCases.Base import Base
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("TestDataReview").get_log()


class TestDataReviewSJ(object):
    yaml_data = load_and_validate_yaml(r'..\TestDatas\ParamData\Login.yaml')
    login_data = yaml_data[1]
    param_data = load_and_validate_yaml(r'..\TestDatas\ParamData\TestDataReview.yaml')

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = Base(page)
        self.login.login(self.login_data)
        self.test_DataReview = DataReviewPage(page)

    # @pytest.mark.run(order=3)
    @pytest.mark.parametrize('project_data', param_data)
    def test_data_review_design(self, project_data):
        """
        测试主管部门资料审核-消防设计审查
        """
        try:
            self._navigate_to_data_review()
            self._data_review_design()
            self._through_data_review_design()
            if self._assert_data_review_design(project_data):
                logger.info('主管部门审核成功-消防设计审查')
        except Exception as e:
            logger.error(f"主管部门审核失败-消防设计审查: {e}")
            raise

    def _navigate_to_data_review(self):
        self.test_DataReview.goto_data_review()
        self.test_DataReview.click_xf()

    def _data_review_design(self):
        self.test_DataReview.click_construction_design_review_list()
        self.test_DataReview.click_enter_project_page()
        self.test_DataReview.click_review_design_review()
        self.test_DataReview.click_generate_credentials()
        self.test_DataReview.click_generate_certificate_signature()

    def _through_data_review_design(self):
        self.test_DataReview.click_through_button()

    def _assert_data_review_design(self, project_data):
        try:
            self.test_DataReview._ele_to_be_expect(project_data['expect'], project_data['expect_text'],
                                                   project_data['iframe'])
            return True
        except Exception as e:
            logger.error(f"断言失败: {e}")
            return False

    # @pytest.mark.run(order=3)
    @pytest.mark.parametrize('project_data', param_data)
    def test_data_review_acceptance(self, project_data):
        """
        测试主管部门资料审核-消防验收
        """
        try:
            self._navigate_to_data_review()
            self._data_review_acceptance()
            self._through_data_review_design()
            if self._assert_data_review_acceptance(project_data):
                logger.info('主管部门审核成功-消防验收')
        except Exception as e:
            logger.error(f"主管部门审核失败-消防验收: {e}")
            raise

    def _data_review_acceptance(self):
        self.test_DataReview.click_acceptance_list()
        self.test_DataReview.click_enter_project_page()
        self.test_DataReview.click_acceptance_review()
        self.test_DataReview.click_generate_credentials()
        self.test_DataReview.click_generate_certificate_signature()

    def _assert_data_review_acceptance(self, project_data):
        try:
            self.test_DataReview._ele_to_be_expect(project_data['expect_acceptance'],
                                                   project_data['expect_acceptance_text'],
                                                   project_data['iframe'])
            return True
        except Exception as e:
            logger.error(f"断言失败: {e}")
            return False

    # @pytest.mark.run(order=3)
    @pytest.mark.parametrize('project_data', param_data)
    def test_data_review_record(self, project_data):
        """
        测试主管部门资料审核-消防验收备案
        """
        try:
            self._navigate_to_data_review()
            self._data_review_record()
            self._through_data_review_design()
            if self._assert_data_review_record(project_data):
                logger.info('主管部门审核成功-消防验收备案')
        except Exception as e:
            logger.error(f"主管部门审核失败-消防验收备案: {e}")
            raise

    def _data_review_record(self):
        self.test_DataReview.click_record_list()
        self.test_DataReview.click_enter_project_page()
        self.test_DataReview.click_record_review()
        self.test_DataReview.click_generate_credentials()
        self.test_DataReview.click_generate_certificate_signature()

    def _assert_data_review_record(self, project_data):
        try:
            self.test_DataReview._ele_to_be_expect(project_data['expect_record'], project_data['expect_record_text'],
                                                   project_data['iframe'])
            return True
        except Exception as e:
            logger.error(f"断言失败: {e}")
            return False


if __name__ == '__main__':
    pytest.main(['-v', __file__])
