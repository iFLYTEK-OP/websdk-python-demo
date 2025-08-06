"""
Spark Agent Client Usage Example
"""
import json
import os
from xfyunsdkspark.agent_client import AgentClient, AgentChatParam, AgentResumeParam
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from dotenv import load_dotenv
except ImportError:
    raise RuntimeError(
        'Python environment is not completely set up: required package "python-dotenv" is missing.') from None

load_dotenv()


def generate():
    """非流式生成音频示例"""
    try:
        # 初始化客户端
        client = AgentClient(
            app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
            api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
            api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
        )

        # 执行工作流
        param = AgentChatParam(
            flow_id="您的工作流 ID",
            parameters={
                "AGENT_USER_INPUT": "今天天气怎么样"
            },
            stream=False
        )
        if param.stream:
            finalResult = []
            thinkResult = []
            for line in client.completion(param):
                result_handler(line, finalResult, thinkResult, client)
        else:
            result = client.completion(param)
            logger.info(result)

        # 恢复工作流
        # resume_param = AgentResumeParam(
        #     event_id="工作流ID",
        #     event_type="事件类型",
        #     content="回复内容",
        # )
        # for line in client.resume(resume_param):
        #     logger.info(line)

        # 文件上传
        # file_path = os.path.join(os.path.dirname(__file__), 'resources', 'ocr.jpg')
        # upload_resp = client.upload(file_path)
        # logger.info(upload_resp)
    except Exception as e:
        logger.error(f"操作失败: {str(e)}")
        raise


def result_handler(line: str, finalResult, thinkResult, client: AgentClient):
    if line:
        jsp = json.loads(line)
        event_data = jsp.get("event_data")
        delta = jsp.get("choices", [])[0].get("delta", {})
        finish_reason = jsp.get("choices", [])[0].get("finish_reason", "")
        if event_data:
            event_id = event_data.get("event_id", "")
            value = event_data.get("value", {})
            content = value.get("content")
            type = value.get("type")
            if "option" == type:
                options = value.get("option", [])
                for option in options:
                    logger.info(f"{option.get('id')}: {option.get('text')}")

            # 遇到问答节点, 调用恢复工作流接口
            answer = input(content + "\r\n")
            resume_param = AgentResumeParam(
                event_id=event_id,
                event_type="resume",
                content=answer,
            )
            for data in client.resume(resume_param):
                result_handler(data, finalResult, thinkResult, client)
        if delta:
            # 回复
            content = delta.get("content")
            if content:
                finalResult.append(content)
                logger.info(f"返回结果 ==> {content}")
            # 思维链
            reasoning_content = delta.get("reasoning_content")
            if reasoning_content:
                thinkResult.append(reasoning_content)
                logger.info(f"思维链结果 ==> {reasoning_content}")
            plugins_content = delta.get("plugins_content")
            if plugins_content:
                logger.info(f"插件信息 ==> {plugins_content}")
        if finish_reason:
            if "stop" == finish_reason:
                logger.info("工作流结束")
                if thinkResult:
                    logger.info(f"思维链结果 ==> {''.join(thinkResult)}")
                if finalResult:
                    logger.info(f"最终识别结果 ==> {''.join(finalResult)}")


if __name__ == "__main__":
    generate()
