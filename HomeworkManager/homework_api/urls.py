from django.urls import path, re_path
from . import views
from .views import deleteAssignment, createAssignment, updateAssignment, timeAssignment, deleteTimer, editTimer, loadData, manageTime, manageAverage

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path(r'^timemanagement?', manageTime),
    re_path(r'^averagemanagement?', manageAverage),
    path('loaddata', loadData, name='load-data'),
    path('<id>/delete', deleteAssignment),
    path('<id>/update', updateAssignment),
    path('create', createAssignment),
    path('<int:assignment_id>/',
         views.AssignmentDetailView.as_view(), name='assignment'),
    path('<int:assignment_id>/timer', timeAssignment),
    path('<int:assignment_id>/timer/delete/<id>', deleteTimer),
    path('<int:assignment_id>/timer/edit/<id>', editTimer)
]
