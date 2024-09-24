import os

from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.identity import DefaultAzureCredential
from azure.search.documents.indexes import SearchIndexerClient, SearchIndexClient
from azure.search.documents.indexes.models import (
    NativeBlobSoftDeleteDeletionDetectionPolicy,
    SearchIndexerDataContainer,
    SearchIndexerDataSourceConnection,
    SearchField,
    SearchFieldDataType,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
    AzureOpenAIVectorizer,
    AzureOpenAIParameters,
    SemanticConfiguration,
    SemanticSearch,
    SemanticPrioritizedFields,
    SemanticField,
    SearchIndex,
    SplitSkill,
    InputFieldMappingEntry,
    OutputFieldMappingEntry,
    AzureOpenAIEmbeddingSkill,
    SearchIndexerIndexProjections,
    SearchIndexerIndexProjectionSelector,
    SearchIndexerIndexProjectionsParameters,
    IndexProjectionMode,
    SearchIndexerSkillset,
    CognitiveServicesAccountKey,
    SearchIndexer,
)

load_dotenv(override=True)
endpoint: str = os.environ["AZURE_SEARCH_SERVICE_ENDPOINT"]
credential: object = AzureKeyCredential(os.getenv("AZURE_SEARCH_ADMIN_KEY")) if os.getenv("AZURE_SEARCH_ADMIN_KEY") else DefaultAzureCredential()
blob_connection_string: str = os.environ["BLOB_CONNECTION_STRING"]
search_blob_connection_string: str = os.getenv("SEARCH_BLOB_DATASOURCE_CONNECTION_STRING", blob_connection_string)

azure_openai_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
azure_openai_key = os.getenv("AZURE_OPENAI_KEY")
azure_openai_embedding_deployment = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-large")
azure_openai_model_name = os.getenv("AZURE_OPENAI_EMBEDDING_MODEL_NAME", "text-embedding-3-large")
azure_openai_model_dimensions = int(os.getenv("AZURE_OPENAI_EMBEDDING_DIMENSIONS", 3072))

azure_ai_services_key = os.getenv("AZURE_AI_SERVICES_KEY", "")

