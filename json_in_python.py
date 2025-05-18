# How does Python sees JSON data?

## 1. **As a String (Raw JSON)**
# - When you receive JSON data (for example, from a web API or a file), it is usually in the form of a **string**.
#
# json_string = '{"name": "Alice", "age": 30}'
# print(json_string)
# print(type(json_string))  # Output: str


## 2. **As a Python Data Structure (After Parsing)**
# - Python provides the `json` module to **parse** (deserialize) JSON strings into native Python data types
# (like dictionaries and lists).

print("------")

# - To parse a JSON string into a Python dict:
import json
json_string = '{"name": "Alice", "age": 30}'
data = json.loads(json_string)  # Now 'data' is a Python dict: {'name': 'Alice', 'age': 30}
print(data)
print(type(data))  # Output: dict

# - Similarly, you can **serialize** (convert) a Python data structure into a JSON string:
json_string = json.dumps(data)  # Now 'json_string' is a string: '{"name": "Alice", "age": 30}'
print(json_string)
print(type(json_string))  # Output: str


# **Summary Table**
#
# | In Python          | Example                               | Type              |
# |--------------------|---------------------------------------|-------------------|
# | JSON string        | `'{"name": "Alice", "age": 30}'`      | `str`             |
# | Python object      | `{'name': 'Alice', 'age': 30}`        | `dict` (or `list`)|
# | Parse JSON string  | `json.loads(json_string)`             | `dict`/`list`     |
# | Dump to JSON       | `json.dumps(python_object)`           | `str`             |

# **In summary:**
# - Python sees raw JSON as a **string**.
# - Use `json.loads()` to convert it to a Python object, and `json.dumps()` to convert a Python object back to a JSON string.

