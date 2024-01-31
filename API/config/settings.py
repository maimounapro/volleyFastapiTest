from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGO_INITDB_DATABASE: str
    DATABASE_URL: str

    # JWT_PUBLIC_KEY: str
    # JWT_PRIVATE_KEY: str
    # REFRESH_TOKEN_EXPIRES_IN: int
    # ACCESS_TOKEN_EXPIRES_IN: int
    # JWT_ALGORITHM: str

    CLIENT_ORIGIN: str
    ALGORITHM: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = 'API/.env'


settings = Settings()



