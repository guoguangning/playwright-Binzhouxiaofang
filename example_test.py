import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://192.168.10.110:10706/login")
    page.get_by_placeholder("请输入账号，账号为您在数字底座中录入的手机号").click()
    page.get_by_placeholder("请输入账号，账号为您在数字底座中录入的手机号").fill("15154385201")
    page.get_by_placeholder("请输入密码", exact=True).click()
    page.get_by_placeholder("请输入密码", exact=True).fill("aa147258.")
    page.get_by_text("登录", exact=True).click()
    page.locator("#xf").click()
    page.locator("a").filter(has_text=re.compile(r"^建设工程消防验收$")).click()
    page.locator("iframe").nth(1).content_frame().get_by_role("link", name="进入项目页面").first.click()
    page.locator("iframe").nth(2).content_frame().get_by_text("Y1").click()
    page.locator("iframe").nth(2).content_frame().locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_placeholder("审查合格日期").click()
    page.locator("iframe").nth(2).content_frame().locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_text("11", exact=True).click()
    page.locator("iframe").nth(2).content_frame().locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().locator("#xfChayanJiben span").first.click()
    page.locator("iframe").nth(2).content_frame().locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_role("button", name="查看模板").click()
    page.locator("iframe").nth(2).content_frame().locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_role("button", name="填入").click()
    page.locator("iframe").nth(2).content_frame().locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_role("button", name="确 定").click()
    page.locator("iframe").nth(2).content_frame().locator("iframe[name=\"layui-layer-iframe1\"]").content_frame().get_by_placeholder("审查合格日期").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
