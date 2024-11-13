"""
-*- coding: utf-8 -*-
@File    : UnitSealPage.py
@Date    : 2024/11/12 10:54
@Author  : ggn
"""
from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("UnitSealPage").get_log()


class UnitSealPage(BasePage):
    """建设单位申报"""
    data = load_and_validate_yaml(r'C:\case\playwright_BinZhouXiaoFang\TestDatas\EleData\UnitSealPage.yaml')

    def goto_unit_seal(self):
        try:
            self._goto_url(self.data['path'])
            logger.info("Navigating to UnitSealPage")
        except Exception as e:
            logger.error(f"Failed to open UnitSealPage: {e}")
            raise

    def click_xf(self) -> None:
        try:
            self._click(self.data['xf'])
            logger.info("Clicking xf")
        except Exception as e:
            logger.error(f"Failed to click xf: {e}")
            raise

    def click_inspection_list(self) -> None:
        """建设工程消防验收列表"""
        try:
            self._click(self.data['inspection_list'])
            logger.info("Clicking inspection_list")
        except Exception as e:
            logger.error(f"Failed to click inspection_list: {e}")
            raise

    def click_record_list(self) -> None:
        """建设单位消防验收备案列表"""
        try:
            self._click(self.data['record_list'])
            logger.info("Clicking record_list")
        except Exception as e:
            logger.error(f"Failed to click record_list: {e}")
            raise

    def click_enter_project_page(self) -> None:
        """进入项目"""
        try:
            self._click(self.data['enter_project_page'], self.data['iframe'])
            logger.info("Clicking enter_project_page")
        except Exception as e:
            logger.error(f"Failed to click enter_project_page: {e}")
            raise

    def click_construction_unit_declaration_inspection(self) -> None:
        """建设单位消防验收申报"""
        try:
            self._click(self.data['construction_unit_declaration_inspection'],
                        self.data['iframe'])
            logger.info("Clicking construction_unit_declaration_inspection")
        except Exception as e:
            logger.error(f"Failed to click construction_unit_declaration_inspection: {e}")
            raise

    def click_construction_unit_declaration_record(self) -> None:
        """建设单位消防验收备案申报"""
        try:
            self._click(self.data['construction_unit_declaration_record'],
                        self.data['iframe'])
            logger.info("Clicking construction_unit_declaration_record")
        except Exception as e:
            logger.error(f"Failed to click construction_unit_declaration_record: {e}")
            raise

    def input_basic_situation_sj(self) -> None:
        """基本情况填写-设计单位"""
        try:
            self._click(self.data['sj'], self.data['iframe2'])
            self._click(self.data['view_template'], self.data['iframe2'])
            self._click(self.data['fill_in'], self.data['iframe2'])
            self._click(self.data['OK_button'], self.data['iframe2'])
            logger.info("input_basic_situation")
        except Exception as e:
            logger.error(f"Failed to input_basic_situation: {e}")
            raise

    def input_basic_situation_jl(self) -> None:
        """基本情况填写-监理单位"""
        try:
            self._click(self.data['jl'], self.data['iframe2'])
            self._click(self.data['view_template'], self.data['iframe2'])
            self._click(self.data['fill_in'], self.data['iframe2'])
            self._click(self.data['OK_button'], self.data['iframe2'])
            logger.info("input_basic_situation")
        except Exception as e:
            logger.error(f"Failed to input_basic_situation: {e}")
            raise

    def input_basic_situation_sg(self) -> None:
        """基本情况填写-施工总承包单位"""
        try:
            self._click(self.data['sg'], self.data['iframe2'])
            self._click(self.data['view_template'], self.data['iframe2'])
            self._click(self.data['fill_in'], self.data['iframe2'])
            self._click(self.data['OK_button'], self.data['iframe2'])
            logger.info("input_basic_situation")
        except Exception as e:
            logger.error(f"Failed to input_basic_situation: {e}")
            raise
        
    def click_signature(self) -> None:
        """签章"""
        try:
            self._click(self.data['signature_button'], self.data['iframe2'])
            self._click(self.data['signature_application_form_switch'], self.data['iframe2'])
            self._click(self.data['signature_acceptance_report_switch'], self.data['iframe2'])
            self._click(self.data['signature_confirm_button'], self.data['iframe2'])
            self._click(self.data['send_sms_button_acceptance'], self.data['iframe2'])
            time = self.get_current_time_format()
            self._fill(self.data['sms_verification_code_acceptance'], value=time,
                       frame_locator=self.data['iframe2'])
            self._click(self.data['signature_confirmation_button_acceptance'],
                        self.data['iframe2'])
            self._ele_to_be_expect(self.data['signature_confirmation_expected'],
                                   self.data['signature_confirmation_expected_text'],
                                   self.data['iframe2'])
            self._click(self.data['signature_ok_button'], self.data['iframe2'])
            logger.info("click_signature")
        except Exception as e:
            logger.error(f"Failed to click_signature: {e}")
            raise
