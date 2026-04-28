from django.urls import path
from webapp import views
urlpatterns=[
    path('home_page/',views.home_page,name="home_page"),
    path('contact/',views.contact,name="contact"),
    path('product/',views.product,name="product"),
    path('single_products/<int:p_id>/',views.single_products,name="single_products"),
    path('product_filtered/<cate_name>/',views.product_filtered,name="product_filtered"),
    path('save_contacts/', views.save_contacts, name="save_contacts"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signup_save/', views.signup_save, name="signup_save"),
    path('about_us/', views.about_us, name="about_us"),
    path('signin_op/', views.signin_op, name="signin_op"),
    path('logoutpage/', views.logoutpage, name="logoutpage"),








]
