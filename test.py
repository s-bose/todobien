import sqlite3
from todobien.config import settings
import os


cursor = sqlite3.connect(str(settings.SQLITE_DB_PATH))
