"""
Example of ToC Updating
"""
import os
import random
from http import HTTPStatus
import dashscope
from dashscope import Generation

from dotenv import load_dotenv

SYSTEM_PROMPT = "按照输入的当前目录格式输出更新后的文档目录"

USER_PROMPT = """当前文档的目录是：
```
- 商业模式
- 产品与服务
- 研发与创新
- 市场与商业化
- 企业治理
- 企业文化
```
更新计划：
- 商业模式章增加"概述"、"云计算业务"、"高等教育业务"、"经济咨询业务"四节。
- 企业治理章增加"人才培养体系"、"联盟生态建设"两节。
"""

RAW_RESULT = """根据您的更新计划，更新后的文档目录如下：

```
- 商业模式
  - 概述
  - 云计算业务
  - 高等教育业务
  - 经济咨询业务
- 产品与服务
- 研发与创新
- 市场与商业化
- 企业治理
  - 人才培养体系
  - 联盟生态建设
- 企业文化
```
"""


load_dotenv('../.env')
dashscope_api_key = os.getenv("DASHSCOPE_API_KEY")
dashscope.api_key = dashscope_api_key


def toc_updating():
    """
    Test that the prompt works when the table of contents is updated.
    """
    messages = [{'role': 'system', 'content': SYSTEM_PROMPT},
                {'role': 'user', 'content': USER_PROMPT}]
    response = Generation.call(
        # turbo不可用，max可用
        model="qwen-max",
        messages=messages,
        # 设置随机数种子seed，如果没有设置，则随机数种子默认为1234
        seed=random.randint(1, 10000),
        # 将输出设置为"message"格式
        result_format='message'
    )
    if response.status_code == HTTPStatus.OK:
        content = response["output"]["choices"][0]["message"]["content"]
        print(content)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))


if __name__ == "__main__":
    toc_updating()
