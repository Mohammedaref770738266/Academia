# Copyright (c) 2024, SanU and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re

class FacultyMemberConferenceandWorkshop(Document):
    def validate(self):
        if not re.match("^[a-zA-Z ]*$", self.name1):
            frappe.throw("Name should only contain letters")
