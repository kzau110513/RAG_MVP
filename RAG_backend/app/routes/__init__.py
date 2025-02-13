from flask import Blueprint
from app.routes.query import query_bp

def register_routes(app):
    # app.register_blueprint(query_bp, url_prefix="/api")
    app.register_blueprint(query_bp)