class AiSearchManager:

    @staticmethod
    def connect_to_container_index(
            blob_container_name: str,
            index_name: str,
    ):
        """
        コンテナとインデックスを接続する

        Args:
            blob_container_name (str): Blob Storage のコンテナ名
            index_name (str): AI Search のインデックス名
            
        Returns:
            data_source (SearchIndexer): Blob Storage と AI Search を接続したインデクサー
                
        """
        indexer_client: SearchIndexerClient = SearchIndexerClient(endpoint, credential)
        container: SearchIndexerDataContainer = SearchIndexerDataContainer(name=blob_container_name)
        data_source_connection: SearchIndexerDataSourceConnection = SearchIndexerDataSourceConnection(
            name=f"{index_name}-blob",
            type="azureblob",
            connection_string=search_blob_connection_string,
            container=container,
            data_deletion_policy=NativeBlobSoftDeleteDeletionDetectionPolicy()
        )
        data_source: SearchIndexer = indexer_client.create_or_update_data_source_connection(data_source_connection)
        print(f"Connected to container '{blob_container_name}' and index '{index_name}'")

        return data_source

    @staticmethod
    def create_index(
            index_name: str
    ):
        """
        AI Search のインデックスを作成する

        Args:
            index_name (str): AI Search のインデックス名
            
        Returns:
            search_index (SearchIndex): AI Search のインデックス
        """

        index_client: SearchIndexClient = SearchIndexClient(endpoint, credential)
        fields: list = AiSearchManager.create_index_fields()
        vector_search: VectorSearch = AiSearchManager.create_vector_search()
        semantic_search: SemanticSearch = AiSearchManager.create_semantic_search()

        index = SearchIndex(
            name=index_name,
            fields=fields,
            vector_search=vector_search,
            semantic_search=semantic_search,
        )

        search_index: SearchIndex = index_client.create_or_update_index(index)
        print(f"Index '{search_index.name}' created.")

        return search_index


    @staticmethod
    def create_index_fields():
        """
        インデックスのフィールドを作成する

        Args:
            None

        Returns:
            fields (list): インデックスのフィールド
        """

        fields: list = [
            SearchField(name="parent_id", type=SearchFieldDataType.String, sortable=True, filterable=True, facetable=True),
            SearchField(name="title", type=SearchFieldDataType.String),
            SearchField(name="chunk_id", type=SearchFieldDataType.String, key=True, sortable=True, filterable=True, facetable=True, analyzer_name="keyword"),
            SearchField(name="chunk", type=SearchFieldDataType.String, sortable=False, filterable=False, facetable=False),
            SearchField(name="vector", type=SearchFieldDataType.Collection(SearchFieldDataType.Single), vector_search_dimensions=azure_openai_model_dimensions, vector_search_profile_name="myHnswProfile"),
        ]
        print("Index fields created.")

        return fields

    @staticmethod
    def create_vector_search():
        """
        ベクトル化の構成を作成する

        Args:
            None

        Returns:
            vector_search (VectorSearch): ベクトル化の構成
        """

        vector_search: VectorSearch = VectorSearch(
            algorithms=[
                HnswAlgorithmConfiguration(name="myHnsw"),
            ],
            profiles=[
                VectorSearchProfile(
                    name="myHnswProfile",
                    algorithm_configuration_name="myHnsw",
                    vectorizer="myOpenAI",
                )
            ],
            vectorizers=[
                AzureOpenAIVectorizer(
                    name="myOpenAI",
                    kind="azureOpenAI",
                    azure_open_ai_parameters=AzureOpenAIParameters(
                        resource_uri=azure_openai_endpoint,
                        deployment_id=azure_openai_embedding_deployment,
                        model_name=azure_openai_model_name,
                        api_key=azure_openai_key,
                    ),
                ),
            ],
        )
        print("Vector search created.")

        return vector_search

    @staticmethod
    def create_semantic_search(
            name: str = "my-semantic-config"
    ):
        """
        セマンティック検索の構成を作成する

        Args:
            name (str, optional): セマンティック検索の構成名

        Returns:
            semantic_search (SemanticSearch): セマンティック検索の構成
        """

        semantic_config: SemanticConfiguration = SemanticConfiguration(
            name=name,
            prioritized_fields=SemanticPrioritizedFields(
                content_fields=[SemanticField(field_name="chunk")]
            ),
        )

        semantic_search: SemanticSearch = SemanticSearch(
               configurations=[semantic_config],
        )
        print(f"Semantic configuration '{name}' created.")

        return semantic_search
    
    def delete_index(
            index_name: str
    ):
        """
        AI Search のインデックスを削除する

        Args:
            index_name (str): AI Search のインデックス名

        Returns:
            None
        """

        index_client: SearchIndexClient = SearchIndexClient(endpoint, credential)
        index_client.delete_index(index_name)
        print(f"Index '{index_name}' deleted.")

        return None

