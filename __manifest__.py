# -*- coding: utf-8 -*-
{
    'name': "Mommy Base",

    'summary': """
        Basic feature powered by Odoomommy.com
    """,

    'description': """
        1. 支持指定计算字段分组汇总
        2. 快速编辑功能可控
        3. 控制个人编辑区域显示效果
        4. 设置系统标题
    """,

    'author': "Kevin Kong",
    'website': "http://www.odoomommy.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'basic',
    'version': '15.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/data.xml',
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/settings.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "assets": {
        "web.assets_backend":[
            "mommy_base/static/src/js/mommy.js",
            # "mommy_base/static/src/js/relation_fields.js",
        ],
        "web.assets_qweb":[
            "mommy_base/static/srx/xml/*"
        ]
    }
}
