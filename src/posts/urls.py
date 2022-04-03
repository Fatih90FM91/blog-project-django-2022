

from django.urls import path
from .views import HomeView
from .views import ArticleDetail
from.views import AddPost
from .views import UpdatePost
from .views import DeletePost
from .views import AddCategory
from .views import CategoryView
from .views import CategoryListView
from .views import LikeView
from .views import AddComment


urlpatterns = [
   path('' ,HomeView.as_view() , name='home'),
   path('article/<int:pk>' ,ArticleDetail.as_view() , name='article-detail'),
   path('add_post/' ,AddPost.as_view() , name='add-post'),
   path('add_category/' ,AddCategory.as_view() , name='add-category'),
   path('article/edit/<int:pk>' ,UpdatePost.as_view() , name='update-post'),
   path('article/<int:pk>/delete' ,DeletePost.as_view() , name='delete-post'),
   path('category/<str:cats>/', CategoryView, name='category'),
   path('category-list/', CategoryListView, name='category-list'),
   path('like/<int:pk>/', LikeView, name='like-post'),
   path('article/<int:pk>/comment' ,AddComment.as_view() , name='add-comment'),
]
