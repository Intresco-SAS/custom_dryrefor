# -*- coding: utf-8 -*-
{
    'author': 'Intresco SAS',
    'name': 'Project Task Paid',
    'version': '14.0.1',
    'category': 'Project',
    'summary': 'Add paid field to projects',
    'description': """
This module adds an option to mark as paid the task projects.
Also it adds a new view for project user group, to see only his tasks
============================================================
    """,
    'depends': [
        'project', 
        #'deltatech_widget_badge', 
        #'l10n_co_res_partner'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/project_task_view.xml',
        'wizard/project_task_cancel_wizard_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
