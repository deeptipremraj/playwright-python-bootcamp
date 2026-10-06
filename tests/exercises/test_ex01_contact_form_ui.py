"""Exercise 1 (UI): submit the Contact Us form.

1. Create `src/autoexercise/pages/contact_page.py` (path "/contact_us") and add a
   `contact_page` fixture in tests/ui/conftest.py.
   Hint: the fields use data-qa values: name, email, subject, message, submit-button.
   Hint: the file input is named upload_file. Use `set_input_files`.
2. Submitting opens a browser confirm dialog. Register the handler BEFORE the click:
   `page.once("dialog", lambda dialog: dialog.accept())`
3. Assert the green success message appears.
"""

import pytest

pytestmark = [pytest.mark.ui, pytest.mark.exercise]


def test_contact_form_submits():  # add the fixtures you need as arguments
    pytest.skip("TODO: complete exercise 1")
