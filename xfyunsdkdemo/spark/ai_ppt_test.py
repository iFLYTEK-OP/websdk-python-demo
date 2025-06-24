import json
import os
import logging
from xfyunsdkspark.ai_ppt import AIPPTClient
from xfyunsdkcore.model.ai_ppt_model import PPTSearch, PPTCreate

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
    client = AIPPTClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
        timeout=120
    )

    try:
        # 1. 获取ppt主题列表
        list_resp = client.list(PPTSearch())
        list_data = json.loads(list_resp)
        logger.info(f"ppt主题列表: {list_data}")

        # 2. PPT生成（直接根据用户输入要求，获得最终PPT）
        file_path = os.path.join(os.path.dirname(__file__), 'resources', 'aipptv2.pdf')
        ppt_create = PPTCreate(
            query="根据提供的文件生成ppt",
            fileName="aipptv2.pdf",
            file=file_path
        )
        create_resp = client.create(ppt_create)
        create_data = json.loads(create_resp)
        logger.info(f"ppt生成返回结果: {create_data}")

        # 3. ppt大纲生成
        create_outline = PPTCreate(
            query="生成一个介绍科大讯飞的大纲"
        )
        outline_resp = client.create_outline(create_outline)
        outline_data = json.loads(outline_resp)
        logger.info(f"ppt大纲生成返回结果: {outline_data}")

        # 4. 自定义大纲生成
        doc_param = PPTCreate(
            query="生成一个随机的大纲",
            fileName="aipptv2.pdf",
            file=file_path
        )
        doc_resp = client.create_outline_by_doc(doc_param)
        doc_data = json.loads(doc_resp)
        logger.info(f"自定义大纲生成返回结果: {doc_data}")

        # 5. 通过大纲生成PPT
        ppt_param = PPTCreate(
            query="生成一个介绍科大讯飞的ppt",
            outline=doc_data["data"]["outline"],
        )
        ppt_resp = client.create_ppt_by_outline(ppt_param)
        ppt_data = json.loads(ppt_resp)
        logger.info(f"通过大纲生成PPT返回结果: {ppt_data}")

        # 6. 查询PPT进度
        progress_resp = client.progress(ppt_data["data"]["sid"])
        progress_data = json.loads(progress_resp)
        logger.info(f"查询PPT进度返回结果: {progress_data}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    main()
