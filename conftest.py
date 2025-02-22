"""
-*- coding: utf-8 -*-
@File    : conftest.py
@Date    : 2024/10/15 10:58
@Author  : ggn
"""
import pytest
from playwright.sync_api import sync_playwright


# def pytest_configure(config):
#     """注册标签"""
#     print("pytest_configure is called!")  # 调试信息
#     markers_list = ["sc", "ys", "ba"]
#     for markers in markers_list:
#         config.addinivalue_line("markers", markers)
#         print(f"Marker {markers} added")  # 调试信息


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=['--start-maximized'])
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()
