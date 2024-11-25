import time
from PyDeepLX import PyDeepLX

# 添加延时
time.sleep(5)  # 等待5秒

try:
    result = PyDeepLX.translate("翻译好像不是你的强项。请问您擅长做什么？")
    print(result)
except PyDeepLX.TooManyRequestsException:
    print("请求太频繁，请稍后再试")
