"""
-*- coding: utf-8 -*-
@File    : ConstructionUnitDeclarationPage.py
@Date    : 2024/10/22 14:53
@Author  : ggn
"""
from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("ConstructionUnitDeclarationPage").get_log()


class ConstructionUnitDeclarationPage(BasePage):
    """建设单位申报"""
    data = load_and_validate_yaml(
        r'..\TestDatas\EleData\ConstructionUnitDeclarationPage.yaml')
    design_review_data = data[0]  # 消防设计审查
    acceptance_data = data[1]  # 消防验收
    registration_data = data[2]  # 消防备案
    input_path = r'..\TestFiles\case.pdf'

    def goto_construction_unit_declaration(self):
        try:
            self._goto_url(self.design_review_data['path'])
            logger.info("Navigating to ConstructionUnitDeclarationPage")
        except Exception as e:
            logger.error(f"Failed to open ConstructionUnitDeclarationPage: {e}")
            raise

    def click_xf(self) -> None:
        try:
            self._click(self.design_review_data['xf'])
            logger.info("Clicking xf")
        except Exception as e:
            logger.error(f"Failed to click xf: {e}")
            raise

    def click_construction_design_review_list(self) -> None:
        """建设工程消防设计审查列表"""
        try:
            self._click(self.design_review_data['construction_design_review_list'])
            logger.info("Clicking construction_design_review_list")
        except Exception as e:
            logger.error(f"Failed to click construction_design_review_list: {e}")
            raise

    def click_inspection_list(self) -> None:
        """建设工程消防验收列表"""
        try:
            self._click(self.acceptance_data['inspection_list'])
            logger.info("Clicking inspection_list")
        except Exception as e:
            logger.error(f"Failed to click inspection_list: {e}")
            raise

    def click_record_list(self) -> None:
        """建设单位消防验收备案列表"""
        try:
            self._click(self.registration_data['record_list'])
            logger.info("Clicking record_list")
        except Exception as e:
            logger.error(f"Failed to click record_list: {e}")
            raise

    def click_enter_project_page(self) -> None:
        """进入项目"""
        try:
            self._click(self.design_review_data['enter_project_page'], self.design_review_data['iframe'])
            logger.info("Clicking enter_project_page")
        except Exception as e:
            logger.error(f"Failed to click enter_project_page: {e}")
            raise

    def click_construction_unit_declaration(self) -> None:
        """建设单位消防设计审查申报"""
        try:
            self._click(self.design_review_data['construction_unit_declaration'], self.design_review_data['iframe'])
            logger.info("Clicking construction_unit_declaration")
        except Exception as e:
            logger.error(f"Failed to click construction_unit_declaration: {e}")
            raise

    def click_construction_unit_declaration_inspection(self) -> None:
        """建设单位消防验收申报"""
        try:
            self._click(self.acceptance_data['construction_unit_declaration_inspection'],
                        self.acceptance_data['iframe'])
            logger.info("Clicking construction_unit_declaration_inspection")
        except Exception as e:
            logger.error(f"Failed to click construction_unit_declaration_inspection: {e}")
            raise

    def click_construction_unit_declaration_record(self) -> None:
        """建设单位消防验收备案申报"""
        try:
            self._click(self.registration_data['construction_unit_declaration_record'],
                        self.registration_data['iframe'])
            logger.info("Clicking construction_unit_declaration_record")
        except Exception as e:
            logger.error(f"Failed to click construction_unit_declaration_record: {e}")
            raise

    def input_review_declaration_design_review(self, value) -> None:
        """建设单位消防设计审查申报填写"""
        try:
            self._fill(self.design_review_data['contact'], value, self.design_review_data['iframe2'])
            self._fill(self.design_review_data['contact_number'], value, self.design_review_data['iframe2'])
            self._click(self.design_review_data['category'], self.design_review_data['iframe2'])
            self._fill(self.design_review_data['planning_permission_documents'], value,
                       self.design_review_data['iframe2'])
            self._fill(self.design_review_data['temporary_building_approval_document'], value,
                       self.design_review_data['iframe2'])
            self._click(self.design_review_data['special_fire_protection_design'], self.design_review_data['iframe2'])
            self._click(self.design_review_data['buildings_larger_than_250m'], self.design_review_data['iframe2'])
            self._fill(self.design_review_data['project_investment'], value, self.design_review_data['iframe2'])
            self._fill(self.design_review_data['total_construction_area'], value, self.design_review_data['iframe2'])
            self._click(self.design_review_data['special_construction_project_situations'],
                        self.design_review_data['iframe2'])
            self._click(self.design_review_data['technical_service_agency'], self.design_review_data['iframe2'])
            logger.info("input_review_declaration")
        except Exception as e:
            logger.error(f"Failed to input_review_declaration: {e}")
            raise

    def input_review_declaration_acceptance(self, value) -> None:
        """建设单位消防验收申报填写"""
        try:
            self._fill(self.acceptance_data['contact'], value, self.acceptance_data['iframe2'])
            self._fill(self.acceptance_data['contact_number'], value, self.acceptance_data['iframe2'])
            self._fill(self.acceptance_data['project_investment'], value, self.acceptance_data['iframe2'])
            self._fill(self.acceptance_data['total_construction_area'], value, self.acceptance_data['iframe2'])
            self._click(self.acceptance_data['fire_construction_unit'], self.acceptance_data['iframe2'])
            self._click(self.acceptance_data['technical_service_agency'], self.acceptance_data['iframe2'])
            self._fill(self.acceptance_data['fire_protection_design_review_opinion'], value,
                       self.acceptance_data['iframe2'])
            self._select_date(self.acceptance_data['click_review_pass_date'], self.acceptance_data['review_pass_date'], self.acceptance_data['iframe2'])
            self._fill(self.acceptance_data['construction_permit_number'], value, self.acceptance_data['iframe2'])
            self._select_date(self.acceptance_data['click_certification_date'], self.acceptance_data['certification_date'], self.acceptance_data['iframe2'])
            logger.info("input_review_declaration_acceptance")
        except Exception as e:
            logger.error(f"Failed to input_review_declaration_acceptance: {e}")
            raise

    def input_review_declaration_registration(self, value) -> None:
        """建设单位消防验收备案申报填写"""
        try:
            self._fill(self.registration_data['contact2'], value, self.registration_data['iframe2'])
            self._fill(self.registration_data['contact_number2'], value, self.registration_data['iframe2'])
            self._fill(self.registration_data['project_investment2'], value, self.registration_data['iframe2'])
            self._fill(self.registration_data['total_construction_area'], value, self.registration_data['iframe2'])
            self._click(self.registration_data['fire_construction_unit'], self.registration_data['iframe2'])
            self._click(self.registration_data['technical_service_agency'], self.registration_data['iframe2'])
            self._fill(self.registration_data['construction_permit_number'], value, self.registration_data['iframe2'])
            self._select_date(self.registration_data['click_certification_date2'], self.registration_data['certification_date2'], self.registration_data['iframe2'])
            logger.info("input_review_declaration_registration")
        except Exception as e:
            logger.error(f"Failed to input_review_declaration_registration: {e}")
            raise

    def input_monomer_information(self, value) -> None:
        """单体信息填写"""
        try:
            self._fill(self.design_review_data['structure_type'], value, self.design_review_data['iframe2'])
            self._fill(self.design_review_data['use_nature'], value, self.design_review_data['iframe2'])
            self.select_option(self.design_review_data['fire_resistance_grade_ground'],
                               self.design_review_data['fire_resistance_grade_ground_type'],
                               self.design_review_data['iframe2'])
            self.select_option(self.design_review_data['fire_resistance_level_underground'],
                               self.design_review_data['fire_resistance_level_underground_type'],
                               self.design_review_data['iframe2'])
            self._fill(self.design_review_data['floors_on_the_ground'], value, self.design_review_data['iframe2'])
            self._fill(self.design_review_data['floors_underground'], value, self.design_review_data['iframe2'])
            self._fill(self.design_review_data['high'], value, self.design_review_data['iframe2'])
            self._fill(self.design_review_data['length'], value, self.design_review_data['iframe2'])
            self._fill(self.design_review_data['floor_space'], value, self.design_review_data['iframe2'])
            self._fill(self.design_review_data['building_area_above_ground'], value, self.design_review_data['iframe2'])
            self._fill(self.design_review_data['building_area_underground'], value, self.design_review_data['iframe2'])
            logger.info("input_monomer_information")
        except Exception as e:
            logger.error(f"Failed to click input_monomer_information: {e}")
            raise

    def input_other(self, value) -> None:
        """其他信息填写-消防设计审查"""
        try:
            self._click(self.design_review_data['decoration'], self.design_review_data['iframe2'])
            self._click(self.design_review_data['decoration_parts'], self.design_review_data['iframe2'])
            self._fill(self.design_review_data['decoration_area'], value, self.design_review_data['iframe2'])
            self._fill(self.design_review_data['decoration_floor'], value, self.design_review_data['iframe2'])
            self._click(self.design_review_data['firefighting_facilities_and_others'],
                        self.design_review_data['iframe2'])
            self._fill(self.design_review_data['brief_description_of_the_project'], value,
                       self.design_review_data['iframe2'])
            logger.info("input_other")
        except Exception as e:
            logger.error(f"Failed to input_other: {e}")
            raise

    def input_basic_situation(self, value) -> None:
        """基本情况填写填写-消防验收、消防验收备案"""
        try:
            self._click(self.acceptance_data['basic_situation'], self.acceptance_data['iframe2'])
            self._click(self.acceptance_data['view_template'], self.acceptance_data['iframe2'])
            self._click(self.acceptance_data['fill_in'], self.acceptance_data['iframe2'])
            self._click(self.acceptance_data['OK_button'], self.acceptance_data['iframe2'])
            self._fill(self.acceptance_data['remark'], value, self.acceptance_data['iframe2'])
            logger.info("input_basic_situation")
        except Exception as e:
            logger.error(f"Failed to input_basic_situation: {e}")
            raise

    def click_complete_design_review(self) -> None:
        """填写完毕_消防设计审查"""
        try:
            self._click(self.design_review_data['complete_button'], self.design_review_data['iframe2'])
            self._ele_to_be_expect(self.design_review_data['complete_expected'],
                                   self.design_review_data['complete_expected_text'],
                                   self.design_review_data['iframe2'])
            self._click(self.design_review_data['complete_ok_button'], self.design_review_data['iframe2'])
            logger.info("click_complete")
        except Exception as e:
            logger.error(f"Failed to click_complete: {e}")
            raise

    def click_complete_acceptance(self) -> None:
        """填写完毕_消防验收、消防验收备案（非一般项目）"""
        try:
            self._click(self.acceptance_data['complete_button'], self.acceptance_data['iframe2'])
            self._ele_to_be_expect(self.acceptance_data['complete_expected'],
                                   self.acceptance_data['complete_expected_text'],
                                   self.acceptance_data['iframe2'])
            self._click(self.acceptance_data['complete_ok_button'], self.acceptance_data['iframe2'])
            logger.info("click_complete_acceptance")
        except Exception as e:
            logger.error(f"Failed to click_complete_acceptance: {e}")
            raise

    def click_complete_registration(self) -> None:
        """填写完毕_消防验收备案（告知承诺制）"""
        try:
            self._click(self.registration_data['complete_button'], self.registration_data['iframe2'])
            self._ele_to_be_expect(self.registration_data['complete_expected'],
                                   self.registration_data['complete_expected_text'],
                                   self.registration_data['iframe2'])
            self._click(self.registration_data['complete_ok_button'], self.registration_data['iframe2'])
            logger.info("click_complete_registration")
        except Exception as e:
            logger.error(f"Failed to click_complete_registration: {e}")
            raise

    def upload_files_design_review(self) -> None:
        """上传文件-消防设计审查"""
        try:
            self._click(self.design_review_data['upload_file_button'], self.design_review_data['iframe2'])
            self._click(self.design_review_data['click_file'], self.design_review_data['iframe3'])
            self._file(self.design_review_data['select_file'], self.input_path, self.design_review_data['iframe3'])
            logger.info("建设工程规划许可文件(依法需要办理的)，文件上传成功")
            self._click(self.design_review_data['upload_file_no'], self.design_review_data['iframe3'])
            self._click(self.design_review_data['upload_file_no2'], self.design_review_data['iframe3'])
            self._click(self.design_review_data['upload_file_no3'], self.design_review_data['iframe3'])
            self._click(self.design_review_data['upload_file_no4'], self.design_review_data['iframe3'])
            self._click(self.design_review_data['upload_file_no5'], self.design_review_data['iframe3'])
            self._click(self.design_review_data['upload_file_no6'], self.design_review_data['iframe3'])
            self._click(self.design_review_data['upload_complete_button'], self.design_review_data['iframe3'])
            self._ele_to_be_expect(self.design_review_data['upload_complete_expected'],
                                   self.design_review_data['upload_complete_expected_text'],
                                   self.design_review_data['iframe3'])
            self._click(self.design_review_data['upload_complete_ok_button'], self.design_review_data['iframe3'])
            logger.info("upload_files_design_review")
        except Exception as e:
            logger.error(f"Failed to upload_files_design_review: {e}")
            raise

    def upload_files_acceptance(self) -> None:
        """上传文件-消防验收"""
        try:
            self._click(self.acceptance_data['upload_file_button'], self.acceptance_data['iframe2'])
            self._click(self.acceptance_data['click_file'], self.acceptance_data['iframe3'])
            self._file(self.acceptance_data['select_file'], self.input_path, self.acceptance_data['iframe3'])
            logger.info("消防查验情况报告上传成功")
            self._click(self.acceptance_data['click_file2'], self.acceptance_data['iframe3'])
            self._file(self.acceptance_data['select_file2'], self.input_path, self.acceptance_data['iframe3'])
            logger.info("消防查验现场查验原始记录表上传成功")
            self._click(self.acceptance_data['click_file3'], self.acceptance_data['iframe3'])
            self._file(self.acceptance_data['select_file3'], self.input_path, self.acceptance_data['iframe3'])
            logger.info("涉及消防的建设工程竣工图纸上传成功")
            self._click(self.acceptance_data['upload_complete_button'], self.acceptance_data['iframe3'])
            self._ele_to_be_expect(self.acceptance_data['upload_complete_expected'],
                                   self.acceptance_data['upload_complete_expected_text'],
                                   self.acceptance_data['iframe3'])
            self._click(self.acceptance_data['upload_complete_ok_button'], self.acceptance_data['iframe3'])
            logger.info("upload_files_acceptance")
        except Exception as e:
            logger.error(f"Failed to upload_files_acceptance: {e}")
            raise

    def upload_files_registration(self) -> None:
        """上传文件-消防备案"""
        try:
            self._click(self.registration_data['upload_file_button2'], self.registration_data['iframe2'])
            self._click(self.registration_data['click_file'], self.registration_data['iframe3'])
            self._file(self.registration_data['select_file'], self.input_path, self.registration_data['iframe3'])
            logger.info("消防查验情况报告")
            self._click(self.registration_data['click_file2'], self.registration_data['iframe3'])
            self._file(self.registration_data['select_file2'], self.input_path, self.registration_data['iframe3'])
            logger.info("消防查验现场查验原始记录表")
            self._click(self.registration_data['upload_complete_button'], self.registration_data['iframe3'])
            self._ele_to_be_expect(self.registration_data['upload_complete_expected'],
                                   self.registration_data['upload_complete_expected_text'],
                                   self.registration_data['iframe3'])
            self._click(self.registration_data['upload_complete_ok_button'], self.registration_data['iframe3'])
            logger.info("upload_files_registration")
        except Exception as e:
            logger.error(f"Failed to upload_files_registration: {e}")
            raise

    def click_signature_design_review(self) -> None:
        """签章-消防设计审查"""
        try:
            self._click(self.design_review_data['signature_button'], self.design_review_data['iframe2'])
            self._click(self.design_review_data['send_sms_button'], self.design_review_data['iframe2'])
            time = self.get_current_time_format()
            self._fill(self.design_review_data['sms_verification_code'], value=time,
                       frame_locator=self.design_review_data['iframe2'])
            self._click(self.design_review_data['signature_confirmation_button'], self.design_review_data['iframe2'])
            self._ele_to_be_expect(self.design_review_data['signature_confirmation_expected'],
                                   self.design_review_data['signature_confirmation_expected_text'],
                                   self.design_review_data['iframe2'])
            self._click(self.design_review_data['signature_ok_button'], self.design_review_data['iframe2'])
            logger.info("click_signature_design_review")
        except Exception as e:
            logger.error(f"Failed to click_signature_design_review: {e}")
            raise

    def click_signature_acceptance(self) -> None:
        """签章-消防验收、备案"""
        try:
            self._click(self.acceptance_data['tab_first'], self.acceptance_data['iframe2'])
            self._click(self.acceptance_data['signature_button'], self.acceptance_data['iframe2'])
            self._click(self.acceptance_data['signature_application_form_switch'], self.acceptance_data['iframe2'])
            self._click(self.acceptance_data['signature_acceptance_report_switch'], self.acceptance_data['iframe2'])
            self._click(self.acceptance_data['signature_confirm_button'], self.acceptance_data['iframe2'])
            self._click(self.acceptance_data['send_sms_button_acceptance'], self.acceptance_data['iframe2'])
            time = self.get_current_time_format()
            self._fill(self.acceptance_data['sms_verification_code_acceptance'], value=time,
                       frame_locator=self.acceptance_data['iframe2'])
            self._click(self.acceptance_data['signature_confirmation_button_acceptance'],
                        self.acceptance_data['iframe2'])
            self._ele_to_be_expect(self.acceptance_data['signature_confirmation_expected'],
                                   self.acceptance_data['signature_confirmation_expected_text'],
                                   self.acceptance_data['iframe2'])
            self._click(self.acceptance_data['signature_ok_button'], self.acceptance_data['iframe2'])
            logger.info("click_signature_acceptance")
        except Exception as e:
            logger.error(f"Failed to click_signature_acceptance: {e}")
            raise

    def input_acceptance_report(self, value) -> None:
        """验收报告填写"""
        try:
            self._click(self.acceptance_data['acceptance_report'], self.acceptance_data['iframe2'])
            self._fill(self.acceptance_data['construction_permit_number_'], value,
                       self.acceptance_data['acceptance_iframe'])
            self._fill(self.acceptance_data['design_review_qualified_opinion'], value,
                       self.acceptance_data['acceptance_iframe'])
            self._fill(self.acceptance_data['inspection_certificate_number'], value,
                       self.acceptance_data['acceptance_iframe'])
            # 建设单位执行基本建设程序情况
            self._click(self.acceptance_data['basic_construction_procedures'],
                        self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['view_template_acceptance'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['fill_in_acceptance'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['OK_button_acceptance'], self.acceptance_data['acceptance_iframe'])
            # 对勘察单位评价
            self._click(self.acceptance_data['survey_unit_evaluation'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['view_template_acceptance'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['fill_in_acceptance'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['OK_button_acceptance'], self.acceptance_data['acceptance_iframe'])
            # 对设计单位评价
            self._click(self.acceptance_data['design_unit_evaluation'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['view_template_acceptance'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['fill_in_acceptance'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['OK_button_acceptance'], self.acceptance_data['acceptance_iframe'])
            # 对施工单位评价
            self._click(self.acceptance_data['construction_unit_evaluation'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['view_template_acceptance'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['fill_in_acceptance'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['OK_button_acceptance'], self.acceptance_data['acceptance_iframe'])
            # 对监理单位评价
            self._click(self.acceptance_data['supervision_unit_evaluation'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['view_template_acceptance'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['fill_in_acceptance'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['OK_button_acceptance'], self.acceptance_data['acceptance_iframe'])
            # 验收程序及组织形式
            self._click(self.acceptance_data['acceptance_procedure_organization'],
                        self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['view_template_acceptance'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['fill_in_acceptance'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['OK_button_acceptance'], self.acceptance_data['acceptance_iframe'])
            # 验收内容
            self._click(self.acceptance_data['acceptance_content'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['view_template_acceptance'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['fill_in_acceptance'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['OK_button_acceptance'], self.acceptance_data['acceptance_iframe'])
            # 竣工验收意见
            self._click(self.acceptance_data['completion_acceptance_opinion'],
                        self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['view_template_acceptance'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['fill_in_acceptance'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['OK_button_acceptance'], self.acceptance_data['acceptance_iframe'])
            # 查验情况
            self._fill(self.acceptance_data['HTWCQKState0'], value, self.acceptance_data['acceptance_iframe'])
            self._fill(self.acceptance_data['HTWCQKState1'], value, self.acceptance_data['acceptance_iframe'])
            self._fill(self.acceptance_data['HTWCQKState2'], value, self.acceptance_data['acceptance_iframe'])
            self._fill(self.acceptance_data['HTWCQKState3'], value, self.acceptance_data['acceptance_iframe'])
            self._fill(self.acceptance_data['DAZLWZXState0'], value, self.acceptance_data['acceptance_iframe'])
            self._fill(self.acceptance_data['DAZLWZXState1'], value, self.acceptance_data['acceptance_iframe'])
            self._fill(self.acceptance_data['DAZLWZXState2'], value, self.acceptance_data['acceptance_iframe'])
            self._fill(self.acceptance_data['DAZLWZXState3'], value, self.acceptance_data['acceptance_iframe'])
            self._fill(self.acceptance_data['FBFXHGestate0'], value, self.acceptance_data['acceptance_iframe'])
            self._fill(self.acceptance_data['FBFXHGestate1'], value, self.acceptance_data['acceptance_iframe'])
            self._fill(self.acceptance_data['FBFXHGestate2'], value, self.acceptance_data['acceptance_iframe'])
            self._fill(self.acceptance_data['FBFXHGestate3'], value, self.acceptance_data['acceptance_iframe'])
            self._fill(self.acceptance_data['SSXNState0'], value, self.acceptance_data['acceptance_iframe'])
            self._fill(self.acceptance_data['SSXNState1'], value, self.acceptance_data['acceptance_iframe'])
            self._fill(self.acceptance_data['SSXNState2'], value, self.acceptance_data['acceptance_iframe'])
            self._fill(self.acceptance_data['completion'], value, self.acceptance_data['acceptance_iframe'])
            # 填写完毕
            self._click(self.acceptance_data['complete_button_acceptance'], self.acceptance_data['acceptance_iframe'])
            self._ele_to_be_expect(self.acceptance_data['complete_expected_acceptance'],
                                   self.acceptance_data['complete_expected_acceptance_text'],
                                   self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['complete_ok_button_acceptance'], self.acceptance_data['acceptance_iframe'])
            logger.info("input_acceptance_report")
        except Exception as e:
            logger.error(f"Failed to input_acceptance_report: {e}")
            raise

    def click_send_signature_notification(self) -> None:
        """发送签章通知"""
        try:
            self._click(self.acceptance_data['acceptance_report'], self.acceptance_data['iframe2'])
            self._click(self.acceptance_data['send_signature_notification_button'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['application_form_switch'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['acceptance_report_switch'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['confirm_button'], self.acceptance_data['acceptance_iframe'])
            self._ele_to_be_expect(self.acceptance_data['expected_signature'], self.registration_data['expected_signature_text'], self.acceptance_data['acceptance_iframe'])
            self._click(self.acceptance_data['complete_ok_button_signature'], self.acceptance_data['acceptance_iframe'])
            logger.info("click_send_signature_notification")
        except Exception as e:
            logger.error(f"Failed to click_send_signature_notification: {e}")
            raise

    def click_send_signature_notification_method(self) -> None:
        """发送签章通知_告知承诺制"""
        try:
            self._click(self.registration_data['send_signature_notification_button_method'], self.registration_data['acceptance_iframe'])
            self._click(self.registration_data['application_form_switch_method'], self.registration_data['acceptance_iframe'])
            self._click(self.registration_data['acceptance_report_switch_method'], self.registration_data['acceptance_iframe'])
            self._click(self.registration_data['confirm_button_method'], self.registration_data['acceptance_iframe'])
            self._ele_to_be_expect(self.registration_data['expected_signature'], self.registration_data['expected_signature_text'], self.acceptance_data['acceptance_iframe'])
            self._click(self.registration_data['complete_ok_button_signature'], self.registration_data['acceptance_iframe'])
            logger.info("click_send_signature_notification_method")
        except Exception as e:
            logger.error(f"Failed to click_send_signature_notification_method: {e}")
            raise

    def click_submit_design_review(self) -> None:
        """提交操作"""
        try:
            self._click(self.design_review_data['submit_button'], self.design_review_data['iframe2'])
            self._ele_to_be_expect(self.design_review_data['submit_button_expected'],
                                   self.design_review_data['submit_button_expected_text'],
                                   self.design_review_data['iframe2'])
            self._click(self.design_review_data['submit_confirmation_button'], self.design_review_data['iframe2'])
            logger.info("click_submit_design_review")
        except Exception as e:
            logger.error(f"Failed to click_submit_design_review: {e}")
            raise
