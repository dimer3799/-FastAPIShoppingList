from yaml import SafeLoader, load

CONFIG_FILE = "settings.yaml"


class Settings:
    pg_host: str = "127.0.0.1"
    pg_port: int = 5432
    pg_user: str = "postgres"
    pg_password: str = "postgres"
    pg_database: str = "executive_journal"

    def __init__(self):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = load(f, SafeLoader)
            if postgres := config.get("Postgres"):
                self.pg_host = postgres.get("host", self.pg_host)
                self.pg_port = int(postgres.get("port", self.pg_port))
                self.pg_user = postgres.get("user", self.pg_user)
                self.pg_password = postgres.get("password", self.pg_password)
                self.pg_database = postgres.get("database", self.pg_database)
