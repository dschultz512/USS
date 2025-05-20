import json
import os
from java.io import FileReader

class SimpleJSONValidator:
    def __init__(self, schema_path="B2MML-BatchML.json"):
        self.schema = self._load_schema(schema_path)

    def _load_schema(self, path):
        with open(path, 'r') as f:
            return json.load(f)

    def validate(self, data):
        errors = []
        self._validate_properties(data, self.schema.get("properties", {}), self.schema.get("required", []), errors)
        return (len(errors) == 0), errors

    def _validate_properties(self, data, properties, required_fields, errors):
        for key in required_fields:
            if key not in data:
                errors.append("Missing required field: %s" % key)

        for prop, definition in properties.items():
            if prop in data:
                expected_type = definition.get("type")
                if expected_type and not self._check_type(data[prop], expected_type):
                    errors.append("Field '%s' should be of type %s" % (prop, expected_type))

    def _check_type(self, value, expected_type):
        type_map = {
            "string": basestring,
            "number": (int, float),
            "integer": int,
            "boolean": bool,
            "object": dict,
            "array": list,
        }
        return isinstance(value, type_map.get(expected_type, object))
