"""
Igr Client Usage Example
性别年龄识别
"""
import os
from xfyunsdkspeech.igr_client import IgrClient
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
        client = IgrClient(
            app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
            api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
            api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
            aue="raw",
            rate=16000,
        )
        file_path = os.path.join(os.path.dirname(__file__), 'resources/igr', 'igr_pcm_16k.pcm')
        f = open(file_path, 'rb')

        for chunk in client.stream(f):
            logger.info(f"返回结果: {chunk}")

    except Exception as e:
        logger.error(f"生成音频失败: {str(e)}")
        raise


if __name__ == "__main__":
    # 可以选择运行非流式或流式生成
    stream()  # 流式生成
