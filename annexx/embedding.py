from langchain_openai.embeddings import AzureOpenAIEmbeddings

from utils.config_loader import load_config

embedding_config = load_config()['embedding']['azure-openai']

embed = AzureOpenAIEmbeddings(
    model=embedding_config['model'],
    api_version=embedding_config['api-version'],
    api_key=embedding_config['api-key'],
    azure_endpoint=embedding_config['endpoint'],
)
