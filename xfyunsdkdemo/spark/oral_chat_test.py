"""
Oral Chat Client Usage Example
"""
import json
import os
import base64
import time

from xfyunsdkspark.oral_chat_client import OralChatClient, OralChatParam
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from dotenv import load_dotenv
except ImportError:
    raise RuntimeError(
        'Python environment is not completely set up: required package "python-dotenv" is missing.') from None

load_dotenv()


def process_response(message: str, player):
    """
    处理来自 WebSocket 的响应消息

    Args:
        message (str): 从 WebSocket 接收到的 UTF-8 编码的消息字符串
        player: 音频播放器对象，需实现 play(audio_data: bytes) 方法

    Returns:
        None
    """
    try:
        # 解析 JSON 响应
        response = json.loads(message)

        # 检查响应状态码
        code = response.get("header", {}).get("code", -1)
        if code != 0:
            logger.error(f"响应错误，错误码: {code}")
            return

        payload = response.get("payload")
        if not payload:
            # logger.error("响应中无 payload 数据")
            return

        # 根据 payload 类型处理不同业务逻辑
        if "event" in payload:
            event_data = payload["event"]
            encoded_text = event_data.get("text", "")
            if encoded_text:
                decoded_text = base64.b64decode(encoded_text).decode('utf-8')
                logger.info(f"事件文本消息: {decoded_text}")

        elif "iat" in payload:
            iat_data = payload["iat"]
            encoded_text = iat_data.get("text", "")
            if encoded_text:
                decoded_text = base64.b64decode(encoded_text).decode('utf-8')
                logger.info(f"语音识别结果: {decoded_text}")

        elif "nlp" in payload:
            nlp_data = payload["nlp"]
            encoded_text = nlp_data.get("text", "")
            if encoded_text:
                decoded_text = base64.b64decode(encoded_text).decode('utf-8')
                logger.info(f"自然语言处理结果: {decoded_text}")

        elif "tts" in payload:
            tts_data = payload["tts"]
            audio_base64 = tts_data.get("audio", "")
            if audio_base64:
                audio_data = base64.b64decode(audio_base64)
                # player.play(audio_data)
                logger.info(f"接收到大小为 {len(audio_data)} 的音频数据")

        elif "cbm_vms" in payload:
            vms_data = payload["cbm_vms"]
            encoded_text = vms_data.get("text", "")
            if encoded_text:
                decoded_text = base64.b64decode(encoded_text)
                logger.info(f"接收到vms数据: {decoded_text}")

        else:
            logger.error("未知的 payload 类型")
    except Exception as e:
        logger.error(f"处理 WebSocket 消息时发生异常: {e}")


def generate():
    """非流式生成音频示例"""
    try:
        # 初始化客户端
        client = OralChatClient(
            app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
            api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
            api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
        )

        # 超拟人服务启动
        param = OralChatParam(
            interact_mode="continuous_vad",
            uid="youtestuid"
        )
        _client = client.start(param)
        logger.info("超拟人单工交互模式开启...")

        file_path = os.path.join(os.path.dirname(__file__), 'resources', '天气16K.wav')
        f = open(file_path, 'rb')

        first_frame = True
        while True:
            data = f.read(1024)
            if not data:
                client.send_msg(data, 2, _client)
                break
            if first_frame:
                client.send_msg(data, 0, _client)
                first_frame = False
            client.send_msg(data, 1, _client)
            time.sleep(0.04)

        # 打印返回结果
        for msg in client.stream(_client):
            # logger.info(msg)
            process_response(msg, None)
    except Exception as e:
        logger.error(f"操作失败: {str(e)}")
        raise


if __name__ == "__main__":
    generate()
