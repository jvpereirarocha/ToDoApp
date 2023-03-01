from flask import Blueprint

from .task_todo import task_todo_bp


api_bp = Blueprint("api", __name__, url_prefix="/api/v1/")

api_bp.register_blueprint(task_todo_bp)
