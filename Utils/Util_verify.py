"""
-*- coding: utf-8 -*-
@File    : Util_verify.py
@Date    : 2024/10/15 9:52
@Author  : ggn
"""
import base64
from typing import Optional
import requests
from BasePage.logger import Logger

logger = Logger("Utils_yaml").get_log()


def verify(image_path: str) -> Optional[str]:
    """
    上传图片并进行验证码验证。

    :param image_path: 图片文件的绝对路径。
    :return: 验证码字符串（如果成功）或空字符串（如果失败）。
    """
    try:
        # 读取并编码图片文件
        with open(image_path, 'rb') as f:
            b = base64.b64encode(f.read()).decode()  # 图片二进制流base64字符串

        # 准备请求数据
        url = "http://api.jfbym.com/api/YmServer/customApi"
        data = {
            "token": "s3Bq6034gMQALrqrRvKrLuaEM3RN-jrVyua2V_F2sn0",
            "type": "50100",
            "image": b,
        }
        _headers = {
            "Content-Type": "application/json"
        }

        # 发送请求并处理响应
        response = requests.request("POST", url, headers=_headers, json=data).json()

        # 提取并返回验证码（如果存在）
        if 'data' in response and 'data' in response['data']:
            code = response['data']['data']
            logger.info(f"The code value is: {code}")
            return code
        else:
            logger.warning("No code found in the response.")
            return None  # 返回空字符串表示没有获取到验证码
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        return None
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        return None
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
        return None


if __name__ == '__main__':
    path = r''
    verify(path)
