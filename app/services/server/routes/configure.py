from .health import router as health_router
from .calculate_payment import router as calculate_payment_router

def configure_routes(app):
    app.register_blueprint(health_router)
    app.register_blueprint(calculate_payment_router)