class AiSearchSkillsetManager:
    @staticmethod
    def create_skillset(
            index_name: str,
            description: str = "Skillset to chunk documents and generating embeddings",
    ):
        """
        AI Search のスキルセットを作成する

        Args:
            index_name (str): AI Search のインデックス名
            description (str): スキルセットの説明
            
        Returns:
            None
        """

        skillset_name = f"{index_name}-skillset"
        split_skill: SplitSkill = AiSearchSkillsetManager.create_split_skell()
        embedding_skill: AzureOpenAIEmbeddingSkill = AiSearchSkillsetManager.create_embedding_skill()
        index_projections: SearchIndexerIndexProjections = AiSearchSkillsetManager.create_index_projection(index_name)
        cognitive_services_account: CognitiveServicesAccountKey = AiSearchSkillsetManager.create_cognitive_services_account()

        skills = [split_skill, embedding_skill]

        skillset = SearchIndexerSkillset(
            name=skillset_name,
            description=description,
            skills=skills,
            index_projections=index_projections,
            cognitive_services_account=cognitive_services_account
        )
        client = SearchIndexerClient(endpoint, credential)
        client.create_or_update_skillset(skillset)
        print(f"Skillset '{skillset.name}' created.")

        return None


    @staticmethod
    def create_split_skell():
        """
        チャンク分割スキルの構成を作成する
        
        Args:
            None
            
        Returns:
            split_skill (SplitSkill): チャンク分割スキルの構成
        """

        split_skill: SplitSkill = SplitSkill(
            description="Split skill to chunk documents",
            text_split_mode="sentences",
            context="/document",
            inputs=[
                InputFieldMappingEntry(name="text", source="/document/content"),
            ],
            outputs=[
                OutputFieldMappingEntry(name="textItems", target_name="pages")
            ]
        )
        print("Split skill created.")

        return split_skill

    @staticmethod
    def create_embedding_skill():
        """
        Embeddingスキルの構成を作成する

        Args:
            None

        Returns:
            embedding_skill (AzureOpenAIEmbeddingSkill): Embeddingスキルの構成
        """

        embedding_skill: AzureOpenAIEmbeddingSkill = AzureOpenAIEmbeddingSkill(
            description="Skill to generate embeddings via Azure OpenAI",
            context="/document/pages/*",
            resource_uri=azure_openai_endpoint,
            deployment_id=azure_openai_embedding_deployment,
            model_name=azure_openai_model_name,
            dimensions=azure_openai_model_dimensions,
            api_key=azure_openai_key,
            inputs=[
                InputFieldMappingEntry(name="text", source="/document/pages/*"),
            ],
            outputs=[
                OutputFieldMappingEntry(name="embedding", target_name="vector")
            ]
        )
        print("Embedding skill created.")

        return embedding_skill
    
    @staticmethod
    def create_index_projection(
            index_name: str
    ):
        """
        インデックスへのターゲットの構成を作成する 

        Args:
            index_name (str): AI Search のインデックス名

        Returns:
            index_projections (SearchIndexerIndexProjections): インデックスへのターゲットの構成
        """
        index_projections: SearchIndexerIndexProjections = SearchIndexerIndexProjections(
            selectors=[
                SearchIndexerIndexProjectionSelector(
                    target_index_name=index_name,
                    parent_key_field_name="parent_id",
                    source_context="/document/pages/*",
                    mappings=[
                        InputFieldMappingEntry(name="chunk", source="/document/pages/*"),
                        InputFieldMappingEntry(name="vector", source="/document/pages/*/vector"),
                        InputFieldMappingEntry(name="title", source="/document/metadata_storage_name")
                    ]
                )
            ],
            parameters=SearchIndexerIndexProjectionsParameters(
                projection_mode=IndexProjectionMode.SKIP_INDEXING_PARENT_DOCUMENTS
            )
        )
        print("Index projection created.")

        return index_projections
    
    @staticmethod
    def create_cognitive_services_account():
        """
        Cognitive Service のアカウントを作成する

        Args:
            None

        Returns:
            cognitive_services_account (CognitiveServicesAccountKey): Cognitive Service のアカウント
        """

        cognitive_services_account: CognitiveServicesAccountKey = CognitiveServicesAccountKey(key=azure_ai_services_key) if use_ocr else None
        print("Cognitive services account created.")

        return cognitive_services_account
    
class AiSearchIndexerManager:
    @staticmethod
    def create_indexer(
            index_name: str,
            data_source: SearchIndexer,
            description: str = "Indexer to index documents and generate embeddings",
    ):
        """
        AI Search のインデクサーを作成する

        Args:
            index_name (str): AI Search のインデックス名
            data_source (SearchIndexer): Blob Storage と AI Search を接続したインデクサー
            
        Returns:
            None
        """

        indexer_name = f"{index_name}-indexer"
        skillset_name = f"{index_name}-skillset"
        indexer_parameters = None

        indexer = SearchIndexer(
            name=indexer_name,
            description=description,
            skillset_name=skillset_name,
            target_index_name=index_name,
            data_source_name=data_source.name,
            parameters=indexer_parameters
        )

        indexer_client: SearchIndexerClient = SearchIndexerClient(endpoint, credential)
        search_indexer: SearchIndexer = indexer_client.create_or_update_indexer(indexer)
        indexer_client.run_indexer(indexer_name)
        print(f"Indexer '{indexer_name}' created.")

        return None
    
    @staticmethod
    def delete_indexer(
            index_name: str
    ):
        """
        AI Search のインデクサーを削除する

        Args:
            index_name (str): AI Search のインデックス名

        Returns:
            None
        """

        indexer_name = f"{index_name}-indexer"
        indexer_client: SearchIndexerClient = SearchIndexerClient(endpoint, credential)
        indexer_client.delete_indexer(indexer_name)
        print(f"Indexer '{index_name}' deleted.")
        
        return None
