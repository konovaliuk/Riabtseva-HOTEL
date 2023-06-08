import secrets
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from config import Configuration
from app import app

if __name__ == '__main__':
    app.secret_key = 'ImNhODJhMTg4YzVkNGJjNDMxZThiMDE0ZDIwZDkzMjk5MDY4YTRiZTEi.ZE6mJQ.R1KoHw0hNwg4TvTO0R_KHSeFqnc'

    bootstrap = Bootstrap(app)
    app.run()
