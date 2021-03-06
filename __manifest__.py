{
    'name': '打印设计',
    'depends': ['base'],
    'author': 'www.mypscloud.com',
    'summary': """
            PSCloud Print
            """,
    'sequence': 100,
    'website': 'www.mypscloud.com',
    'data': [
        'views/menu_root.xml',
        'views/print_design_define.xml',
        'views/print_design_bill.xml',
        'views/print_design_bill2model.xml',
        'views/print_design_field.xml',
        'views/print_design_template_js.xml',
        'views/print_preview_template_js.xml',
        'views/print_button.xml',
        # 'wizard/print_account_act.xml', // 动作里面添加的打印功能,暂时去掉。story
        # 'data/print_account_move.xml',
        'security/ir.model.access.csv',
        ],
    'qweb': [
        "static/src/xml/print_design_template.xml",
        "static/src/xml/print_preview_template.xml",
        "static/src/xml/ps_button.xml",
        "static/src/xml/ps_button_format.xml",
        "static/src/xml/temp.xml",
        ],
    'js': ["static/src/js/*.js"],
    'js': ["static/src/dist/*.js"],
    'js': ["static/src/dist/ext/*.js"],
    'css': ["static/src/dist/*.css"],
    'css': ["static/src/dist/ext/*.css"],
    'application': True
}