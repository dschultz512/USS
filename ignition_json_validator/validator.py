import json
import requests
from jsonschema import validate, ValidationError
from .config import SCHEMA_URL, SCHEMA_CACHE_FILE
from .utils import load_or_fetch_schema

class JSONValidator:
    def __init__(self):
        self.schema = load_or_fetch_schema()

    def validate(self, data):
        try:
            validate(instance=data, schema=self.schema)
            return True, None
        except ValidationError as e:
            return False, str(e)
