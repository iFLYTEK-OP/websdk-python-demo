"""
Intsig OCR Client Usage Example
身份证识别 营业执照识别 增值税发票识别  通用文字识别
"""
import json
import logging
import os
import base64
from xfyunsdkocr.intsig_ocr_client import IntsigOCRClient, IntsigOCREnum

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
    client = IntsigOCRClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
        api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
        ocr_type=IntsigOCREnum.BUSINESS_LICENSE
    )

    try:
        # 获取识别文件路径
        file_path = os.path.join(os.path.dirname(__file__), 'resources', 'yyzz.jpg')
        with open(file_path, "rb") as file:
            encoded_string = str(base64.b64encode(file.read()), 'utf-8')
        # 发送请求
        resp = client.send(encoded_string, "jpg")
        json_resp = json.loads(resp)
        logger.info(f"识别返回结果: {json_resp}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    main()
