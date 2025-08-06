"""
LLM OCR Client Usage Example
"""
import json
import logging
import base64
import os
from xfyunsdkocr.llm_ocr_client import LlmOcrClient, LlmOcrParam

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
    client = LlmOcrClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
        api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
    )

    try:
        # 获取识别文件路径
        file_path = os.path.join(os.path.dirname(__file__), 'resources', 'car.jpg')
        with open(file_path, "rb") as file:
            encoded_string = base64.b64encode(file.read())
        # 发送请求
        param = LlmOcrParam(
            image_base64=encoded_string.decode("utf-8"),
            format="jpg"
        )
        resp = client.send(param)
        json_resp = json.loads(resp)

        code = json_resp.get("header", {}).get("code")
        if code == 0:
            logger.info(f"识别返回结果: {json_resp}")
            result = json_resp.get("payload", {}).get("result", {}).get("text", "")
            decode_str = base64.b64decode(result).decode("utf-8")
            logger.info(f"识解码后结果: {decode_str}")
        else:
            logger.error(f"识别失败: {resp}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    main()
