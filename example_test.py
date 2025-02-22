import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://192.168.10.110:10710/login")
    page.get_by_placeholder("请输入账号，账号为您在数字底座中录入的手机号").click()
    page.get_by_placeholder("请输入账号，账号为您在数字底座中录入的手机号").fill("101011")
    page.get_by_placeholder("请输入密码", exact=True).click()
    page.get_by_placeholder("请输入密码", exact=True).fill("101010")
    page.get_by_placeholder("请输入账号，账号为您在数字底座中录入的手机号").click()
    page.get_by_placeholder("请输入账号，账号为您在数字底座中录入的手机号").fill("15154385201")
    page.get_by_placeholder("请输入密码", exact=True).click()
    page.get_by_placeholder("请输入密码", exact=True).fill("aa147258.")
    expect(page.locator("#loginForm_su")).to_contain_text("登录")
    page.get_by_text("登录", exact=True).click()
    page.goto("http://192.168.10.110:10710/selectSystem?type=2")
    page.locator("#xf").click()
    page.goto("http://192.168.10.110:10710/index#1/1??type=2")
    page.locator("a").filter(has_text="新建建设工程消防验收").click()
    page.locator("iframe[name=\"layui-layer-iframe1\"]").content_frame.get_by_role("button", name="关闭").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
