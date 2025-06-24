"""
PD Rec Client Usage Example
图片还原文档
"""
import logging
import base64
import os
from xfyunsdkocr.pd_rec_client import PDRecClient

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from dotenv import load_dotenv
except ImportError:
    raise RuntimeError(
        'Python environment is not completely set up: required package "python-dotenv" is missing.') from None

load_dotenv()


def save_byte_to_file(document_data: bytes, filename: str = 'temp.docx') -> str:
    """保存数据到文件

    Args:
        document_data: 文件数据
        filename: 输出文件名

    Returns:
        str: 保存的文件绝对路径
    """
    try:
        with open(filename, 'wb') as f:
            f.write(document_data)
        file_path = os.path.abspath(filename)
        logger.info(f"文件已保存: {file_path}")
        return file_path
    except Exception as e:
        logger.error(f"保存文件失败: {str(e)}")
        raise


def main():
    # 初始化客户端
    client = PDRecClient(
        app_id=os.getenv('APP_ID'),  # 替换为你的应用ID
        api_key=os.getenv('API_KEY'),  # 替换为你的API密钥
        api_secret=os.getenv('API_SECRET'),  # 替换为你的API密钥
    )

    try:
        # 获取识别文件路径
        file_path = os.path.join(os.path.dirname(__file__), 'resources', 'pdrec.jpg')
        with open(file_path, "rb") as file:
            encoded_string = base64.b64encode(file.read())
        # 发送请求
        resp = client.generate(encoded_string.decode("utf-8"), "1", "jpg")
        # 保存文件
        save_byte_to_file(resp, "123.docx")
    except Exception as e:
        logger.error(f"发生错误: {str(e)}")
        raise


if __name__ == "__main__":
    main()
