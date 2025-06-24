"""
Translate Client Usage Example
机械翻译
"""
import base64
import json
import logging
import os
from xfyunsdknlp.translate_client import TranslateClient

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from dotenv import load_dotenv
except ImportError:
    raise RuntimeError(
        'Python environment is not completely set up: required package "python-dotenv" is missing.') from None

load_dotenv()


def main():
    # 初始化客户端
    client = TranslateClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
        api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
    )

    try:
        text = "6月9日是科大讯飞司庆日。"
        # 1. 发送请求 ist
        resp = client.send_ist(text)
        json_resp = json.loads(resp)
        logger.info(f"ist翻译结果: {json_resp}")

        # 2. 发送请求 ist_v2
        # resp = client.send_ist_v2(text)
        # json_resp = json.loads(resp)
        # logger.info(f"ist_v2翻译结果: {json_resp}")
        # if json_resp["header"]['code'] == 0:
        #     text = json_resp['payload']['result']['text']
        #     result = base64.b64decode(text).decode("utf-8")
        #     logger.info(f"ist_v2解码后结果: {result}")
        # else:
        #     logger.error(f"ist_v2翻译失败: {json_resp}")

        # # 3. 发送请求 niu_trans
        # resp = client.send_niu_trans(text)
        # json_resp = json.loads(resp)
        # logger.info(f"小牛翻译结果: {json_resp}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    main()
