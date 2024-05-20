# 智谱AI

## 设置API KEYS

```
import os 
os.environ["ZHIPU_API_KEY"] = "your-zhipu-api-key"
```

## 非流式调用

```python
from unionllm import unionchat

# model call
response = completion(
    provider="zhipuai",
    model="glm-4", 
    messages = [{ "content": "Hello, how are you?","role": "user"}]
)
```

## 流式调用

```python
from unionllm import unionchat

## set ENV variables
os.environ["COHERE_API_KEY"] = "cohere key"

# model call
response = completion(
    provider="zhipuai",
    model="glm-4", 
    messages = [{ "content": "Hello, how are you?","role": "user"}]
)

print(response)
```

## 直接传入API_Key调用

```python
# model call
response = completion(
    provider="zhipuai",
    model="glm-4", 
    api_key="your-zhipu-api-key",
    messages = [{ "content": "Hello, how are you?","role": "user"}]
)

for chunk in response:
    print(chunk)
```