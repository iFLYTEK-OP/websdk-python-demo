"""
Voice Train Client Usage Example
一句话训练
"""
import json
import logging
import time
import os
from xfyunsdkspark.voice_train import VoiceTrainClient, CreateTaskRequest, AudioAddRequest

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
    client = VoiceTrainClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
    )

    try:
        # 1. 获取训练文本
        logger.info("获取训练文本...")
        text_response = client.train_text(text_id=5001, async_mode=False)  # 使用默认训练文本
        text_data = json.loads(text_response)
        logger.info(f"训练文本: {text_data}")

        # 2. 创建训练任务
        logger.info("创建训练任务...")
        create_request = CreateTaskRequest(
            taskName="task-03",
            sex=2,  # 1: 男声, 2: 女声
            ageGroup=2,  # 1: 儿童, 2: 青年, 3: 中年, 4: 老年
            language="cn",  # 中文
            resourceName="中文女发音人",
        )
        task_response = client.create_task(create_request)
        task_data = json.loads(task_response)
        task_id = task_data.get("data")
        if not task_id:
            raise ValueError(f"Failed to create task: {task_response}")
        logger.info(f"任务创建成功, task_id: {task_id}")

        # 3. 添加音频到任务
        # logger.info("添加音频到任务...")
        # audio_request = AudioAddRequest(
        #     taskId=task_id,
        #     textId=5001,
        #     textSegId=1,
        #     audioUrl="https开头,wav|mp3|m4a|pcm文件结尾的URL地址"
        # )
        # audio_response = client.audio_add(audio_request)
        # audio_data = json.loads(audio_response)
        # logger.info(f"音频添加结果: {audio_data}")

        # 4. 提交训练任务
        # logger.info("提交训练任务...")
        # submit_response = client.submit(task_id)
        # submit_data = json.loads(submit_response)
        # logger.info(f"任务提交结果: {submit_data}")

        # 5. 提交文件任务(不需要单独调用submit接口)
        file_path = os.path.join(os.path.dirname(__file__), 'resources', 'train.mp3')
        local_audio_request = AudioAddRequest(
            taskId=task_id,
            textId=5001,
            textSegId=1,
            files=file_path
        )
        submit_with_audio_response = client.submit_with_audio(local_audio_request)
        logger.info(f"Submit with audio response: {submit_with_audio_response}")

        # 6. 轮询获取训练结果
        while True:
            result_response = client.result(task_id)
            result_data = json.loads(result_response)
            status = result_data.get("data", {}).get("trainStatus")

            if status == -1:
                logger.info("一句话复刻训练中...")
            elif status == 0:
                message = result_data.get("data", {}).get("failedDesc")
                logger.error(f"一句话复刻训练失败: {message}")
                break
            elif status == 2:
                logger.warning(f"一句话复刻训练任务未提交: {result_response}")
                break
            elif status == 1:
                resId = result_data.get("data", {}).get("assetId")
                logger.info(f"一句话复刻训练完成, 声纹ID: {resId}")
                break
            time.sleep(3)
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    main()
