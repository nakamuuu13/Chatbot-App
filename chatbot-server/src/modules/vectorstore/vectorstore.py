import os

from dotenv import load_dotenv
from azure.search.documents.indexes.models import (
    SearchIndex,
)

from modules.vectorstore.blob_storage import BlobStorageManager
from modules.vectorstore.ai_search import (
    AiSearchManager,
    AiSearchSkillsetManager,
    AiSearchIndexerManager,
    AiSearchSearchManager,
)
from modules.document_structuring.document_structuring import DocumentStructuring

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

        # index_name = f"{name}-index"
        # index_description = description
        # blob_container_name = f"{name}-container"

        # BlobStorageManager.upload_documents(
        #     files=files,
        #     blob_container_name=blob_container_name
        # )
        # data_source = AiSearchManager.connect_to_container_index(
        #     blob_container_name=blob_container_name,
        #     index_name=index_name
        # )
        # seearch_index: SearchIndex = AiSearchManager.create_index(
        #     index_name=index_name
        # )
        # AiSearchSkillsetManager.create_skillset(
        #     index_name=index_name
        # )
        # AiSearchIndexerManager.create_indexer(
        #     index_name=index_name,
        #     data_source=data_source
        # )
        # print(f"Vectorstore '{name}' created.")

        try :
        
            DocumentStructuring.invoke(
                files=files,
                name=name
            )

        except Exception as e:
            print(e)
        
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

        index_name = f"{name}-index"
        blob_container_name = f"{name}-container"

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
    
    @staticmethod
    def search_vectorstore(
            name: str,
            query: str
    ):
        """
        検索を実行する

        Args:
            name (str): ベクトルストアの名前
            query (str): 検索クエリ

        Returns:
            search_results (SearchResults): 検索結果
        """

        index_name = f"{name}-index"

        search_results = AiSearchSearchManager.search(
            index_name=index_name,
            query=query
        )

        return search_results