import json
import os
import logging
from xfyunsdkspark.aiui_knowledge_client import AiUiKnowledgeClient
from xfyunsdkcore.model.aiui_knowledge_model import (
    AiUiCreate,
    AiUiUpload,
    AiUiDelete,
    AiUiSearch,
    AiUiLink,
    Repo,
    AiUiFileInfo
)

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
    client = AiUiKnowledgeClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_password=os.getenv('API_SECRET'),  # 替换为你的API密钥
        timeout=120
    )

    try:
        # 1. 创建个性化知识库
        # create_param = AiUiCreate(
        #     # 用户id
        #     uid=123123213,
        #     name="测试库py-001",
        #     # description="测试py库",
        #     # sid="123456",
        #     # channel="test"
        # )
        # create_resp = client.create(create_param)
        # create_data = json.loads(create_resp)
        # logger.info(f"个性化知识库创建结果: {create_data}")

        # 2. 上传文件
        # file_path1 = os.path.join(os.path.dirname(__file__), 'resources', 'aiuiknowledge.txt')
        # file_url1 = "https://oss-beijing-m8.openstorage.cn/knowledge-origin-test/knowledge/file/123123213/7741/a838a943/20250910163419/aiuiknowledge.txt"
        # upload_param = AiUiUpload(
        #     # 用户id
        #     uid=123123213,
        #     groupId="创建知识库生成的groupId",
        #     # files=[file_path1],
        #     fileList=[
        #         AiUiFileInfo(
        #             fileName="aiuiknowledge.txt",
        #             filePath=file_url1,
        #             fileSize=43
        #         )
        #     ]
        # )
        # upload_resp = client.upload(upload_param)
        # upload_data = json.loads(upload_resp)
        # logger.info(f"个性化知识库上传结果: {upload_data}")

        # 3. 删除知识库文件
        # delete_param = AiUiDelete(
        #     # 用户Id
        #     uid=123123213,
        #     groupId="创建知识库生成的groupId",
        #     docId="上传到知识库文件返回的docId"
        # )
        # delete_resp = client.delete(delete_param)
        # delete_data = json.loads(delete_resp)
        # logger.info(f"个性化知识库删除文件结果: {delete_data}")

        # 4. 查询知识库文件
        search_param = AiUiSearch(
            # 用户Id
            uid=123123213,
            appId=client.app_id,
            sceneName="sos_app"
        )
        search_resp = client.list(search_param)
        search_data = json.loads(search_resp)
        logger.info(f"个性化知识库查询结果: {search_data}")

        # 5. 用户应用关联绑定知识库
        # repo = Repo(
        #     groupId=group_id,
        # )
        # link_param = AiUiLink(
        #     uid=123123213,
        #     appId=client.app_id,
        #     sceneName="sos_app",
        #     repos=[repo]
        # )
        # link_resp = client.link(link_param)
        # link_data = json.loads(link_resp)
        # logger.info(f"用户应用关联绑定知识库结果: {link_data}")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    # asyncio.run(main())
    main()
