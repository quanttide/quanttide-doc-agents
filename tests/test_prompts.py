import random
from http import HTTPStatus
from dashscope import Generation

from tests.prompts import USER_PROMPT, PARSED_RESULT


def test_toc_updating_prompt():
    """
    Test that the prompt works when the table of contents is updated.
    """
    messages = [{'role': 'system', 'content': '你是文档写作者'},
                {'role': 'user', 'content': USER_PROMPT}]
    response = Generation.call(model="qwen-max",
                               messages=messages,
                               # 设置随机数种子seed，如果没有设置，则随机数种子默认为1234
                               seed=random.randint(1, 10000),
                               # 将输出设置为"message"格式
                               result_format='message')
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
