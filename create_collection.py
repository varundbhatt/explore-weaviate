import weaviate.classes as wvc
from clients import build_weaviate_client

client = build_weaviate_client()

def create_collection():
    try:
        client.collections.create(
            name="Jobs",
            vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_google_aistudio(model_id="text-embedding-004"),    # Set the vectorizer to "text2vec-openai" to use the OpenAI API for vector-related operations
            properties=[
                wvc.config.Property(
                    name="job_id",
                    data_type=wvc.config.DataType.INT,
                    skip_vectorization=True,
                ),
                wvc.config.Property(
                    name="company",
                    data_type=wvc.config.DataType.TEXT,
                    skip_vectorization=True,
                    tokenization=wvc.config.Tokenization.WORD
                ),
                wvc.config.Property(
                    name="job_title",
                    data_type=wvc.config.DataType.TEXT,
                    skip_vectorization=False,
                    tokenization=wvc.config.Tokenization.WORD
                ),
                wvc.config.Property(
                    name="job_description",
                    data_type=wvc.config.DataType.TEXT,
                    skip_vectorization=False,
                    tokenization=wvc.config.Tokenization.WORD
                ),
                wvc.config.Property(
                    name="location",
                    data_type=wvc.config.DataType.TEXT,
                    skip_vectorization=True,
                    tokenization=wvc.config.Tokenization.WORD
                ),
                wvc.config.Property(
                    name="industry",
                    data_type=wvc.config.DataType.TEXT,
                    skip_vectorization=True,
                    tokenization=wvc.config.Tokenization.WORD
                ),
                wvc.config.Property(
                    name="date_posted",
                    data_type=wvc.config.DataType.DATE,
                    skip_vectorization=True,
                ),
                wvc.config.Property(
                    name="salary_min",
                    data_type=wvc.config.DataType.INT,
                    index_range_filters=True
                ),
                wvc.config.Property(
                    name="salary_max",
                    data_type=wvc.config.DataType.INT,
                    index_range_filters=True
                ),
                wvc.config.Property(
                    name="funding_stage",
                    data_type=wvc.config.DataType.TEXT,
                    skip_vectorization=True,
                    tokenization=wvc.config.Tokenization.WORD
                ),
                wvc.config.Property(
                    name="visa_sponsorship",
                    data_type=wvc.config.DataType.TEXT,
                    skip_vectorization=True,
                    tokenization=wvc.config.Tokenization.WORD
                ),
                
            ]
        )

    finally:
        client.close()

create_collection()
