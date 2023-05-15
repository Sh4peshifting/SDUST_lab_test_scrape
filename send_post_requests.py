import requests
from docx import Document


# 读取id.txt中的数字
def read_ids(file_path):
    with open(file_path, 'r') as f:
        ids = [int(line.strip()) for line in f.readlines()]
    return ids


# 发送POST请求
def send_post_request(url, praxis_id, headers):
    data = {'praxisId': praxis_id}
    response = requests.post(url, data=data, headers=headers)
    return response.text


# 将返回的内容存储到Word文档中
def save_to_word(doc, content):
    doc.add_paragraph(content)
    doc.add_page_break()


def main():
    url = 'http://aqjy.sdust.edu.cn/ept/manage/practice/praxis'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',
        'Cookie': 'your_cookie'
    }
    file_path = 'id.txt'
    output_file = 'output.docx'

    praxis_ids = read_ids(file_path)
    doc = Document()

    for praxis_id in praxis_ids:
        content = send_post_request(url, praxis_id, headers)
        save_to_word(doc, content)

    doc.save(output_file)
    print(f"结果已保存到 {output_file}")


if __name__ == '__main__':
    main()
