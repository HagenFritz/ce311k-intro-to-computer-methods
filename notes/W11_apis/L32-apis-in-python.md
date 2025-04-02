# Using Python for API Calls

## Navigating API Documentation
### Understanding Endpoints
Endpoints are essentially the “doors” or “entry points” to access different parts of an API. You’ll often see them described in documentation like:
```
GET /data/3.0/onecall
POST /rest/v1.0/projects/{project_id}/rfis
```
They specify where you’re sending your request (e.g., `GET` or `POST`) and what resource or functionality you’re targeting. If the documentation is good, you’ll see examples showing how to form these endpoints (like adding IDs or using query parameters).

### Parameters
APIs typically handle three main types of parameters:
- **Query Parameters:** Key-value pairs at the end of a URL, such as `?limit=10`.
- **Path Parameters:** Values in the URL path itself, often in curly braces, like `/projects/{project_id}`.
- **Headers:** Metadata for requests, such as authentication tokens or content types.

Properly combining these can be the difference between a working request and a lovely 400 or 401 error.

### Request Body
Some APIs, especially when creating or updating data, require a request body in JSON format. An example might look like:
```json
{
  "folder": {
    "parent_id": 12,
    "name": "test_folder",
    "is_tracked": true
  }
}
```
The documentation should mention which fields are required and which are optional.

### Responses
The best docs show example responses—often in JSON—with status codes like `200` for success, or `401` when you forgot to copy your API key. A typical response might look like:
```json
{
  "id": 123,
  "status": "success"
}
```
Use these examples to sanity-check that your code is actually doing what you think it’s doing.

## Python’s requests Library
### Overview
`requests` is a super friendly library for making HTTP requests in Python. You can do things like:
```python
import requests

response = requests.get("https://api.example.com/data")
```
It handles all that messy HTTP under the hood.

### Defining Input Parameters
Success with `requests` comes down to setting headers and parameters just right. For instance:
```python
headers = {
    "x-api-key": "<Your-API-Key>",
    "Content-Type": "application/json"
}

params = {
    "limit": 3,
    "has_breeds": False
}
```
Keep an eye on the docs for the *exact* parameter names.

## Making API Requests in Python
### GET Requests
A GET request is used to fetch data. With `requests`:
```python
url = "https://api.thecatapi.com/v1/images/search"
headers = {"x-api-key": "<Your-API-Key>"}
params = {"limit": 5}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    print("Success! Here's your data:")
    print(response.json())
else:
    print(f"Failed. Status code: {response.status_code}")
```
Check `response.json()` or `response.text` to see what the server returned. If you see an error code, double-check those parameters and headers.

### POST Requests
POST is for sending or creating data on the server. For example, to “vote” for a cat image:
```python
url = "https://api.thecatapi.com/v1/votes"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "<Your-API-Key>"
}
payload = {
    "image_id": "bjl",  # Just an example ID
    "value": 1
}

response = requests.post(url, headers=headers, json=payload)
```
If all goes well, the server might return a `201 Created` response, or something similar. If you’re cursed with a 400 or 401, the first suspect is your payload formatting or missing headers.

### DELETE Requests
Finally, to remove an item—like a mistaken cat vote:
```python
url = "https://api.thecatapi.com/v1/votes/{vote_id}"
headers = {"x-api-key": "<Your-API-Key>"}

response = requests.delete(url, headers=headers)
```
If your vote ID is correct and your key is legit, you’ll hopefully see a 200 response.

## Putting It All Together
### A Quick Example Workflow
1. **Find the Endpoint:** Locate the endpoint in the docs, e.g. `/images/search` to fetch images.
2. **Gather Parameters & Headers:** Check if you need a path parameter like `{id}`, a query parameter like `?limit=10`, or any special headers.
3. **Send the Request:** Use `requests.get(...)` or another method, attach headers and parameters.
4. **Inspect the Response:** Check the status code and body. Convert to JSON with `.json()` when relevant.
5. **Handle Errors:** If it’s not `200`, figure out what you did wrong (which can be fun, I promise).

And that’s basically it. Once you grasp the docs, forming the correct requests becomes routine—until the next time you switch APIs and everything changes.