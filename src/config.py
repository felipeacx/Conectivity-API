import os

from dotenv import load_dotenv

load_dotenv()

user = os.environ["POSTGRES_USER"]
ps = os.environ["POSTGRES_PASSWORD"]
db = os.environ["POSTGRES_DATABASE"]
host = os.environ["POSTGRES_HOST"]

DB_CONNECTION_URI = f'postgresql://{user}:{ps}@{host}/{db}'
