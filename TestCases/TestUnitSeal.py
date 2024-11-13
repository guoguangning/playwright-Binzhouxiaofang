"""
-*- coding: utf-8 -*-
@File    : TestUnitSeal.py
@Date    : 2024/11/12 13:34
@Author  : ggn
"""
import pytest
from BasePage.logger import Logger
from Pages.UnitSealPage import UnitSealPage
from TestCases.Base import Base
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("TestDeputy").get_log()


class TestUnitSealSJ(object):
    yaml_data = load_and_validate_yaml(r'C:\case\playwright_BinZhouXiaoFang\TestDatas\ParamData\Login.yaml')
    login_data_sj = yaml_data[2]

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = Base(page)
        self.login.login(self.login_data_sj)
        self.test_UnitSealPage = UnitSealPage(page)

    # @pytest.mark.run(order=3)
    def test_unit_seal_sj_inspection(self):
        """
        测试设计单位签章-消防验收
        """
        try:
            self._navigate_to_unit_seal_sj_inspection()
            self._sj_inspection()
            logger.info('消防验收设计单位签章完成')
        except Exception as e:
            logger.error(f"消防验收设计单位签章失败: {e}")
            raise

    def _navigate_to_unit_seal_sj_inspection(self):
        self.test_UnitSealPage.goto_unit_seal()
        self.test_UnitSealPage.click_xf()

    def _sj_inspection(self):
        self.test_UnitSealPage.click_inspection_list()
        self.test_UnitSealPage.click_enter_project_page()
        self.test_UnitSealPage.click_construction_unit_declaration_inspection()
        self.test_UnitSealPage.input_basic_situation_sj()
        self.test_UnitSealPage.click_signature()

    # @pytest.mark.run(order=3)
    def test_unit_seal_sj_record(self):
        """
        测试设计单位签章-消防备案
        """
        try:
            self._navigate_to_unit_seal_sj_record()
            self._sj_record()
            logger.info('消防备案设计单位签章完成')
        except Exception as e:
            logger.error(f"消防备案设计单位签章失败: {e}")
            raise

    # @pytest.mark.run(order=3)
    def test_unit_seal_sj_record_method(self):
        """
        测试设计单位签章-消防备案-告知承诺制
        """
        try:
            self._navigate_to_unit_seal_sj_record()
            self._sj_record()
            logger.info('消防备案设计单位签章完成')
        except Exception as e:
            logger.error(f"消防备案设计单位签章失败: {e}")
            raise

    def _navigate_to_unit_seal_sj_record(self):
        self.test_UnitSealPage.goto_unit_seal()
        self.test_UnitSealPage.click_xf()

    def _sj_record(self):
        self.test_UnitSealPage.click_record_list()
        self.test_UnitSealPage.click_enter_project_page()
        self.test_UnitSealPage.click_construction_unit_declaration_record()
        self.test_UnitSealPage.input_basic_situation_sj()
        self.test_UnitSealPage.click_signature()


