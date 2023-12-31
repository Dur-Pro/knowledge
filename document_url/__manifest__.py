# Copyright 2014 Tecnativa - Pedro M. Baeza
# Copyright 2020 Tecnativa - Manuel Calero
{
    "name": "URL attachment",
    "version": "16.0.1.0.3",
    "category": "Tools",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/knowledge",
    "license": "AGPL-3",
    "depends": ["mail"],
    "description": """
URL attachment
==============
This module allows to attach URL links to any model.
    """,
    "data": [
        "security/ir.model.access.csv",
        "view/document_url_view.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "document_url/static/src/js/url.esm.js",
            "document_url/static/src/xml/url.xml",
            "document_url/static/src/scss/document_url.scss",
        ],
    },
    "installable": True,
}
