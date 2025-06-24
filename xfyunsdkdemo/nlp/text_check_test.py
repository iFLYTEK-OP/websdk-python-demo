"""
Text Check Client Usage Example
文本纠错
"""
import json
import logging
import os
from xfyunsdknlp.text_check_client import TextCheckClient

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
    client = TextCheckClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
        api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
    )

    try:
        text = "衣据，鱿鱼圈，战士，画蛇天足，足不初户，狐假唬威，威风凛领，轮到"
        # 1. 发送请求
        resp = client.send(text)
        json_resp = json.loads(resp)
        logger.info(f"识别返回结果: {json_resp}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    main()
