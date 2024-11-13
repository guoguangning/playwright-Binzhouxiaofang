"""
-*- coding: utf-8 -*-
@File    : DataReviewPage.py
@Date    : 2024/11/13 13:56
@Author  : ggn
"""
from BasePage.BasePage import BasePage
from BasePage.logger import Logger
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("DataReviewPage").get_log()


class DataReviewPage(BasePage):
    """主管部门资料审核"""
    data = load_and_validate_yaml(r'..\TestDatas\EleData\DataReviewPage.yaml')
    design_review_data = data[0]  # 消防设计审查
    acceptance_data = data[1]  # 消防验收
    registration_data = data[2]  # 消防备案

    def goto_data_review(self):
        try:
            self._goto_url(self.design_review_data['path'])
            logger.info("Navigating to DataReviewPage")
        except Exception as e:
            logger.error(f"Failed to open DataReviewPage: {e}")
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

    def click_acceptance_list(self) -> None:
        """建设工程消防验收列表"""
        try:
            self._click(self.acceptance_data['construction_acceptance_list'])
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

    def click_review_design_review(self) -> None:
        """主管部门审核-S3"""
        try:
            self._click(self.design_review_data['review_design_review'], self.design_review_data['iframe'])
            logger.info("Clicking review_design_review")
        except Exception as e:
            logger.error(f"Failed to click review_design_review: {e}")
            raise

    def click_acceptance_review(self) -> None:
        """主管部门审核-Y2"""
        try:
            self._click(self.acceptance_data['acceptance_review'],
                        self.acceptance_data['iframe'])
            logger.info("Clicking acceptance_review")
        except Exception as e:
            logger.error(f"Failed to click acceptance_review: {e}")
            raise

    def click_record_review(self) -> None:
        """主管部门审核-B2"""
        try:
            self._click(self.registration_data['record_review'],
                        self.registration_data['iframe'])
            logger.info("Clicking record_review")
        except Exception as e:
            logger.error(f"Failed to click record_review: {e}")
            raise

    def click_generate_credentials(self) -> None:
        """点击生成凭证按钮"""
        try:
            self._click(self.design_review_data['generate_credentials'],
                        self.design_review_data['iframe2'])
            logger.info("Clicking generate_credentials")
        except Exception as e:
            logger.error(f"Failed to click generate_credentials: {e}")
            raise

    def click_generate_certificate_signature(self) -> None:
        """生成凭证操作"""
        try:
            self._click(self.design_review_data['generate_certificate_signature'],
                        self.design_review_data['iframe3'])
            self._ele_to_be_expect(self.design_review_data['expect'], self.design_review_data['expect_text'],
                                   self.design_review_data['iframe3'])
            self._click(self.design_review_data['confirm_button'], self.design_review_data['iframe3'])
            self._ele_to_be_expect(self.design_review_data['expect_sig'], self.design_review_data['expect_sig_text'],
                                   self.design_review_data['iframe3'])
            self._click(self.design_review_data['OK_button'], self.design_review_data['iframe3'])
            self._click(self.design_review_data['close_window'], self.design_review_data['iframe3'])
            logger.info("Clicking generate_certificate_signature")
        except Exception as e:
            logger.error(f"Failed to click generate_certificate_signature: {e}")
            raise

    def click_through_button(self) -> None:
        """点击通过按钮"""
        try:
            self._click(self.design_review_data['through_button'],
                        self.design_review_data['iframe2'])
            logger.info("Clicking through_button")
        except Exception as e:
            logger.error(f"Failed to click through_button: {e}")
            raise
