# -*- coding: utf-8 -*-
from databases import Database
from settings import Settings

service_settings = Settings()


DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(
    service_settings.pg_user,
    service_settings.pg_password,
    service_settings.pg_host,
    service_settings.pg_port,
    service_settings.pg_database,
)
# databases query builder
database = Database(DATABASE_URL)
