"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import (home,
                    # todoListCreate,
                    # todoList,
                    # todoListUpdate,
                    # todoListDelete,
                    # todoDetail,
                    # TodoList,
                    # TodoDetail,
                    # TodoListCreate,
                    # TodoRetrieveUpdateDelete,
                    # TodoConcListCreate,
                    # TodoConcRetreiveUpdateDelete,
                    # TodoVSRetrieve,
                    TodoMVS
                                      
                    )

from rest_framework import routers

router = routers.DefaultRouter()
# router.register('todovs-list',TodoVSRetrieve )
router.register('todomvs',TodoMVS )


urlpatterns = [
    path('', home, name='home'),
    
    #@api_view
    # path('todoList/', todoList, name='todoList'), # combined
    # # path('todoListCreate/', todoListCreate, name='todoListCreate'),
    # # path('todoListUpdate/<int:pk>', todoListUpdate, name='todoListUpdate'),
    # # path('todoListDelete/<int:pk>', todoListDelete, name='todoListDelete'),
    # path('todoDetail/<int:pk>', todoDetail, name='todoDetail'),
    
    #API View
    # path('todo-list/', TodoList.as_view()),
    # path('todo-detail/<int:pk>', TodoDetail.as_view()),
    
    #GENERIC View
    # path('todo-list/', TodoListCreate.as_view()),
    # path('todo-detail/<int:pk>', TodoRetrieveUpdateDelete.as_view()),
    
    #GENERIC View
    # path('todo-list/', TodoConcListCreate.as_view()),
    # path('todo-detail/<int:pk>', TodoConcRetreiveUpdateDelete.as_view()),
    path('', include(router.urls))
]

