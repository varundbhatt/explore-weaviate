import weaviate
from weaviate.classes.init import Auth
import os

from dotenv import load_dotenv

load_dotenv() 

openai_key = os.getenv("OPENAI_APIKEY")
studio_key = os.getenv("STUDIO_APIKEY")
weaviate_url = os.getenv("WEAVIATE_URL")
weaviate_key = os.getenv("WEAVIATE_KEY")

headers = {
    "X-OpenAI-Api-Key": openai_key,
    "X-Goog-Studio-Api-Key": studio_key
}

def build_weaviate_client():
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=weaviate_url,
        auth_credentials=Auth.api_key(weaviate_key),
        headers=headers
    )
    return client

