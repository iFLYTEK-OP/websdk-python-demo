"""
Ise Client Usage Example
语音评测
"""
import os
import base64
from xfyunsdkspeech.ise_client import IseClient
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from dotenv import load_dotenv
except ImportError:
    raise RuntimeError(
        'Python environment is not completely set up: required package "python-dotenv" is missing.') from None

load_dotenv()


def stream():
    """非流式生成音频示例"""
    try:
        # 初始化客户端
        client = IseClient(
            app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
            api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
            api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
            aue="raw",
            group="pupil",
            ent="cn_vip",
            category="read_sentence",
        )
        file_path = os.path.join(os.path.dirname(__file__), 'resources/ise', 'read_sentence_cn.pcm')
        f = open(file_path, 'rb')

        for chunk in client.stream('\uFEFF' + "今天天气怎么样", f):
            if chunk["data"]:
                result = str(base64.b64decode(chunk["data"]), 'utf-8')
                logger.info(f"返回结果: {result}")
            else:
                logger.info(f"返回结果: {chunk}")
    except Exception as e:
        logger.error(f"生成音频失败: {str(e)}")
        raise


if __name__ == "__main__":
    # 可以选择运行非流式或流式生成
    stream()  # 流式生成
