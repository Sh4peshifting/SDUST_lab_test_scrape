import re

# 打开文本文件，读取内容
with open('original_id.txt', 'r') as file:
    content = file.read()

# 使用正则表达式查找所有rel=""的值
matches = re.findall(r'rel="([^"]+)"', content)

# 输出所有匹配结果
for match in matches:
    print(match)