import tempfile
import time
import base64
import os
from io import BytesIO
from PIL import Image

from pdf2image import convert_from_path
from dotenv import load_dotenv
from openai import AzureOpenAI

from modules.document_structuring.prompt import SYSTEM_PROMPT, USER_PROMPT


load_dotenv(override=True)

class DocumentStructuring:
    """
    ドキュメントをテキストに構造化するクラス
    """

    @staticmethod
    def invoke(
        files: list,
        name: str,
    ):

        """
        ファイルをテキストに構造化する

        Args:
            files (list): ファイルのリスト
            name (str): テキストに構造化されるファイルの名前

        Returns:
            None
        """

        try :
            api_key = os.getenv("AZURE_OPENAI_KEY")
            model = os.getenv("AZURE_OPENAI_GPT-4O-MINI_DEPLOYMENT")
            api_version = os.getenv("AZURE_OPENAI_GPT-4O-MINI_VERSION")
            base_url = os.getenv("AZURE_OPENAI_ENDPOINT")
            base_url = f"{base_url}/openai/deployments/{model}"
            
            # PDFをbase64に変換
            pdf_base64_list = DocumentStructuring.pdf_to_base64(files)
            
            # プロンプト作成
            prompt = DocumentStructuring.create_prompt(pdf_base64_list)

            client = AzureOpenAI(
                api_key=api_key,
                api_version=api_version,
                base_url=base_url,
            )

            completion = client.chat.completions.create(
                model=model,
                messages=prompt,
            )

            response = completion.choices[0].message.content
            print("response : ", response)

            return "Success"

        except Exception as e:
            print(e)
            return None
        
    @staticmethod
    def pdf_to_base64(files: list):
        """
        PDFをbase64に変換する

        Args:
            files (list): ファイルのリスト

        Returns:
            pdf_base64_list (list): PDFをbase64に変換したリスト
        """
        pdf_base64_list = []

        for file in files:
            print(f'Starting conversion of PDF: {file.filename}')
            start_time = time.time()
            
            # 一時ファイルとして保存
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                file.save(temp_pdf.name)  # FileStorageオブジェクトを保存
                temp_pdf_path = temp_pdf.name

            # convert_from_pathに一時ファイルのパスを渡す
            images = convert_from_path(temp_pdf_path)
            base64_images = []
            
            for page_number, image in enumerate(images, start=1):
                page_start_time = time.time()
                
                buffered = BytesIO()
                image.save(buffered, format="PNG")
                img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
                base64_images.append(img_str)

                page_end_time = time.time()
                print(f'Converted page {page_number} of {file.filename} to base64 in {page_end_time - page_start_time:.2f} seconds')

                # 確認
                save_dir = "./test/pdf"
                save_path = os.path.join(save_dir, f"{file.filename}_{page_number}.png")
                image_data = base64.b64decode(img_str)
                with open(save_path, 'wb') as f:
                    f.write(image_data)

            end_time = time.time()
            print(f'Completed conversion of PDF: {file.filename} in {end_time - start_time:.2f} seconds')

            pdf_base64_list.append(base64_images)
        
        return pdf_base64_list
    
    @staticmethod
    def excel_to_base64():
        """
        Excelをbase64に変換する
        """

        pass

        return "Success"
    
    @staticmethod
    def word_to_base64():
        """
        Wordをbase64に変換する
        """

        pass

        return "Success"
    
    @staticmethod
    def ppt_to_base64():
        """
        PowerPointをbase64に変換する
        """

        pass

        return "Success"
    
    @staticmethod
    def create_prompt(
        base64_list: list
    ):
        """
        プロンプトを作成する

        Args:
            base64_list (list): 画像をbase64に変換したリスト

        Returns:
            prompt (str): プロンプト
        """

        prompt = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
        ]

        content_prompt = [
            {
                "type": "text",
                "text": USER_PROMPT,
            },
        ]

        for base64_image in base64_list[0]:

            content_prompt.append(
                {
                    "type": "image_url",
                    "image_url": {
                            "url": f"data:image/png;base64,{base64_image}",
                    },
                },
            )

        prompt.append(
            {
                "role": "user",
                "content": content_prompt
            }
        )

        return prompt