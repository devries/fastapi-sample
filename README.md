# FastAPI sample

## Running the project
Install the libraries using `uv` by running

```
uv sync
```

Then run the server with the command:

```
uv run uvicorn main:app --reload
```

## Endpoints

- [http://localhost:8000](http://localhost:8000) returns a Hello World JSON
  structure.
- [http://localhost:8000/items/123?q=hello](http://localhost:8000/items/123?q=hello)
  returns a JSON structure with the item id (123 in this case) and the query
  string ("hello" in this case) or null if there is no query string.

## Self-documentation
- [http://localhost:8000/docs](http://localhost:8000/docs) - Standard OpenAPI
  docs.
- [http://localhost:8000/redoc](http://localhost:8000/redoc) - Redocly docs.
- [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json) -
  OpenAPI JSON structure describing API.
