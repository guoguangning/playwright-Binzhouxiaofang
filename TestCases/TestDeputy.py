"""
-*- coding: utf-8 -*-
@File    : TestDeputy.py
@Date    : 2024/10/17 13:53
@Author  : ggn
"""
import pytest

from BasePage.logger import Logger
from Pages.DeputyPage import DeputyPage
from TestCases.TestLogin import TestLogin
from Utils.Util_yaml import load_yaml

logger = Logger("TestDeputy").get_log()


class TestDeputy(object):
    yaml_data = load_yaml(r'C:\case\playwright_BinZhouXiaoFang\TestDatas\ParamData\Login.yaml')
    if yaml_data is None:
        raise ValueError("无法加载 Login.yaml 文件或文件内容为空。")
    login_data = yaml_data[1]

    param_data = load_yaml(r'C:\case\playwright_BinZhouXiaoFang\TestDatas\ParamData\TestDeputy.yaml')
    if param_data is None:
        raise ValueError("无法加载 TestDeputy.yaml 文件或文件内容为空。")

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = TestLogin()
        self.login.test_login(page, self.login_data)
        self.test_Deputy = DeputyPage(page)

    # @pytest.mark.run(order=3)
    @pytest.mark.parametrize('project_data', param_data)
    def test_deputy(self, project_data):
        """
        测试帮办
        """
        try:
            self._navigate_to_deputy()
            self._deputy(project_data)
            self._submit_deputy()
            if self._assert_deputy(project_data):
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

    def _assert_deputy(self, project_data):
        try:
            self.test_Deputy._ele_to_be_expect(project_data['expected'], project_data['expected_text'],
                                               project_data['iframe'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False


if __name__ == '__main__':
    pytest.main(['-v', __file__])
