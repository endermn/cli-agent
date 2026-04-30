from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	google_api_key: str = "sample_api_key"
	shell: str = ""
	app_data: str = ""

	class Config:
		env_file = ".env"


settings: Settings = Settings()
