# Copyright 2019 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Document Page Reference",
    "summary": """
        Include references on document pages""",
<<<<<<< HEAD
    "version": "17.0.1.0.0",
=======
    "version": "16.0.1.0.1",
>>>>>>> 77fead85e1b2b468438f3130e2f9630b2e7aebe6
    "license": "AGPL-3",
    "author": "Creu Blanca,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/knowledge",
    "depends": ["document_page", "web_editor"],
    "data": [
        "views/document_page.xml",
        "views/report_document_page.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "document_page_reference/static/src/js/**/*",
        ],
    },
    "maintainers": ["etobella"],
}
