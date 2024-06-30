from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('сlients/', сlients, name='сlients'),
    path('goods/', goods, name='goods'),
    path('employees/', employees, name='employees'),
    path('сlient/<slug:client_slug>/', show_сlient, name='сlient'),
    path('reports_salary/', reports_salary, name='reports_salary'),
    path('reports_salary_manage/', reports_salary_manage, name='reports_salary_manage'),
    path('reports_salary_managers_сomparison/', reports_salary_managers_сomparison, name='reports_salary_managers_сomparison'),
    path('reports_currencies/', reports_currencies, name='reports_currencies'),
    path('reports_currencies_uah/', reports_currencies_uah, name='reports_currencies_uah'),
    path('notes/', NotesList.as_view(), name='notes'),
    path('show_note/<int:note_id>/', show_note, name='show_note'),
    path('add_note/', AddNote.as_view(), name='add_note'),
    path('delete_note/<int:note_id>/', delete_note, name='delete_note'),


]