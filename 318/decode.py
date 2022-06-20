import base64
import csv
from typing import List  # will remove with 3.9


def get_credit_cards(data: bytes) -> List[str]:
    """Decode the base64 encoded data which gives you a csv
    of "first_name,last_name,credit_card", from which you have
    to extract the credit card numbers.
    """
    decoded_data = base64.b64decode(data)
    reader = csv.DictReader(
        line.decode('utf-8') for line in decoded_data.splitlines())
    return [row["credit_card"] for row in reader]
