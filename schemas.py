from sqlmodel import SQLModel, Field

class SomeData(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content : str