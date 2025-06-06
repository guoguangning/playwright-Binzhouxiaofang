"""
-*- coding: utf-8 -*-
@File    : TestChangePassword.py
@Date    : 2024/10/15 14:02
@Author  : ggn
"""
import pytest
from BasePage.logger import Logger
from Pages.ChangePasswordPage import ChangePasswordPage
from Utils.Util_yaml import load_and_validate_yaml

logger = Logger("TestChangePassword").get_log()


class TestChangePassword(object):
    param_data = load_and_validate_yaml(r'..\TestDatas\ParamData\TestChangePassword.yaml')

    @pytest.mark.skip(reason="Not Implemented")
    @pytest.mark.parametrize('project_data', param_data)
    def test_change_password(self, page, project_data):
        """测试忘记密码修改密码功能"""
        try:
            self.ChangePassword = ChangePasswordPage(page)  # 创建 LoginPage 实例
            # 进行登录操作
            self.ChangePassword.goto_change_password()
            self.ChangePassword.click_forget_password()
            self.ChangePassword.fill_username(project_data['username'])
            self.ChangePassword.fill_graphic_verification_code()
            self.ChangePassword.fill_sms_verification_code(project_data['sms_verification_code'])
            self.ChangePassword.fill_new_password(project_data['new_password'])
            self.ChangePassword.fill_enter_again_new_password(project_data['new_password'])
            self.ChangePassword.click_submit_button()

            if self.ChangePassword.ele_assert_change_password():
                logger.info("修改密码成功")
        except Exception as e:
            logger.error(f"修改密码失败: {e}")
            raise


if __name__ == '__main__':
    pytest.main(['-v', __file__])
