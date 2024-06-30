menu_directory = [{'title': 'Контрагенты', 'ref': 'сlients'}, {'title': 'Номенклатура', 'ref': 'goods'},
                  {'title': 'Торговые', 'ref': 'employees'}]
menu_documents = ["Продажи", "Оплаты", "Возвраты"]
menu_reports = [{'title': 'Продажи', 'ref': 'reports_salary'},
                {'title': 'Оплаты', 'ref': 'reports_salary'},
                {'title': 'Взаиморасчеты', 'ref': 'reports_salary'},
                {'title': 'Валюты', 'ref': 'reports_currencies'}
                ]
class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu_directory'] = menu_directory
        context['menu_documents'] = menu_documents
        context['menu_reports'] = menu_reports
        return context

    def get_menu_context( **kwargs):
        context = kwargs
        context['menu_directory'] = menu_directory
        context['menu_documents'] = menu_documents
        context['menu_reports'] = menu_reports
        return context