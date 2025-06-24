"""
Word Lib Client Usage Example
词库操作
"""
import json
import logging
import os
from xfyunsdknlp.wordlib_client import WordLibClient

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
    client = WordLibClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
        api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
    )

    try:
        # 1. 获取训练文本
        create_lib_resp = client.create_lib("测试词库003", "pornDetection")
        create_lib_data = json.loads(create_lib_resp)
        logger.info(f"创建词库响应: {create_lib_data}")

        # 2. 根据lib_id添加黑名单词条
        add_word_resp = client.add_word("8f70d68e744e4c47a08797099636ca68", ["大保健", "马杀鸡"])
        add_word_data = json.loads(add_word_resp)
        logger.info(f"添加词条响应: {add_word_data}")

        # 3. 根据lib_id删除词条
        del_word_resp = client.del_word("8f70d68e744e4c47a08797099636ca68", ["马杀鸡"])
        del_word_data = json.loads(del_word_resp)
        logger.info(f"删除词条响应: {del_word_data}")

        # 4. 根据lib_id查询词条明细
        detail_resp = client.detail("8f70d68e744e4c47a08797099636ca68")
        detail_data = json.loads(detail_resp)
        logger.info(f"词条明细响应: {detail_data}")

        # 5. 根据appid查询账户下所有词库
        list_lib_resp = client.list_lib()
        list_lib_data = json.loads(list_lib_resp)
        logger.info(f"查询词库响应: {list_lib_data}")

        # 6. 根据lib_id删除词库
        delete_lib_resp = client.delete_lib("8f70d68e744e4c47a08797099636ca68")
        delete_lib_data = json.loads(delete_lib_resp)
        logger.info(f"删除词库响应: {delete_lib_data}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    main()
