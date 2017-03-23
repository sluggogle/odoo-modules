# coding: utf-8
{
    "name": "MRP Preview Lot",

    "summary": """
View the potential lot number of the current manufacturing order.
""",

    "description":"""
Adds a field in the manufacturing order form showing the potential lot for the selected product.
The MO has to be in state 'confirmed', 'ready' or 'in_production'.\n\n

Be aware that the real and final lot number will be created and assigned as usual.\n
""",

    "version": "8.0.1",
    "author": "Laboratoires Bories",
    "category": "Mrp",
    "website": "www.laboratoires-bories.com",
    "depends": [
        "mrp", "ir_sequence_preview", "product_category_lot",
    ],
    "demo": [],
    "data": [
        "mrp_view.xml"
    ],
    "test": [],
    "js": [],
    "css": [],
    "qweb": [],
    "installable": True,
    "auto_install": False,
}
