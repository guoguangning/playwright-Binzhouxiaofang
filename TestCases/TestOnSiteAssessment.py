"""
-*- coding: utf-8 -*-
@File    : TestOnSiteAssessment.py
@Date    : 2024/11/14 11:07
@Author  : ggn
"""
import pytest
from BasePage.logger import Logger
from Pages.OnSiteAssessmentPage import OnSiteAssessmentPage
from TestCases.Base import Base
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("TestOnSiteAssessment").get_log()


class TestOnSiteAssessment(object):
    yaml_data = load_and_validate_yaml(r'..\TestDatas\ParamData\Login.yaml')
    login_data = yaml_data[1]
    param_data = load_and_validate_yaml(r'..\TestDatas\ParamData\TestOnSiteAssessment.yaml')

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = Base(page)
        self.login.login(self.login_data)
        self.test_OnSiteAssessment = OnSiteAssessmentPage(page)

    # @pytest.mark.run(order=3)
    @pytest.mark.parametrize('project_data', param_data)
    def test_on_site_assessment(self, project_data):
        """
        测试现场评定 消防验收
        """
        try:
            self._navigate_to_on_site_assessment()
            self._on_site_assessment()
            if self._assert_on_site_assessment(project_data):
                logger.info('现场评定转预生成文书完成')
        except Exception as e:
            logger.error(f"现场评定转预生成文书失败: {e}")
            raise

    def _navigate_to_on_site_assessment(self):
        self.test_OnSiteAssessment.goto_on_site_assessment_page()
        self.test_OnSiteAssessment.click_xf()

    def _on_site_assessment(self):
        self.test_OnSiteAssessment.click_construction_acceptance_list()
        self.test_OnSiteAssessment.click_enter_project_page()
        self.test_OnSiteAssessment.click_on_site_assessment()
        self.test_OnSiteAssessment.click_spot_check()
        self.test_OnSiteAssessment.click_to_pre_generated_documents()

    def _assert_on_site_assessment(self, project_data):
        try:
            self.test_OnSiteAssessment._ele_to_be_expect(project_data['expected'], project_data['expected_text'],
                                                         project_data['iframe'])
            return True
        except Exception as e:
            logger.error(f"断言失败: {e}")
            return False


if __name__ == '__main__':
    pytest.main(['-v', __file__])
