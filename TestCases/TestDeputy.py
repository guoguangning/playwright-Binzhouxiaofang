"""
-*- coding: utf-8 -*-
@File    : TestDeputy.py
@Date    : 2024/10/17 13:53
@Author  : ggn
"""
import pytest
from BasePage.logger import Logger
from Pages.DeputyPage import DeputyPage
from TestCases.Base import Base
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("TestDeputy").get_log()


class TestDeputy(object):
    yaml_data = load_and_validate_yaml(r'..\TestDatas\ParamData\Login.yaml')
    login_data = yaml_data[5]

    param_data = load_and_validate_yaml(r'..\TestDatas\ParamData\TestDeputy.yaml')

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = Base(page)
        self.login.login(self.login_data)
        self.test_Deputy = DeputyPage(page)

    # @pytest.mark.run(order=2)
    @pytest.mark.sc
    @pytest.mark.skip(reason="Not Implemented")
    @pytest.mark.parametrize('project_data', param_data)
    def test_deputy(self, project_data):
        """
        测试帮办
        """
        try:
            self._navigate_to_deputy()
            self._deputy(project_data)
            self._submit_deputy()
            if self._assert_deputy():
                logger.info('帮办完成')
        except Exception as e:
            logger.error(f"帮办失败: {e}")
            raise

    def _navigate_to_deputy(self):
        self.test_Deputy.goto_deputy_page()
        self.test_Deputy.click_xf()

    def _deputy(self, project_data):
        self.test_Deputy.click_construction_design_review_list()
        self.test_Deputy.click_enter_project_page()
        self.test_Deputy.click_deputy()
        self.test_Deputy.click_upload_file_configuration()
        self.test_Deputy.click_deputy_suggestion(project_data['value'])

    def _submit_deputy(self):
        self.test_Deputy.click_deputy_service_completed()

    def _assert_deputy(self):
        try:
            self.test_Deputy.ele_assert_deputy()
            return True
        except Exception as e:
            logger.error(f"断言成功: {e}")
            return False


if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])
