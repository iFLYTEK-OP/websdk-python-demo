"""
Text Rewrite Client Usage Example
文本改写
"""
import json
import logging
import os
import base64
from xfyunsdknlp.text_rewrite_client import TextRewriteClient

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
    client = TextRewriteClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
        api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
    )

    try:
        text = "随着我国城市化脚步的不断加快，园林工程建设的数量也在不断上升，城市对于园林工程的质量要求也随之上升，然而就当前我国园林工程管理的实践而言，就园林工程质量管理这一环节还存在许多不足之处，本文在探讨园林工程质量内涵的基础上，深入进行质量管理策略探讨，目的是保障我国园林工程施工质量和提升整体发展效率。"
        # 1. 发送请求
        resp = client.send(text)
        json_resp = json.loads(resp)
        logger.info(f"识别返回结果: {json_resp}")

        if json_resp["header"]['code'] == 0:
            text = json_resp['payload']['result']['text']
            result = base64.b64decode(text).decode("utf-8")
            logger.info(f"解码后结果: {result}")
        else:
            logger.error(f"改写失败: {json_resp}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    main()
