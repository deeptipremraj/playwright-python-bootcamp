"""Test data builders. Every call returns a brand new, unique user."""

import uuid


def build_user(**overrides) -> dict:
    token = uuid.uuid4().hex[:10]
    user = {
        "name": f"Tester{token}",
        "email": f"qa.{token}@example.com",
        "password": "Passw0rd!",
        "title": "Mrs",
        "birth_date": "10",
        "birth_month": "May",
        "birth_year": "1990",
        "firstname": "Test",
        "lastname": "User",
        "company": "Bootcamp",
        "address1": "1 Main Street",
        "address2": "Suite 2",
        "country": "United States",
        "zipcode": "10001",
        "state": "NY",
        "city": "New York",
        "mobile_number": "5551234567",
    }
    user.update(overrides)
    return user
