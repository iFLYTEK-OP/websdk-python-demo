"""
Video Moderation Client Usage Example
视频合规
"""
import json
import logging
import time
import os
from xfyunsdknlp.video_moderation_client import VideoModerationClient

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
    client = VideoModerationClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
        api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
    )

    try:
        # 获取识别文件路径
        videoUrl = "https://api.limewire.com/sharing/download/43f3a6bd-3fbe-458e-9218-583f3244f63a"
        moderate_param = [{
            "video_type": "mp4",
            "file_url": videoUrl,
            "name": "tts.mp4"
        }]
        # 1. 发送请求
        resp = client.send(moderate_param)
        json_resp = json.loads(resp)

        if json_resp["code"] == '000000':
            logger.info(f"识别返回结果: {json_resp}")
            request_id = json_resp["data"]["request_id"]
            get_result(request_id, client)
        else:
            logger.error(f"识别失败: {json_resp}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


def get_result(request_id, client=None):
    if not client:
        # 初始化客户端
        client = VideoModerationClient(
            app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
            api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
            api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
        )
    # 2. 轮询获取训练结果
    while True:
        result_response = client.query(request_id)
        result_data = json.loads(result_response)
        status = result_data.get("data", {}).get("audit_status")

        if status == 0:
            logger.info("视频合规待审核...")
        elif status == 1:
            logger.info("视频合规审核中...")
        elif status == 2:
            logger.info("视频合规审核完成：")
            logger.info(result_data)
            break
        elif status == 4:
            logger.info("视频合规审核异常：")
            logger.info(result_data)
            break
        else:
            break
        time.sleep(3)


if __name__ == "__main__":
    main()
    # get_result("T2025061214240301ad390b60a235000")
