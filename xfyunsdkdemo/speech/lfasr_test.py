"""
LFasr Client Usage Example
录音文件转写
"""
import json
import logging
import os
import time
from xfyunsdkspeech.lfasr_client import LFasrClient
from xfyunsdkcore.model.lfasr_model import UploadParam

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
    client = LFasrClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        secret_key=os.getenv('API_SECRET'),  # 替换为你的API密钥
    )

    try:
        # 1. 上传文件
        logger.info("上传文件...")
        # 参数准备
        file_path = os.path.join(os.path.dirname(__file__), 'resources/lfasr', 'lfasr_涉政.wav')
        param = UploadParam(
            audioMode="fileStream",
            fileName="lfasr_涉政.wav",
            fileSize=os.path.getsize(file_path),
        )
        upload_resp = client.upload(param.to_dict(), file_path)  # 使用默认训练文本
        upload_data = json.loads(upload_resp)
        if upload_data["code"] != "000000":
            logger.error(f"查询失败: {upload_data}")
            return
        logger.info(f"上传文件返回结果: {upload_data}")

        orderId = upload_data["content"]["orderId"]
        # 2. 查询结果
        logger.info("查询结果...")
        status = 3
        # 建议使用回调的方式查询结果，查询接口有请求频率限制
        while status == 3:
            param = {"orderId": orderId}
            result_resp = client.get_result(param)
            result_data = json.loads(result_resp)
            if result_data["code"] != "000000":
                logger.error(f"查询失败: {result_data}")
                break
            # logger.info(f"查询结果: {result_data}")
            status = result_data['content']['orderInfo']['status']
            if status == 0:
                logger.info(f"订单已经创建: {result_data}")
            elif status == 3:
                logger.info("订单处理中...")
            elif status == 4:
                logger.info(f"订单已完成: {result_data}")
                orderResult = result_data['content']['orderResult']
                order_data = json.loads(orderResult)
                logger.info(f"听写详情: {order_data}")
                break
            elif status == -1:
                failType = result_data['content']['orderInfo']['failType']
                logger.info(f"订单失败: {orderId}, 失败类型: {failType}")
                break
            time.sleep(5)
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    main()
