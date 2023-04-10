from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    rdbms: str = "postgresql"
    connector: str = "asyncpg"
    host: str = "localhost"
    port: int = 5432
    database: str = "test"
    user: str = ""
    password: str = ""
    echo: bool = True

    @property
    def full_url(self) -> str:
        return "{}+{}://{}:{}@{}:{}/{}".format(
            self.rdbms, self.connector, self.user, self.password,
            self.host, self.port, self.database
        )
