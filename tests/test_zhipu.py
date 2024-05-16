import sys
import os
import json
import pytest
from dotenv import load_dotenv
load_dotenv()

# 将项目根目录添加到sys.path中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from unionllm.providers.zhipu import ZhipuAIProvider, ZhiPuOpenAIError

class TestZhipuAIProvider:
    @pytest.fixture(autouse=True)
    def setup_provider(self):
        # 从环境变量中导入API密钥
        self.provider = ZhipuAIProvider(api_key=os.getenv("ZHIPU_API_KEY"))

    def test_completion_stream(self):
        # Test non-stream completion
        model = "GLM-4"
        messages = [{"content": "introduce yourself briefly.", "role": "user"}]        
        try:
            response = self.provider.completion(model=model, messages=messages, stream=True)
            for chunk in response:
                print(chunk["choices"][0]["delta"]["content"])
        except Exception as e:
            pytest.fail(f"Error occurred: {e}")
        

    def test_completion_non_stream(self):
        # 定义模型和消息
        model = "GLM-4"
        messages = [{"content": "introduce yourself briefly.", "role": "user"}]
        try:
            response = self.provider.completion(model=model, messages=messages, stream=False)
            print(response)
        except Exception as e:
            pytest.fail(f"Error occurred: {e}")
