"""
QBH Client Usage Example
歌曲识别
"""
import json
import logging
import os
from xfyunsdkspeech.qbh_client import QbhClient

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
    client = QbhClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        secret_key=os.getenv('API_SECRET'),  # 替换为你的API密钥
        timeout=120
    )

    try:
        # 1. 上传文件
        logger.info("歌曲识别...")
        # 参数准备
        file_path = os.path.join(os.path.dirname(__file__), 'resources/qbh', '一次就好16k.wav')

        resp = client.send(file_path=file_path)
        json_resp = json.loads(resp)
        if json_resp["code"] != "0":
            logger.error(f"识别失败: {json_resp}")
            return
        logger.info(f"歌曲识别结果: {json_resp}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    main()