class TestUnitSealJL(object):
    yaml_data = load_and_validate_yaml(r'C:\case\playwright_BinZhouXiaoFang\TestDatas\ParamData\Login.yaml')
    login_data_jl = yaml_data[3]

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = Base(page)
        self.login.login(self.login_data_jl)
        self.test_UnitSealPage = UnitSealPage(page)

    # @pytest.mark.run(order=3)
    def test_unit_seal_jl_inspection(self):
        """
        测试监理单位签章-消防验收
        """
        try:
            self._navigate_to_unit_seal_jl_inspection()
            self._jl_inspection()
            logger.info('消防验收监理单位签章完成')
        except Exception as e:
            logger.error(f"消防验收监理单位签章失败: {e}")
            raise

    def _navigate_to_unit_seal_jl_inspection(self):
        self.test_UnitSealPage.goto_unit_seal()
        self.test_UnitSealPage.click_xf()

    def _jl_inspection(self):
        self.test_UnitSealPage.click_inspection_list()
        self.test_UnitSealPage.click_enter_project_page()
        self.test_UnitSealPage.click_construction_unit_declaration_inspection()
        self.test_UnitSealPage.input_basic_situation_jl()
        self.test_UnitSealPage.click_signature()

    # @pytest.mark.run(order=3)
    def test_unit_seal_jl_record(self):
        """
        测试监理单位签章-消防备案
        """
        try:
            self._navigate_to_unit_seal_jl_record()
            self._jl_record()
            logger.info('消防备案监理单位签章完成')
        except Exception as e:
            logger.error(f"消防备案监理单位签章失败: {e}")
            raise

    @pytest.mark.run(order=3)
    def test_unit_seal_jl_record_method(self):
        """
        测试监理单位签章-消防备案-告知承诺制
        """
        try:
            self._navigate_to_unit_seal_jl_record()
            self._jl_record()
            logger.info('消防备案监理单位签章完成')
        except Exception as e:
            logger.error(f"消防备案监理单位签章失败: {e}")
            raise

    def _navigate_to_unit_seal_jl_record(self):
        self.test_UnitSealPage.goto_unit_seal()
        self.test_UnitSealPage.click_xf()

    def _jl_record(self):
        self.test_UnitSealPage.click_record_list()
        self.test_UnitSealPage.click_enter_project_page()
        self.test_UnitSealPage.click_construction_unit_declaration_record()
        self.test_UnitSealPage.input_basic_situation_jl()
        self.test_UnitSealPage.click_signature()


class TestUnitSealSG(object):
    yaml_data = load_and_validate_yaml(r'C:\case\playwright_BinZhouXiaoFang\TestDatas\ParamData\Login.yaml')
    login_data_sg = yaml_data[4]

    @pytest.fixture(autouse=True)
    def set_up(self, page):
        """在每个测试用例前执行"""
        self.login = Base(page)
        self.login.login(self.login_data_sg)
        self.test_UnitSealPage = UnitSealPage(page)

    # @pytest.mark.run(order=3)
    def test_unit_seal_sg_inspection(self):
        """
        测试施工总承包单位签章-消防验收
        """
        try:
            self._navigate_to_unit_seal_sg_inspection()
            self._sg_inspection()
            logger.info('消防验收施工总承包单位签章完成')
        except Exception as e:
            logger.error(f"消防验收施工总承包单位签章失败: {e}")
            raise

    def _navigate_to_unit_seal_sg_inspection(self):
        self.test_UnitSealPage.goto_unit_seal()
        self.test_UnitSealPage.click_xf()

    def _sg_inspection(self):
        self.test_UnitSealPage.click_inspection_list()
        self.test_UnitSealPage.click_enter_project_page()
        self.test_UnitSealPage.click_construction_unit_declaration_inspection()
        self.test_UnitSealPage.input_basic_situation_sg()
        self.test_UnitSealPage.click_signature()

    # @pytest.mark.run(order=3)
    def test_unit_seal_sg_record(self):
        """
        测试施工总承包单位签章-消防备案
        """
        try:
            self._navigate_to_unit_seal_sg_record()
            self._sg_record()
            logger.info('消防备案施工总承包单位签章完成')
        except Exception as e:
            logger.error(f"消防备案施工总承包单位签章失败: {e}")
            raise

    @pytest.mark.run(order=3)
    def test_unit_seal_sg_record_method(self):
        """
        测试施工总承包单位签章-消防备案-告知承诺制
            """
        try:
            self._navigate_to_unit_seal_sg_record()
            self._sg_record()
            logger.info('消防备案施工总承包单位签章完成')
        except Exception as e:
            logger.error(f"消防备案施工总承包单位签章失败: {e}")
            raise

    def _navigate_to_unit_seal_sg_record(self):
        self.test_UnitSealPage.goto_unit_seal()
        self.test_UnitSealPage.click_xf()

    def _sg_record(self):
        self.test_UnitSealPage.click_record_list()
        self.test_UnitSealPage.click_enter_project_page()
        self.test_UnitSealPage.click_construction_unit_declaration_record()
        self.test_UnitSealPage.input_basic_situation_sg()
        self.test_UnitSealPage.click_signature()


if __name__ == '__main__':
    pytest.main(['-v', __file__])
