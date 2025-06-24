"""
Tuputech Api Client Usage Example
人脸特征分析tuputech
"""
import json
import logging
import os
from xfyunsdkface.tup_api_client import TupApiClient, TupEnum

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
    client = TupApiClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
        tup_type=TupEnum.FACE_SCORE
    )

    try:
        # 参数准备
        file_path = os.path.join(os.path.dirname(__file__), 'resources', 'people.jpg')
        resp = client.send("people.jpg", file_path)
        logger.info(f"{client.tup_type.get_desc()}结果: {resp}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    main()
