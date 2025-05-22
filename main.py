from fastapi import FastAPI
from pydantic import BaseModel

# Create a FastAPI application instance.
# This 'app' object is the main entry point for your API.
app = FastAPI()

# Define a Pydantic model for the "Hello World!" message.
# This provides a clear structure and type validation for the response.
class Message(BaseModel):
    message: str

# Define a Pydantic model for an item.
# This ensures that items returned from the API have a consistent structure.
class Item(BaseModel):
    item_id: int
    query_param: str | None = None # Use | None for optional types in Python 3.10+

# Define a GET endpoint for the root URL ("/").
# The `@app.get("/")` decorator tells FastAPI that the `read_root` function
# should be executed when an HTTP GET request is made to the root path.
@app.get("/", response_model=Message)
async def read_root() -> Message:
    """
    This is a simple GET endpoint that returns a classic "Hello World!" message.
    FastAPI uses this docstring to automatically populate the description
    of this endpoint in the generated OpenAPI documentation.
    """
    # Return an instance of the Pydantic Message model.
    # FastAPI will automatically convert this into a JSON response,
    # validating it against the `response_model` defined in the decorator.
    return Message(message="Hello World!")

# You can add more endpoints here if you want to expand your API later.
# For example:
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int, q: str | None = None) -> Item:
    """
    Retrieves an item by its ID, with an optional query parameter.
    """
    # Return an instance of the Pydantic Item model.
    # This ensures the response adheres to the defined Item structure.
    return Item(item_id=item_id, query_param=q)
