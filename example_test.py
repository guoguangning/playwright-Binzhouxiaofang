import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://192.168.10.110:10700/login")
    page.get_by_placeholder("请输入账号，账号为您在数字底座中录入的手机号").click()
    page.get_by_placeholder("请输入账号，账号为您在数字底座中录入的手机号").fill("15154385201")
    page.get_by_placeholder("请输入密码", exact=True).click()
    page.get_by_placeholder("请输入密码", exact=True).fill("aa147258.")
    page.get_by_text("登录", exact=True).click()
    page.locator("#xf").click()
    page.locator("a").filter(has_text="新建建设工程消防设计审查").click()
    page.locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_text("选择", exact=True).first.click()
    page.locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_text("*-BC-20241015-").click()
    page.locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_role("button", name="确 定").click()
    page.locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_text("选择", exact=True).nth(1).click()
    page.locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_text("*-BC-20241015-051-").click()
    page.locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_role("button", name="确 定").click()
    page.locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_placeholder("请选择").nth(1).click()
    page.locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().locator("li").filter(has_text="房屋建筑工程").click()
    page.locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().locator("div").filter(has_text=re.compile(r"^项目地址 类别新建扩建改建$")).get_by_placeholder("请选择").click()
    page.locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().locator("li").filter(has_text="新建").click()
    page.locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_text("2022072210542403587").click()
    page.locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_role("cell", name="项目1").click()
    page.locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_role("cell", name="1", exact=True).locator("div").first.click()
    page.locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_role("row", name="1 项目1 滨城区 特殊建设工程消防设计审查").get_by_role("radio").click()
    page.locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_role("button", name="创建完毕并发送至帮办").click()
    page.locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_role("button", name="取消").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
