from setuptools import setup, find_packages

setup(
    name="xfyunsdkdemo",
    version="0.0.1",
    description="a sdk demo for xfyun",
    author="zyding6",
    author_email="zyding6@iflytek.com",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(include=["xfyunsdkdemo", "xfyunsdkdemo.*"]),
    install_requires=[
        "xfyunsdkspark>=0.0.3",
        "xfyunsdkspeech>=0.0.4",
        "xfyunsdkocr>=0.0.3",
        "xfyunsdkface>=0.0.3",
        "xfyunsdknlp>=0.0.3",
        "pipwin",
        "pyaudio",
        "python-dotenv"
    ]
)
