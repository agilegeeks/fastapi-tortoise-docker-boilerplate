# sample models
from pydantic import BaseModel


class SamplePayloadSchema(BaseModel):
    model: str


class SampleResponseSchema(SamplePayloadSchema):
    id: int
