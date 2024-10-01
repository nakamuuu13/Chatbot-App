import os
import json
import time

import requests
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class OpenAIChatResponse:
    @staticmethod
    def create_response_gpt_4o_mini(
            input_text: str,
            model_name="gpt-4o-mini-2024-07-18",
            max_tokens=100,
            temperature=1.2
        ):
            """
            入力文に対してGPT-4o-miniの回答文を作成する
            
            Args:
                input_text (str): 入力文
                model_name (str): モデル名
                max_tokens (int): 回答文の最大トークン数
                temperature (float): トークンのランダム性
            
            Returns:
                create_response_generator() (str): 回答文
            """
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {OPENAI_API_KEY}"
            }
            data = {
                "model": model_name,
                "messages": [{"role": "user", "content": input_text}],
                "max_tokens": max_tokens,
                "temperature": temperature,
                "stream": True
            }

            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data,
                stream=True
            )

            def response_stream_generator():
                """
                responseからyieldで回答文をchunk毎に返す
                
                Args:
                    None

                Yields:
                    res (str): chunk毎の回答文
                """
                for line in response.iter_lines():
                    if line:
                        line = line.decode("utf-8").replace("data: ", "", 1)
                        line_data = json.loads(line)
                        if "stop" != line_data["choices"][0]["finish_reason"]:
                            res = line_data['choices'][0]['delta']['content']
                            time.sleep(0.1)
                            yield res

                        else:
                            break

            return response_stream_generator()