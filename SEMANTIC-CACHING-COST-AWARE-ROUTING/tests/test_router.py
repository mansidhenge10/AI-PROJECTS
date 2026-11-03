from app.router.model_router import ModelRouter
from app.config import SMALL_MODEL, LARGE_MODEL


def test_simple_query_uses_small_model():
    router = ModelRouter()

    model, route = router.route("Explain machine learning")

    assert model == SMALL_MODEL
    assert route == "fast"


def test_complex_query_uses_large_model():
    router = ModelRouter()

    model, route = router.route(
        "Compare supervised and unsupervised learning"
    )

    assert model == LARGE_MODEL
    assert route == "advanced"


def test_technical_query_uses_large_model():
    router = ModelRouter()

    model, route = router.route(
        "Debug this API and optimize its performance"
    )

    assert model == LARGE_MODEL
    assert route == "advanced"