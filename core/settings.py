import os

# Root directory
ROOT_DIR = os.path.dirname(os.path.abspath("."))

# DATABASE PATH (Local only)
DB_PATH = os.path.join(ROOT_DIR, 'airport.db')
# DATABASE URL 
DB_URL = 'sqlite:///' + DB_PATH
