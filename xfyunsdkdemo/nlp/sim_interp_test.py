"""
Sim Interp Client Usage Example
同声传译
"""
import os
import base64
import json
from xfyunsdknlp.sim_interp_client import SimInterpClient
from tool.audio_player import AudioPlayer
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
    """非流式生成音频示例"""

    # 启动扬声器
    player = AudioPlayer()
    player.start()

    try:
        # 初始化客户端
        client = SimInterpClient(
            app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
            api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
            api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
            # encoding="lame"
        )
        file_path = os.path.join(os.path.dirname(__file__), 'resources', 'original.pcm')
        f = open(file_path, 'rb')

        # 准备存储所有音频数据
        audio_bytes = bytearray()

        content_map = {}
        final_result = ''
        trans_src_result = ''
        trans_dst_result = ''
        for chunk in client.stream(f):
            # logger.info(f"返回结果: {chunk}")
            if "recognition_results" in chunk:
                text_chunk = base64.b64decode(chunk["recognition_results"]["text"]).decode("utf-8")
                if text_chunk:
                    status = chunk["recognition_results"]["status"]
                    json_parse_text = json.loads(text_chunk)
                    req_result = get_ws_content(json_parse_text)
                    if json_parse_text['pgs'] == 'apd':
                        content_map[len(content_map)] = req_result
                        # logger.info(f"中间识别结果 【{req_result}】 拼接后结果==> {get_last_result(content_map)}")
                        logger.info(f"拼接后结果==> {get_last_result(content_map)}")
                    elif json_parse_text['pgs'] == 'rpl':
                        rg = json_parse_text['rg']
                        start_index = rg[0]
                        end_index = rg[1]
                        for i in range(start_index, end_index + 1):
                            content_map.pop(i, None)
                        content_map[len(content_map)] = req_result
                        # logger.info(f"中间识别结果 【{req_result}】 替换后结果==> {get_last_result(content_map)}")
                        logger.info(f"替换后结果==> {get_last_result(content_map)}")
                    if status == 2:
                        logger.info("转写流程结束==========================>")

            if "streamtrans_results" in chunk:
                trans_chunk = base64.b64decode(chunk["streamtrans_results"]["text"]).decode("utf-8")
                if trans_chunk:
                    json_trans_chunk = json.loads(trans_chunk)
                    is_final = json_trans_chunk["is_final"]
                    src = json_trans_chunk["src"]
                    dst = json_trans_chunk["dst"]
                    if 1 == is_final:
                        trans_src_result += src
                        trans_dst_result += dst
                        logger.info(f"翻译最终结果 ==> 原文：{trans_src_result}， 译文：{trans_dst_result}")
                        logger.info("翻译流程结束==========================>")
                    elif 0 == is_final:
                        logger.info(f"翻译中间结果 ==> 原文：{src}， 译文：{dst}")
            if "tts_results" in chunk:
                audio_chunk = base64.b64decode(chunk["tts_results"]["audio"])
                audio_bytes.extend(audio_chunk)
                # 流式播放
                player.play(audio_chunk)


        # 保存音频文件
        if audio_bytes:
            logger.info(f"生成音频文件大小: {len(audio_bytes)}")
            # save_audio_to_file(audio_bytes, f"oral_{uuid.uuid4().hex[:8]}.mp3")
        else:
            logger.warning("未收到音频数据")
    except Exception as e:
        logger.error(f"生成音频失败: {str(e)}")
        raise
    finally:
        player.stop()


def get_last_result(content_map):
    result = ''.join(content_map.values())
    return result


def get_ws_content(json_parse_text):
    req_result = ''
    ws_list = json_parse_text.get('ws', [])
    for ws in ws_list:
        cw_list = ws.get('cw', [])
        for cw in cw_list:
            req_result += cw.get('w', '')
    return req_result


if __name__ == "__main__":
    # 可以选择运行非流式或流式生成
    stream()  # 流式生成
