from sqlalchemy.orm import DeclarativeBase


class BaseOrmModel(DeclarativeBase):
    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if key in self.__table__.columns.keys()}
