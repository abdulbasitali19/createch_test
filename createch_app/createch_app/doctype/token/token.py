# Copyright (c) 2023, abdul basit  and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Token(Document):
    def validate(self):
        # Check if the validity date of the token is equal to or before the invoice posting date
        if self.validity_date > self.get("invoice_posting_date"):
            frappe.throw(
                "The validity date of the token must be equal to or before the invoice posting date.")

        # Check if the token is already issued for some other invoice
        if self.is_issued and self.get("issued_invoice"):
            frappe.throw(
                "The token has already been issued for another invoice.")
