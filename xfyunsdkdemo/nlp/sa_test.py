"""
Sa Client Usage Example
情感分析
"""
import json
import logging
import os
from xfyunsdknlp.sa_client import SaClient

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
    client = SaClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
    )

    try:
        text = "我觉得挺感动。她是一个那么坚强的人，独自一个人撑起了整个家庭，非常佩服。"
        # 1. 发送请求
        resp = client.send(text)
        json_resp = json.loads(resp)
        logger.info(f"识别返回结果: {json_resp}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    main()
