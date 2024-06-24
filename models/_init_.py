#!/usr/bin/python3
"""
initialize the hospital_models package
"""

from os import getenv

storage_t = getenv("HOSPITAL_TYPE_STORAGE")

if storage_t == "db":
    from hospital_models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from hospital_models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
