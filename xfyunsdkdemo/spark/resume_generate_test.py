"""
Resume Generate Client Usage Example
简历生成
"""
import json
import logging
import base64
import os
from xfyunsdkspark.resume_generate_client import ResumeGenClient

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
    client = ResumeGenClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
        api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
    )

    try:
        # 1. 获取训练文本
        logger.info("简历生成中...")
        desc = '''我是一名从业5年的java开发程序员, 今年25岁, 邮箱是xxx@qq.com , 电话13000000000, 性别男 , 就业地址合肥, 期望薪资20k , 主要从事AI大模型相关的项目经历'''
        resp = client.send(desc)
        json_resp = json.loads(resp)
        logger.info(f"简历生成返回结果: {json_resp}")

        code = json_resp['header']['code']
        if code == 0:
            text = json_resp['payload']['resData']['text']
            resume = base64.b64decode(text)
            logger.info(f"通过链接下载简历文件: {resume}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    main()
