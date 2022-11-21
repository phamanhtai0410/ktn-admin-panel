# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask_admin.form import RenderTemplateWidget


class DependSelectWidget(RenderTemplateWidget):
    def __init__(self, depend_field):
        super(DependSelectWidget, self).__init__('widgets/nft_types.html')
