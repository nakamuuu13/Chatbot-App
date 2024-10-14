import os

from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient, ContainerClient
from azure.identity import DefaultAzureCredential

load_dotenv(override=True)
blob_connection_string = os.environ["BLOB_CONNECTION_STRING"]
class BlobStorageManager:

    @staticmethod
    def upload_documents(
            files: list,
            blob_container_name: str,
            use_user_identity: bool = False
    ):

        """
        ドキュメントをコンテナにアップロードする

        Args:
            files (list): アップロードするファイルのリスト
            blob_container_name (str): Blob Storage のコンテナ名
            use_user_identity (bool, optional): ユーザーの識別子を使用するかどうか。 Defaults to False.
        """
            
        blob_service_client: BlobServiceClient = BlobServiceClient.from_connection_string(logging_enable=True, conn_str=blob_connection_string, credential=DefaultAzureCredential() if use_user_identity else None)
        container_client: ContainerClient = blob_service_client.get_container_client(blob_container_name)
        if not container_client.exists():   # コンテナが存在しない場合は作成
            container_client.create_container()
            
        # for file in files:
        #     with open(file, "rb") as data:
        #         name = os.path.basename(file)
        #         if not container_client.get_blob_client(name).exists():
        #             container_client.upload_blob(name=name, data=data)

        for file in files:
            name = file.filename
            if not container_client.get_blob_client(name).exists():
                container_client.upload_blob(name=name, data=file.stream)

        print(f"Setup {len(files)} files in {blob_container_name} container.")
    
    @staticmethod
    def delete_container(
            blob_container_name: str,
            use_user_identity: bool = False,
    ):

        """
        ドキュメントをコンテナから削除する

        Args:
            blob_container_name (str): Blob Storage のコンテナ名
            use_user_identity (bool, optional): ユーザーの識別子を使用するかどうか。 Defaults to False.

        """

        blob_service_client: BlobServiceClient = BlobServiceClient.from_connection_string(logging_enable=True, conn_str=blob_connection_string, credential=DefaultAzureCredential() if use_user_identity else None)
        blob_service_client.delete_container(blob_container_name)
        print(f"Delete {blob_container_name} container.")