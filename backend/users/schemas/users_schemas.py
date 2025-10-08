from pydantic import BaseModel


class UsersSchemas(BaseModel):
    name: str

    class config:
        orm = True
