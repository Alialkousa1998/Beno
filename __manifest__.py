{
    'name': 'XYZ Event Management',
    'version': '1.0',
    'summary': 'Manage events and reminders for XYZ company',
    'description': """
        This module manages events and reminders for XYZ company,
        sending notifications to salespersons and allowing them
        to start communication with contacts.
    """,
    'author': 'Ali Alkousa',
    'website': 'http://www.xyz.com',
    'category': 'Sales',
    'depends': ['base', 'mail'],
    'data': [
        'data/event.xml',
        'views/res_partner_views.xml',
        'data/event_reminder_cron.xml',
        'data/event_reminder_email_template.xml',
        'views/event_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}