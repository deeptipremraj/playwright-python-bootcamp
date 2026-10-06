"""Exercise 2 (UI): sign up through the browser.

1. Add `signup(name, email)` to LoginPage. Hint: data-qa values signup-name, signup-email,
   signup-button.
2. Fill the account form that follows. Hint: data-qa values password, first_name, last_name,
   address, state, city, zipcode, mobile_number, create-account. The title is a radio button.
3. Assert the "ACCOUNT CREATED!" heading.
4. Clean up. Create a fixture with `yield` that deletes the account through
   `account_api.delete_account(email, password)`. Use `build_user()` for unique data.
"""

import pytest

pytestmark = [pytest.mark.ui, pytest.mark.exercise]


def test_signup_creates_account():  # add the fixtures you need as arguments
    pytest.skip("TODO: complete exercise 2")
