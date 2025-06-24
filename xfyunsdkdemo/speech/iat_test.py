"""
Iat Client Usage Example
语音听写
"""
import os
from xfyunsdkspeech.iat_client import IatClient
import logging
import time
import pyaudio
import threading

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
        client = IatClient(
            app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
            api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
            api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
            dwa="wpgs"
        )
        # file_path = os.path.join(os.path.dirname(__file__), 'resources/iat', 'iat_pcm_16k.pcm')
        file_path = os.path.join(os.path.dirname(__file__), 'resources', '123.mp3')
        f = open(file_path, 'rb')

        for chunk in client.stream(f):
            logger.info(f"返回结果: {chunk}")

    except Exception as e:
        logger.error(f"生成音频失败: {str(e)}")
        raise


def microphone_stream():
    """非流式生成音频示例"""
    try:
        # 初始化客户端
        client = IatClient(
            app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
            api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
            api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
            dwa="wpgs"
        )

        time.sleep(1)
        input("按回车开始实时转写...")

        p = pyaudio.PyAudio()
        mic_stream = p.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=16000,
                            input=True,
                            frames_per_buffer=1280)

        def run():
            for chunk in client.stream(mic_stream):
                logger.info(f"返回结果: {chunk}")

        thread = threading.Thread(target=run)
        thread.start()

        time.sleep(2)
        input("正在聆听，按回车结束转写...\r\n")
        p.terminate()
    except Exception as e:
        logger.error(f"生成音频失败: {str(e)}")
        raise


if __name__ == "__main__":
    # 可以选择运行非流式或流式生成
    stream()  # 流式生成
    # microphone_stream()  # 麦克风采集
