from flask import Blueprint

auth = Blueprint('bot', __name__)

from . import   models, events


