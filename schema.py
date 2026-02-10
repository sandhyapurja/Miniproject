from pydantic import BaseModel, Field

class ThemedWordList(BaseModel):
    """Schema for themed word list generation"""
    words: list[str] = Field(
        description="List of unique words or phrases related to the theme"
    )