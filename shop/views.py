from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, FormView
from rest_framework import generics
from cart.forms import CartAddProductForm
from .forms import UserCreateForm
from .models import Product, Category


def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/product_list.html', {'products': products,
                                                              'categories': categories,
                                                              'category': category
                                                              })


def product_detail(request, id, slug):
    cart_product_form = CartAddProductForm()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/product_detail.html', {'product': product,
                                                                'cart_product_form': cart_product_form,
                                                                })


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = "/shop_login"
    template_name = "shop/product/shop_register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "shop/product/shop_login.html"
    success_url = "/"

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(LoginFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginFormView, self).form_invalid(form)


class LogoutView(TemplateView):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
