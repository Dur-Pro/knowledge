# Copyright (C) 2013 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Document Page Approval",
    "version": "17.0.1.1.0",
    "author": "Savoir-faire Linux, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/knowledge",
    "license": "AGPL-3",
    "category": "Knowledge Management",
    "description": """
This module allows to approve pages.
=====================================
This module allows to approve pages. Pages can be approved by a user with
the group "Document Page Manager" or by a user with the group "Document Page
Approver" and the same group as the page.
""",
    "depends": ["document_page", "mail"],
    "data": [
        "data/email_template.xml",
        "views/document_page_approval.xml",
        "security/document_page_security.xml",
        "security/ir.model.access.csv",
    ],
    "images": [
        "images/category.png",
        "images/page_history_list.png",
        "images/page_history.png",
    ],
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
    "installable": True,
}
