"""
General Words OCR Client Usage Example
印刷文字识别 & 手写文字识别
"""
import json
import logging
import base64
import os
from xfyunsdkocr.general_words_client import WordOCRClient

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from dotenv import load_dotenv
except ImportError:
    raise RuntimeError(
        'Python environment is not completely set up: required package "python-dotenv" is missing.') from None

load_dotenv()


def general():
    # 初始化客户端
    client = WordOCRClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
    )

    try:
        # 获取识别文件路径
        file_path = os.path.join(os.path.dirname(__file__), 'resources', 'ocr.jpg')
        with open(file_path, "rb") as file:
            encoded_string = base64.b64encode(file.read())
        # 发送请求
        resp = client.general(encoded_string.decode("utf-8"))
        json_resp = json.loads(resp)

        if json_resp["code"] == '0':
            logger.info(f"识别返回结果: {json_resp}")
            block = json_resp["data"]["block"]
            for line in block[0]["line"]:
                line_result = ""
                for content in line["word"]:
                    line_result += " " + content["content"]
                logger.info(f"{line_result}")
        else:
            logger.error(f"识别失败: {json_resp}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


def hand_writing():
    # 初始化客户端
    client = WordOCRClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
    )

    try:
        # 获取识别文件路径
        file_path = os.path.join(os.path.dirname(__file__), 'resources', 'ocr.jpg')
        with open(file_path, "rb") as file:
            encoded_string = base64.b64encode(file.read())
        # 发送请求
        resp = client.handwriting(encoded_string.decode("utf-8"))
        json_resp = json.loads(resp)

        if json_resp["code"] == '0':
            logger.info(f"识别返回结果: {json_resp}")
            block = json_resp["data"]["block"]
            for line in block[0]["line"]:
                line_result = ""
                for content in line["word"]:
                    line_result += " " + content["content"]
                logger.info(f"{line_result}")
        else:
            logger.error(f"识别失败: {json_resp}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    general()
    # hand_writing()
