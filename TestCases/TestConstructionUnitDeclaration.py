"""
-*- coding: utf-8 -*-
@File    : TestConstructionUnitDeclaration.py
@Date    : 2024/11/11 9:11
@Author  : ggn
"""
import pytest
from BasePage.logger import Logger
from Pages.ConstructionUnitDeclarationPage import ConstructionUnitDeclarationPage
from TestCases.Base import Base
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("TestDeputy").get_log()


class TestConstructionUnitDeclaration(object):
    yaml_data = load_and_validate_yaml(r'C:\case\playwright_BinZhouXiaoFang\TestDatas\ParamData\Login.yaml')
    login_data = yaml_data[0]

    param_data = load_and_validate_yaml(
        r'C:\case\playwright_BinZhouXiaoFang\TestDatas\ParamData\TestConstructionUnitDeclaration.yaml')

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = Base(page)
        self.login.login(self.login_data)
        self.test_construction_unit_declaration = ConstructionUnitDeclarationPage(page)

    # @pytest.mark.run(order=3)
    @pytest.mark.parametrize('project_data', param_data)
    def test_construction_unit_declaration_design_review(self, project_data):
        """
        测试建设工程消防设计审查申报
        """
        try:
            self._navigate_to_design_review()
            self._design_review(project_data)
            self._submit_design_review()
            if self._assert_design_review(project_data):
                logger.info('建设工程消防设计审查申报提交完成')
        except Exception as e:
            logger.error(f"建设工程消防设计审查申报提交失败: {e}")
            raise

    def _navigate_to_design_review(self):
        self.test_construction_unit_declaration.goto_construction_unit_declaration()
        self.test_construction_unit_declaration.click_xf()

    def _design_review(self, project_data):
        self.test_construction_unit_declaration.click_construction_design_review_list()
        self.test_construction_unit_declaration.click_enter_project_page()
        self.test_construction_unit_declaration.click_construction_unit_declaration()
        self.test_construction_unit_declaration.input_review_declaration_design_review(project_data['num'])
        self.test_construction_unit_declaration.input_monomer_information(project_data['num'])
        self.test_construction_unit_declaration.input_other(project_data['num'])
        self.test_construction_unit_declaration.click_complete_design_review()
        self.test_construction_unit_declaration.upload_files_design_review()
        self.test_construction_unit_declaration.click_signature_design_review()

    def _submit_design_review(self):
        self.test_construction_unit_declaration.click_submit_design_review()

    def _assert_design_review(self, project_data):
        try:
            self.test_construction_unit_declaration._ele_to_be_expect(project_data['expected'],
                                                                      project_data['iframe'])
            return True
        except Exception as e:
            logger.error(f"断言不可见: {e}")
            return False

    # @pytest.mark.run(order=3)
    @pytest.mark.parametrize('project_data', param_data)
    def test_construction_unit_declaration_acceptance(self, project_data):
        """
        测试建设工程消防验收申报填写、签章
        """
        try:
            self._navigate_to_acceptance()
            self._acceptance(project_data)
            logger.info('建设工程消防验收申报填写并签章完成')
        except Exception as e:
            logger.error(f"建设工程消防验收申报填写并签章失败: {e}")
            raise

    #
    def _navigate_to_acceptance(self):
        self.test_construction_unit_declaration.goto_construction_unit_declaration()
        self.test_construction_unit_declaration.click_xf()

    def _acceptance(self, project_data):
        self.test_construction_unit_declaration.click_inspection_list()
        self.test_construction_unit_declaration.click_enter_project_page()
        self.test_construction_unit_declaration.click_construction_unit_declaration_inspection()
        self.test_construction_unit_declaration.input_review_declaration_acceptance(project_data['num'])
        self.test_construction_unit_declaration.input_monomer_information(project_data['num'])
        self.test_construction_unit_declaration.input_basic_situation(project_data['num'])
        self.test_construction_unit_declaration.click_complete_acceptance()
        self.test_construction_unit_declaration.upload_files_acceptance()
        self.test_construction_unit_declaration.input_acceptance_report(project_data['num'])
        self.test_construction_unit_declaration.click_send_signature_notification()
        self.test_construction_unit_declaration.click_signature_acceptance()

    # @pytest.mark.run(order=3)
    @pytest.mark.parametrize('project_data', param_data)
    def test_construction_unit_declaration_registration(self, project_data):
        """
        测试建设工程消防验收备案申报填写、签章（非一般项目）
        """
        try:
            self._navigate_to_registration()
            self._registration(project_data)
            logger.info('建设工程消防验收备案申报填写并签章完成')
        except Exception as e:
            logger.error(f"建设工程消防验收备案申报填写并签章失败: {e}")
            raise

    def _navigate_to_registration(self):
        self.test_construction_unit_declaration.goto_construction_unit_declaration()
        self.test_construction_unit_declaration.click_xf()

    def _registration(self, project_data):
        self.test_construction_unit_declaration.click_record_list()
        self.test_construction_unit_declaration.click_enter_project_page()
        self.test_construction_unit_declaration.click_construction_unit_declaration_record()
        self.test_construction_unit_declaration.input_review_declaration_registration(project_data['num'])
        self.test_construction_unit_declaration.input_monomer_information(project_data['num'])
        self.test_construction_unit_declaration.input_basic_situation(project_data['num'])
        self.test_construction_unit_declaration.click_complete_acceptance()
        self.test_construction_unit_declaration.upload_files_acceptance()
        self.test_construction_unit_declaration.input_acceptance_report(project_data['num'])
        self.test_construction_unit_declaration.click_send_signature_notification()
        self.test_construction_unit_declaration.click_signature_acceptance()

    # @pytest.mark.run(order=3)
    @pytest.mark.parametrize('project_data', param_data)
    def test_construction_unit_declaration_registration_method(self, project_data):
        """
        测试建设工程消防验收备案申报填写、签章（告知承诺制）
        """
        try:
            self._navigate_to_registration_method()
            self._registration_method(project_data)
            logger.info('建设工程消防验收备案申报填写并签章完成')
        except Exception as e:
            logger.error(f"建设工程消防验收备案申报填写并签章失败: {e}")
            raise

    def _navigate_to_registration_method(self):
        self.test_construction_unit_declaration.goto_construction_unit_declaration()
        self.test_construction_unit_declaration.click_xf()

    def _registration_method(self, project_data):
        self.test_construction_unit_declaration.click_record_list()
        self.test_construction_unit_declaration.click_enter_project_page()
        self.test_construction_unit_declaration.click_construction_unit_declaration_record()
        self.test_construction_unit_declaration.input_review_declaration_registration(project_data['num'])
        self.test_construction_unit_declaration.input_monomer_information(project_data['num'])
        self.test_construction_unit_declaration.input_basic_situation(project_data['num'])
        self.test_construction_unit_declaration.click_complete_registration()
        self.test_construction_unit_declaration.upload_files_registration()
        self.test_construction_unit_declaration.input_acceptance_report(project_data['num'])
        self.test_construction_unit_declaration.click_send_signature_notification_method()
        self.test_construction_unit_declaration.click_signature_acceptance()

    # @pytest.mark.run(order=3)
    def test_construction_unit_declaration_acceptance_submit(self):
        """
        测试建设工程消防验收申报提交
        """
        try:
            self._navigate_to_acceptance()
            self._submit()
            logger.info('建设工程消防验收申报提交完成')
        except Exception as e:
            logger.error(f"建设工程消防验收申报提交失败: {e}")
            raise

    def _submit(self) -> None:
        self.test_construction_unit_declaration.click_inspection_list()
        self.test_construction_unit_declaration.click_enter_project_page()
        self.test_construction_unit_declaration.click_construction_unit_declaration_inspection()
        self.test_construction_unit_declaration.click_submit_design_review()

    # @pytest.mark.run(order=3)
    def test_construction_unit_declaration_registration_submit(self):
        """
        测试建设工程消防验收备案申报提交-非一般项目
        """
        try:
            self._navigate_to_acceptance()
            self._submit_registration()
            logger.info('建设工程消防验收申报提交完成')
        except Exception as e:
            logger.error(f"建设工程消防验收申报提交失败: {e}")
            raise

    # @pytest.mark.run(order=3)
    def test_construction_unit_declaration_registration_method_submit(self):
        """
        测试建设工程消防验收备案申报提交-告知承诺制
        """
        try:
            self._navigate_to_acceptance()
            self._submit_registration()
            logger.info('建设工程消防验收申报提交完成')
        except Exception as e:
            logger.error(f"建设工程消防验收申报提交失败: {e}")
            raise

    def _submit_registration(self) -> None:
        self.test_construction_unit_declaration.click_record_list()
        self.test_construction_unit_declaration.click_enter_project_page()
        self.test_construction_unit_declaration.click_construction_unit_declaration_record()
        self.test_construction_unit_declaration.click_submit_design_review()


if __name__ == '__main__':
    pytest.main(['-v', __file__])
