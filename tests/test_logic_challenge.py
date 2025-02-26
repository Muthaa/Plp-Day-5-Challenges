import logic_challenge
import pytest

@pytest.fixture
def clear_orders():
    """Fixture to clear orders dictionary before each test."""
    logic_challenge.orders.clear()
    return logic_challenge.orders

def test_black_coffee_order(monkeypatch, clear_orders):
    """Test ordering Black Coffee."""
    inputs = iter(["a", "a", "John", "none"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    logic_challenge.coffee_or_tea()

    assert "John" in logic_challenge.orders
    assert logic_challenge.orders["John"] == "Black Coffee"

def test_coffee_with_milk_order(monkeypatch, clear_orders):
    """Test ordering Coffee with Milk."""
    inputs = iter(["a", "b", "Alice", "none"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    logic_challenge.coffee_or_tea()

    assert "Alice" in logic_challenge.orders
    assert logic_challenge.orders["Alice"] == "Coffee with Milk"

def test_green_tea_order(monkeypatch, clear_orders):
    """Test ordering Green Tea."""
    inputs = iter(["b", "a", "Tom", "none"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    logic_challenge.coffee_or_tea()

    assert "Tom" in logic_challenge.orders
    assert logic_challenge.orders["Tom"] == "Green Tea"

def test_tea_with_milk_order(monkeypatch, clear_orders):
    """Test ordering Tea with Milk."""
    inputs = iter(["b", "b", "Emma", "none"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    logic_challenge.coffee_or_tea()

    assert "Emma" in logic_challenge.orders
    assert logic_challenge.orders["Emma"] == "Tea with Milk"
