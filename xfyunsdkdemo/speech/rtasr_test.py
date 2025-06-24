"""
Rtasr Client Usage Example
实时语音转写
"""
from xfyunsdkspeech.rtasr_client import RtasrClient
import logging
import os
import json
import pyaudio
import time
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
        client = RtasrClient(
            app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
            api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
        )

        file_path = os.path.join(os.path.dirname(__file__), 'resources/rtasr', 'rtasr.pcm')
        f = open(file_path, 'rb')

        # 流式打印结果
        final_result = []
        for chunk in client.stream(f):
            # logger.info(f"实时结果：{chunk}")
            if chunk:
                logger.info(f"实时转写结果：{''.join(final_result) + _handle_and_return_content(chunk, final_result)}")
    except Exception as e:
        logger.error(f"生成音频失败: {str(e)}")
        raise


def microphone_stream():
    """非流式生成音频示例"""
    try:
        # 初始化客户端
        client = RtasrClient(
            app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
            api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
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
            final_result = []
            for chunk in client.stream(mic_stream):
                # logger.info(f"实时结果：{chunk}")
                if chunk:
                    logger.info(
                        f"实时转写结果：{''.join(final_result) + _handle_and_return_content(chunk, final_result)}")

        thread = threading.Thread(target=run)
        thread.start()

        time.sleep(2)
        input("正在聆听，按回车结束转写...\r\n")
        p.terminate()
    except Exception as e:
        logger.error(f"生成音频失败: {str(e)}")
        raise


def _handle_and_return_content(message: str, final_result: list) -> str:
    temp_result = []

    try:
        # 解析 JSON 数据
        message_obj = json.loads(message)
        cn = message_obj.get("cn", {})
        st = cn.get("st", {})
        rt_arr = st.get("rt", [])

        for rt_obj in rt_arr:
            ws_arr = rt_obj.get("ws", [])
            for ws_obj in ws_arr:
                cw_arr = ws_obj.get("cw", [])
                for cw_obj in cw_arr:
                    w_str = cw_obj.get("w", "")
                    temp_result.append(w_str)

        # 根据 type 判断逻辑
        type_ = st.get("type")
        if type_ == "1":
            # 实时转写内容
            return ''.join(temp_result)
        elif type_ == "0":
            # 完整转写内容
            final_result.append(''.join(temp_result))
            return ''
        else:
            logger.warning("未知的转写响应类型：%s", type_)
            return ''.join(temp_result)

    except Exception as e:
        logger.error("解析异常：%s", e)
        return message


if __name__ == "__main__":
    # 可以选择运行非流式或流式生成
    stream()  # 流式生成
    # microphone_stream()  # 麦克风采集
