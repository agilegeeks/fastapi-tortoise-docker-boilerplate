from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class SampleModel(models.Model):
    sample = fields.TextField()

    def __str__(self) -> str:
        return self.sample


SampleSchema = pydantic_model_creator(SampleModel)
