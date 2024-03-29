import sys
import os
import unittest
import json

# 将项目根目录添加到sys.path中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cnlitellm.providers.zhipu import ZhipuAIProvider


class TestZhipuAIProvider(unittest.TestCase):
    def setUp(self):
        # 请将'your_api_key'替换为您的Zhipu AI API密钥
        self.provider = ZhipuAIProvider(
            api_key="e3833c6712b25eb4d89babd15c8134f5.Do904yhEYxDjewxI"
        )

    def test_completion(self):
        model = "GLM-4"
        messages = [{"content": "你好，今天天气怎么样？", "role": "user"}]
        response = self.provider.completion(model=model, messages=messages)
        print("response: ", response)
        self.assertIsNotNone(response)

    # def test_completion(self):
    #     model = "GLM-4"
    #     messages = [{"content": "你好，今天天气怎么样？", "role": "user"}]
    #     response = self.provider.completion(model=model, messages=messages, stream=True)
    #     for chunk in response:
    #         new_chunk = json.loads(chunk)
    #         delta = new_chunk["choices"][0]["delta"]
    #         line = {
    #             "choices": [
    #                 {
    #                     "delta": {
    #                         "role": delta["role"],
    #                         "content": delta["content"],
    #                     }
    #                 }
    #             ]
    #         }
    #         if "usage" in new_chunk:
    #             usage_info = new_chunk["usage"]
    #             line["usage"] = {
    #                 "prompt_tokens": usage_info["prompt_tokens"],
    #                 "completion_tokens": usage_info["completion_tokens"],
    #                 "total_tokens": usage_info["total_tokens"],
    #             }
    #         print("line:", line)
    #     self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
