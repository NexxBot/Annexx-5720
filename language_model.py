from langchain_openai import AzureChatOpenAI

from utils.config_loader import load_config

config = load_config()
openai_config = config['llm']['azure-openai']

gpt_default = AzureChatOpenAI(
    model_name=openai_config['model-name'],
    api_version=openai_config['api-version'],
    api_key=openai_config['api-key'],
    temperature=0,
    azure_endpoint=openai_config['endpoint'],
)

gpt_35_turbo = AzureChatOpenAI(
    model_name='gpt-35-turbo-16k',
    api_version=openai_config['api-version'],
    api_key=openai_config['api-key'],
    temperature=0,
    azure_endpoint=openai_config['endpoint'],
)


def load_gpt_default():
    return gpt_default


def load_gpt_35_turbo():
    return gpt_35_turbo
