from src.application.dto.release_dto import ReleaseInputDTO
from src.presentation.http.schemas.release import CreateReleaseRequest, CreateReleaseResponse, GetReleaseResponse

def pydantic_to_dto(input: CreateReleaseRequest):
    return ReleaseInputDTO(**input.model_dump())

def dto_to_pydantic(output):
    return CreateReleaseResponse(**output.to_dict())

def many_dto_to_pydantic(output):
    return tuple(GetReleaseResponse(**dto.to_dict()) for dto in output)
