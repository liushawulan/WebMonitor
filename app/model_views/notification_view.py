#!/usr/bin/env python
# coding=UTF-8
'''
@Author: LogicJake
@Date: 2019-03-24 11:01:56
@LastEditTime: 2019-03-26 20:51:47
'''
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for
from flask_login import current_user


class NotificationView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('main.login'))

    can_create = False
    can_delete = False

    column_labels = {'type': '通知方式', 'number': '邮箱地址/Server酱 SCKEY'}

    form_widget_args = {'type': {'readonly': True}}
