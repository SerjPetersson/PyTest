from pydantic import BaseModel, validator


class Schema(BaseModel):
    id: int
    title: str

    @validator('id')
    def check_id(cls,v):
        if v > 2:
            raise ValueError('ID is not less than 2')
        else:
            return v





    #[{'id': 1, 'title': 'Post 1'},