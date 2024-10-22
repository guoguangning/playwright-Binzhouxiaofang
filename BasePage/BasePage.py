"""
-*- coding: utf-8 -*-
@File    : BasePage.py
@Date    : 2024/9/24 15:25
@Author  : ggn
"""
import re
from datetime import datetime
from typing import Optional, Union, List
from playwright.sync_api import expect, Page, Locator
from BasePage.logger import Logger
from Utils.Util_url import Utils

logger = Logger("BasePage").get_log()


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.utils = Utils()

    def _goto_url(self, path: str) -> None:
        """使用配置文件中的 URL 打开网页"""
        full_url = self.utils.get_full_url(path)
        try:
            self.page.goto(full_url)
            logger.info(f"Navigated to URL: {full_url}")
        except Exception as e:
            logger.error(f"Cannot navigate to page: {e}")
            raise

    def _click(self, locators: Union[str, List[str]], frame_locator: Optional[str] = None) -> None:
        """
        点击元素
        :param locators: 传入单个元素定位器或多个元素定位器的列表
        :param frame_locator: 传入frame框架的定位器，如果没有传入，则一般点击
        :return:
        """
        # 如果传入的是单个 locator，将其转换为列表
        if isinstance(locators, str):
            locators = [locators]

        for locator in locators:
            try:
                self._ele_to_be_visible_force(locator, frame_locator)
                target = self._get_target_locator(locator, frame_locator)
                target.click()
                return  # 如果点击成功，退出函数
            except Exception as e:
                logger.warning(f"尝试点击 {locator} 失败: {e}")

        # 如果所有 locator 都尝试过但没有一个成功，抛出异常
        logger.error("所有元素点击失败")
        raise Exception("所有元素点击失败")

    def _hover(self, locator: str, frame_locator: Optional[str] = None) -> None:
        """
        悬停在元素上
        :param locator: 传入元素定位器
        :param frame_locator: 传入frame框架的的定位器，如果没有传入，则一般悬停
        :return:
        """
        try:
            self._ele_to_be_visible_force(locator, frame_locator)
            target = self._get_target_locator(locator, frame_locator)
            target.hover()
        except Exception as e:
            logger.error(f"悬停失败: {e}")
            raise

    def _fill(self, locator: Union[str, List[str]], value: str, frame_locator: Optional[str] = None) -> None:
        """
        定位元素，输入内容
        :param locator: 传入单个元素定位器或多个元素定位器列表
        :param value: 传入输入的值
        :param frame_locator: 传入frame框架
        :return:
        """
        # 如果传入的是单个定位器，将其转换为列表
        if isinstance(locator, str):
            locators = [locator]
        else:
            locators = locator

        for loc in locators:
            try:
                target = self._get_target_locator(loc, frame_locator)
                target.click()
                target.fill(value)
                return  # 成功填充后退出函数
            except Exception as e:
                logger.warning(f"定位器 {loc} 失败: {e}")

        # 如果所有定位器都失败，则抛出异常
        logger.error("所有定位器均失败，输入失败")
        raise Exception("所有定位器均失败，输入失败")

    def _type(self, locator: str, value: str, frame_locator: Optional[str] = None) -> None:
        """
        模拟人工输入，一个键一个键的输入
        :param locator:传入元素定位器
        :param value:传入输入的值
        :param frame_locator: 传入frame框架
        :return:
        """
        try:
            target = self._get_target_locator(locator, frame_locator)
            target.type(text=value, delay=100)
        except Exception as e:
            logger.error(f"输入失败: {e}")
            raise

    def _fill_select(self, locator: str, *option_locators: str, input_value: Optional[str] = None,
                     frame_locator: Optional[str] = None) -> None:
        """
        填充输入框或选择下拉选项，支持输入及多选。

        :param locator: 输入框或下拉框定位元素
        :param option_locators: 需要选择的下拉选项元素
        :param input_value: 当 locator 为输入框时填写的内容
        :param frame_locator: 提供的 frame 框架
        """
        try:
            target_element = self._get_target_locator(locator, frame_locator)
            logger.info("定位输入框或下拉框成功")
            target_element.click()

            if input_value:
                self._fill_input(target_element, input_value)
                self._select_option(option_locators[0], frame_locator)
            else:
                self._select_multiple_options(option_locators, frame_locator)

        except ValueError as ve:
            logger.error(f"值错误: {ve}. 请检查传入的参数。")
            raise
        except Exception as e:
            logger.error(f"下拉框选择失败: {str(e)}")
            raise

    @staticmethod
    def _fill_input(target_element, input_value: str) -> None:
        """ 填充输入框的辅助方法 """
        logger.info("准备输入内容")
        target_element.fill('')
        target_element.fill(input_value)
        logger.info(f"输入内容 '{input_value}' 成功")

    def _select_option(self, option_locator: str, frame_locator: Optional[str]) -> None:
        """ 选择单个下拉选项的辅助方法 """
        self._ele_to_be_visible_force(option_locator, frame_locator)
        option_element = self._get_target_locator(option_locator, frame_locator)
        option_element.click()

    def _select_multiple_options(self, option_locators: tuple, frame_locator: Optional[str]) -> None:
        """ 选择多个下拉选项的辅助方法 """
        for option_locator in option_locators:
            option_element = self._get_target_locator(option_locator, frame_locator)
            option_element.click()

    def _select_date(self, date_placeholder: str, frame_locator: Optional[str] = None) -> None:
        """
        选择日期的封装函数
        :param date_placeholder: 日期选择框的占位符文本
        """
        try:
            target = self._get_target_locator(date_placeholder, frame_locator)
            target.click()

            # 获取当前日期
            current_date = datetime.now()
            date_to_select = str(current_date.day)
            logger.info("{date_to_select}")

            # 寻找并选择当前日期
            date_element = self._get_target_locator(frame_locator).get_by_text(date_to_select, exact=True)
            if date_element.count() > 0:  # 确保找到元素
                date_element.click()
            else:
                logger.warning(f"未找到日期 {date_to_select}，请确认日期选择框是否正确显示.")

        except Exception as e:
            logger.error(f"选择时间失败: {e}")
            raise

    def _select_options(self, category_text: str, *options: str, frame_locator: Optional[str] = None) -> None:
        """根据给定的类别和选项进行选择

        :param category_text: 下拉框类别文本，例如 "类别：新建装修建筑保温用途变更扩建其他"
        :param options: 需要选择的选项，例如 "新建", "建筑保温"
        :param frame_locator:提供的 frame 框架
        """
        try:
            # 创建选择器，考虑是否有 frame
            locator = self.page.frame_locator(frame_locator).locator("div") if frame_locator else self.page.locator(
                "div")

            # 找到包含类别文本的 div 元素
            category_locator = locator.filter(has_text=re.compile(f"^{re.escape(category_text)}$"))

            # 点击下拉框
            category_locator.get_by_placeholder("请选择").click()
            # 点击所有选项
            for option in options:
                category_locator.get_by_text(option).click()

            logger.info("选项选择成功")
        except Exception as e:
            logger.error(f"选项选择失败: {e}")
            raise  # 重新抛出异常以便外部捕获和处理

    def select_option(self, select_locator: str, options: Union[str, List[str]], frame_locator: Optional[str] = None):
        """选择下拉框选项
        :param select_locator: 下拉框定位器
        :param options:需要选择的选项
        :param frame_locator: 提供的 frame 框架
        """
        logger.info(f"开始选择下拉框选项: {select_locator}, 选项: {options}")

        # 动态等待元素加载
        self._ele_to_be_visible_force(select_locator, frame_locator)
        target_locator = self._get_target_locator(select_locator, frame_locator)

        try:
            if isinstance(options, list):
                # 多选下拉框
                selected_options = []
                for option in options:
                    if not isinstance(option, str):
                        raise ValueError(f"每个选项值必须是字符串，但收到: {option}")
                    selected_options.append(option)

                logger.info(f"选择多选下拉框选项: {options}")
                target_locator.select_option(*selected_options)
            else:
                # 单选下拉框
                if not isinstance(options, str):
                    raise ValueError("单选下拉框的选项值必须是字符串")

                logger.info(f"选择单选下拉框选项: {options}")
                target_locator.select_option(options)
        except ValueError as e:
            logger.error(f"选项值类型错误: {e}")
        except Exception as e:
            logger.error(f"选择选项 '{options}' 时发生未知错误: {e}")

    def _file(self, locator: str, files: Union[str, List[str]], frame_locator: Optional[str] = None) -> None:
        """
        上传文件的方法
        :param locator: 定位器
        :param files: 单个文件路径，或者列表存放多个文件路径
        :param frame_locator: iframe框架定位器，如果没有就不传
        :return:
        """
        file_paths = []
        try:
            if isinstance(files, str):
                file_paths = [files]
            elif isinstance(files, list):
                file_paths = files
            else:
                raise TypeError("files 参数必须是字符串或字符串列表")

            target = self._get_target_locator(locator, frame_locator)
            target.set_input_files(file_paths)
            logger.info(f"文件上传成功: {', '.join(file_paths)} 到定位器 {locator}")
        except Exception as e:
            logger.error(f"文件上传失败: {e} - 定位器: {locator}, 文件路径: {file_paths}")
            raise  # 重新抛出异常，以便调用者可以处理

    def _ele_to_be_expect(self, locator: str, text: Optional[str] = None, frame_locator: Optional[str] = None) -> bool:
        """断言元素"""
        try:
            # 等待元素可见
            self._ele_to_be_visible_force(locator, frame_locator)

            if text is not None:
                # 日志记录尝试断言的元素定位器
                logger.info(f"尝试定位断言的元素 '{locator}' 值.")
                # 使用 expect 断言元素值
                expect(self._get_target_locator(locator, frame_locator)).to_contain_text(text)
                logger.info(f"定位的元素 '{locator}' 值与断言值一致.")
                return True
            else:
                # 日志记录尝试断言的元素定位器
                logger.info(f"尝试定位断言的元素 '{locator}' 可见.")
                # 使用 expect 断言元素可见
                expect(self._get_target_locator(locator, frame_locator)).to_be_visible()
                logger.info(f"定位的元素 '{locator}' 可见.")
                return True
        except Exception as e:
            # 日志记录异常情况
            logger.error(f"使用定位器声明元素的可见性时发生错误 '{locator}': {e}")
            return False  # 断言失败

    def _ele_to_be_visible_force(self, locator: str, frame_locator: Optional[str] = None, timeout: int = 5) -> None:
        """强制等待某个元素可见"""
        target = self._get_target_locator(locator, frame_locator)
        for _ in range(timeout * 2):  # 每0.5秒检查一次
            self.page.wait_for_timeout(500)
            if target.is_visible():
                return
        raise Exception("元素未找到!")

    def _ele_is_checked(self, locator: str) -> bool:
        """判断元素是否被选选中"""
        return self.page.is_checked(locator)

    def _browser_operation(self, reload: bool = False, forward: bool = False, back: bool = False) -> None:
        """浏览器操作，reload 刷新，forward 前进，back 后退"""
        if reload:
            self.page.reload()
        if back:
            self.page.go_back()
        if forward:
            self.page.go_forward()

    def _screenshot(self, path: str, full_page: bool = True, locator: Optional[str] = None) -> dict:
        """
        截图功能，默认截取全屏。如果传入定位器，则截取元素。

        :param path: 截图保存的路径。
        :param full_page: 是否截取全屏，默认为 True。
        :param locator: 定位器，用于指定要截图的元素。
        :return: 返回一个字典，包含截图结果的状态和路径。
        """
        try:
            if locator:
                # 检查定位器是否有效
                if not self.page.locator(locator).is_visible():
                    raise ValueError(f"Locator '{locator}' is not visible.")
                self.page.locator(locator).screenshot(path=path)
            else:
                self.page.screenshot(path=path, full_page=full_page)

            logger.info(f"Screenshot saved to {path}")
            return {"status": "success", "path": path}
        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")
            return {"status": "failure", "message": str(e)}

    def _get_target_locator(self, locator: Optional[str] = None,
                            frame_locators: Optional[Union[str, List[str]]] = None):
        """获取目标定位器，支持一层或多层 iframe，locator 是非必填参数"""

        if frame_locators is None:
            # 如果没有提供 frame_locators，直接返回 page 的定位器
            return self.page.locator(locator) if locator else self.page

        if isinstance(frame_locators, str):
            # 处理一层 iframe
            if locator:
                return self.page.frame_locator(frame_locators).locator(locator)
            else:
                return self.page.frame_locator(frame_locators)

        # 处理多层 iframe
        current_frame_locator = frame_locators[0]
        current_frame = self.page.frame_locator(current_frame_locator)

        if len(frame_locators) > 1:
            # 递归调用处理多层 iframe
            if locator:
                return self._get_target_locator(locator, frame_locators[1:])
            else:
                return self._get_target_locator(frame_locators=frame_locators[1:])

        # 最后一层 iframe
        return current_frame.locator(locator) if locator else current_frame

    @staticmethod
    def get_current_time_format():
        """ 获取当前时间并转换为 'HHMM' 格式 """
        return datetime.now().strftime("%H%M")



