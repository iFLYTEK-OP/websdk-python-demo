"""
Invoice OCR Client Usage Example
国内通用票证识别sinosecu & 票据卡证识别
"""
import json
import logging
import os
import base64
from xfyunsdkocr.invoice_ocr_client import InvoiceOCRClient, InvoiceTypeEnum

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from dotenv import load_dotenv
except ImportError:
    raise RuntimeError(
        'Python environment is not completely set up: required package "python-dotenv" is missing.') from None

load_dotenv()


def identify():
    # 初始化客户端
    client = InvoiceOCRClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
        api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
    )

    try:
        # 获取识别文件路径
        file_path = os.path.join(os.path.dirname(__file__), 'resources', 'backcard.jpg')
        with open(file_path, "rb") as file:
            encoded_string = base64.b64encode(file.read())
        # 发送请求
        resp = client.identify(encoded_string.decode("utf-8"), "jpg", InvoiceTypeEnum.BANK_CARD)
        json_resp = json.loads(resp)
        logger.info(f"识别返回结果: {json_resp}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


def identify_sino():
    # 初始化客户端
    client = InvoiceOCRClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
        api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
    )

    try:
        # 获取识别文件路径
        file_path = os.path.join(os.path.dirname(__file__), 'resources', 'backcard.jpg')
        with open(file_path, "rb") as file:
            encoded_string = base64.b64encode(file.read())
        # 发送请求
        resp = client.identify_sino(encoded_string.decode("utf-8"), "jpg")
        json_resp = json.loads(resp)

        if json_resp["header"]["code"] == 0:
            # logger.info(f"识别返回结果: {json_resp}")
            text = json_resp["payload"]["output_text_result"]["text"]
            final = base64.b64decode(text).decode("utf-8")
            logger.info(f"解码后结果: {final}")
        else:
            logger.error(f"识别失败: {json_resp}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    # identify_sino()
    identify()
