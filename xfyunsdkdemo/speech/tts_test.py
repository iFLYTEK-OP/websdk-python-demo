"""
TTS Client Usage Example
语音合成
"""
import os
import base64
from xfyunsdkspeech.tts_client import TtsClient
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from dotenv import load_dotenv
except ImportError:
    raise RuntimeError(
        'Python environment is not completely set up: required package "python-dotenv" is missing.') from None

load_dotenv()


def save_audio_to_file(audio_data: bytes, filename: str = 'output.mp3') -> str:
    """保存音频数据到文件

    Args:
        audio_data: 音频数据
        filename: 输出文件名

    Returns:
        str: 保存的文件绝对路径
    """
    try:
        with open(filename, 'wb') as f:
            f.write(audio_data)
        file_path = os.path.abspath(filename)
        logger.info(f"音频文件已保存: {file_path}")
        return file_path
    except Exception as e:
        logger.error(f"保存音频文件失败: {str(e)}")
        raise


def stream():
    """流式生成音频示例"""
    try:
        # 初始化客户端
        client = TtsClient(
            app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
            api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
            api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
            vcn="xiaoyan",
        )

        # 准备存储所有音频数据
        audio_bytes = bytearray()

        # 流式生成音频
        text = "语音合成流式接口将文字信息转化为声音信息"
        logger.info(f"开始流式生成音频，文本长度: {len(text)}")

        for chunk in client.stream(text):
            if "audio" in chunk and chunk["audio"]:
                audio_chunk = base64.b64decode(chunk["audio"])
                audio_bytes.extend(audio_chunk)
                logger.info(f"收到一块音频，大小 {len(audio_chunk)} 字节")

        logger.info(f"音频总大小: {len(audio_bytes)} 字节")

        # 保存音频文件
        if audio_bytes:
            save_audio_to_file(audio_bytes)
        else:
            logger.warning("未收到音频数据")

    except Exception as e:
        logger.error(f"流式生成音频失败: {str(e)}")
        raise


if __name__ == "__main__":
    # 可以选择运行非流式或流式生成
    stream()
