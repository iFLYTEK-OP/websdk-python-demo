"""
Face Compare Client Usage Example
人脸比对
"""
import json
import logging
import os
import base64
from xfyunsdkface.face_compare_client import FaceCompareClient

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
    client = FaceCompareClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
        api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
    )

    try:
        # 获取识别文件路径
        file_path1 = os.path.join(os.path.dirname(__file__), 'resources', 'compare1.jpg')
        file_path2 = os.path.join(os.path.dirname(__file__), 'resources', 'compare2.jpg')
        with open(file_path1, "rb") as file1:
            encoded_string1 = base64.b64encode(file1.read())
        with open(file_path2, "rb") as file2:
            encoded_string2 = base64.b64encode(file2.read())
        # 1. 发送请求
        resp = client.send(encoded_string1.decode("utf-8"), "jpg", encoded_string2.decode("utf-8"), "jpg")
        json_resp = json.loads(resp)
        logger.info(f"识别返回结果: {json_resp}")

        if json_resp["header"]['code'] == 0:
            text = json_resp['payload']['face_compare_result']['text']
            result = base64.b64decode(text).decode("utf-8")
            logger.info(f"解码后结果: {result}")
        else:
            logger.error(f"识别失败: {json_resp}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    main()
