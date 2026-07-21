import os
from typing import AsyncGenerator
from functools import lru_cache
from src.db.database import AsyncSessionLocal
from src.ingestion.bucket_client import BucketClient

async def get_db() -> AsyncGenerator:
    async with AsyncSessionLocal() as session:
        yield session


@lru_cache(maxsize=1)
def get_bucket_client() -> BucketClient:
    return BucketClient(
        bucket_name=os.environ["S3_BUCKET_NAME"],
        endpoint_url=os.environ["S3_ENDPOINT_URL"],
        access_key=os.getenv("S3_ACCESS_KEY"),
        secret_key=os.getenv("S3_SECRET_KEY"),
        region=os.getenv("S3_REGION", "us-east-1"),
    )


def bucket_client_dep() -> BucketClient:
    return get_bucket_client()