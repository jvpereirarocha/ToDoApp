from flask import Blueprint, jsonify


task_todo_bp = Blueprint("task-todo", __name__, url_prefix="/todo")


@task_todo_bp.route("/")
def hello():
    data = {"message": "Hello"}
    return jsonify(data), 200
