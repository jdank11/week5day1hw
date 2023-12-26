from flask import Flask

app = Flask(__name__)

from resources.mods import routes
from resources.cars import routes