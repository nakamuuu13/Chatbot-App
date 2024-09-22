import os

from dotenv import load_dotenv
from azure.search.documents.indexes.models import (
    SearchIndex,
)

from modules.vectorstore.blob_storage import BlobStorageManager
from modules.vectorstore.ai_search import (
    AiSearchManager,
    AiSearchSkillsetManager,
    AiSearchIndexerManager
)

load_dotenv(override=True)
index_name = os.getenv("AZURE_SEARCH_INDEX", "sample-vec")
blob_container_name = os.getenv("BLOB_CONTAINER_NAME", "sample-blob")

class VectorstoreManager:
    @staticmethod
    def create_vectorstore(
            files: list,
            name: str,
            description: str,
    ):

        """
        ベクトルストアを作成する

        Args:
            files (list): ファイルのリスト
            name (str): ベクトルストアの名前
            description (str): ベクトルストアの説明

        Returns:
            None

        """
        BlobStorageManager.upload_documents(
            files=files,
            blob_container_name=blob_container_name
        )
        AiSearchManager.connect_to_container_index(
            blob_container_name=blob_container_name,
            index_name=index_name
        )
        seearch_index: SearchIndex = AiSearchManager.create_index(
            index_name=index_name
        )
        AiSearchSkillsetManager.create_skillset(
            index_name=index_name
        )
        AiSearchIndexerManager.create_indexer(
            index_name=index_name,
            data_source=seearch_index
        )
        print(f"Vectorstore '{name}' created.")

        return None
    
    @staticmethod
    def delete_vectorstore(
            name: str
    ):
        """
        ベクトルストアを削除する

        Args:
            name (str): ベクトルストアの名前

        Returns:
            None
        """

        BlobStorageManager.delete_container(
            blob_container_name=blob_container_name
        )
        AiSearchManager.delete_index(
            index_name=index_name
        )
        AiSearchIndexerManager.delete_indexer(
            index_name=index_name
        )
        print(f"Vectorstore '{name}' deleted.")

        return None