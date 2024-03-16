from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import Products

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )

    def post(self, request):
        if 'clear_cart' in request.POST:
            # Если в POST-запросе есть ключ "clear_cart", очищаем содержимое корзины
            request.session['cart'] = {}
            # Перенаправляем пользователя на страницу корзины после очистки
            return redirect('cart')  # Замените 'cart' на имя URL-шаблона для вашего представления корзины
        # Дополнительные обработки POST-запросов, если нужно