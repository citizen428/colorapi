import hug
import colorapi
import pytest

response = hug.test.get(colorapi, 'color', {'name': 'red'})
assert(response.status) == '200 OK'
assert(response.content_type) == 'application/json'
