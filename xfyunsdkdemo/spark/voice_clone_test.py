"""
Voice Clone Client Usage Example
一句话复刻
"""
import os
import logging
from xfyunsdkspark.voice_clone import VoiceCloneClient
from tool.audio_player import AudioPlayer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from dotenv import load_dotenv
except ImportError:
    raise RuntimeError(
        'Python environment is not completely set up: required package "python-dotenv" is missing.') from None

load_dotenv()


class PrintCallback:
    @staticmethod
    def on_audio_chunk(audio_chunk, **kwargs):
        """音频块回调处理"""
        if audio_chunk and audio_chunk.audio and audio_chunk.audio.audio:
            size = len(audio_chunk.audio.audio)
            logger.info(f"[回调] 收到一块音频，大小 {size} 字节, final={kwargs.get('final', False)}")


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


def generate():
    """非流式生成音频示例"""
    try:
        # 初始化客户端
        client = VoiceCloneClient(
            app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
            api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
            api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
            res_id="您的声纹ID",  # 替换为你的声纹ID
            encoding="raw",  # 默认为lame(mp4) , 此处设置raw(pcm)方便调用麦克风播放
            # callback=PrintCallback(),  # 使用回调处理音频块
            rhy=1  # 返回音素信息
        )

        player = AudioPlayer()
        player.start()

        # 生成音频
        text = "全民制作人大家好，我是练习时长两年半的个人练习生蔡徐坤。喜欢唱、跳、rap、篮球"
        logger.info(f"开始生成音频，文本长度: {len(text)}")

        result = client.generate(text)

        # 处理音频数据
        if result.pybuf and result.pybuf.text:
            logger.info(f"音频元素信息: {result.pybuf.text}")

        if result.audio and result.audio.audio:
            audio_data = result.audio.audio
            logger.info(f"音频总大小: {len(audio_data)} 字节")

            # 调用流式音频播放
            player.play(audio_data)
            player.stop()

            # 保存音频文件
            # save_audio_to_file(audio_data)
        else:
            logger.warning("未收到音频数据")

    except Exception as e:
        logger.error(f"生成音频失败: {str(e)}")
        raise


def stream():
    """流式生成音频示例"""

    # 启动音频播放器
    player = AudioPlayer()
    player.start()

    try:
        # 初始化客户端
        client = VoiceCloneClient(
            app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
            api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
            api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
            res_id="您的声纹ID",  # 替换为你的声纹ID
            encoding="raw",  # 默认为lame(mp4) , 此处设置raw(pcm)方便调用麦克风播放
            # callback=PrintCallback(),  # 使用回调处理音频块
            rhy=1  # 返回音素信息
        )

        # 准备存储所有音频数据
        audio_bytes = bytearray()
        pybuf_text = ''

        # 流式生成音频
        text = "一句话复刻可以通过声纹训练合成对应的音频信息"
        logger.info(f"开始流式生成音频，文本长度: {len(text)}")

        for chunk in client.stream(text):
            if chunk.audio and chunk.audio.audio:
                audio_chunk = chunk.audio.audio
                audio_bytes.extend(audio_chunk)
                logger.info(f"收到一块音频，大小 {len(audio_chunk)} 字节")

                # 音频流传入播放器
                player.play(audio_chunk)

            if chunk.pybuf and chunk.pybuf.text:
                pybuf_text += chunk.pybuf.text

        logger.info(f"音频总大小: {len(audio_bytes)} 字节")
        if pybuf_text:
            logger.info(f"音频元素信息: {pybuf_text}")

        # 保存音频文件
        if audio_bytes:
            # 保存音频文件
            save_audio_to_file(audio_bytes)
        else:
            logger.warning("未收到音频数据")

    except Exception as e:
        logger.error(f"流式生成音频失败: {str(e)}")
        raise
    finally:
        player.stop()


if __name__ == "__main__":
    # 可以选择运行非流式或流式生成
    generate()  # 非流式生成
    # stream()   # 流式生成
