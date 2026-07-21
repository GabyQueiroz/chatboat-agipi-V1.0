import io
from pathlib import Path
from typing import Any

import boto3
from botocore.exceptions import ClientError


class BucketClient:
    def __init__(
        self,
        bucket_name: str,
        endpoint_url: str | None = None,
        access_key: str | None = None,
        secret_key: str | None = None,
        region: str = "us-east-1",
    ) -> None:
        self.bucket_name = bucket_name
        self._client = boto3.client(
            "s3",
            endpoint_url=endpoint_url,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region,
        )

    def is_available(self) -> bool:
        try:
            self._client.head_bucket(Bucket=self.bucket_name)
            return True
        except Exception:
            return False

    def list_objects(self, prefix: str = "") -> list[dict[str, Any]]:
        objects = []
        paginator = self._client.get_paginator("list_objects_v2")
        for page in paginator.paginate(Bucket=self.bucket_name, Prefix=prefix):
            for obj in page.get("Contents", []):
                objects.append({
                    "key": obj["Key"],
                    "size": obj["Size"],
                    "etag": obj["ETag"].strip('"'),
                    "last_modified": obj["LastModified"].isoformat(),
                })
        return objects

    def download_file(self, key: str, destination: Path) -> Path:
        destination.parent.mkdir(parents=True, exist_ok=True)
        self._client.download_file(self.bucket_name, key, str(destination))
        return destination

    def read_bytes(self, key: str) -> bytes:
        response = self._client.get_object(Bucket=self.bucket_name, Key=key)
        return response["Body"].read()

    def upload_file(self, source: Path, key: str) -> None:
        self._client.upload_file(str(source), self.bucket_name, key)

    def upload_bytes(self, data: bytes, key: str, content_type: str = "application/octet-stream") -> None:
        self._client.put_object(
            Bucket=self.bucket_name,
            Key=key,
            Body=io.BytesIO(data),
            ContentType=content_type,
        )

    def object_etag(self, key: str) -> str | None:
        try:
            response = self._client.head_object(Bucket=self.bucket_name, Key=key)
            return response["ETag"].strip("")
        except ClientError:
            return None

    def delete_object(self, key: str) -> None:
        self._client.delete_object(Bucket=self.bucket_name, Key=key)