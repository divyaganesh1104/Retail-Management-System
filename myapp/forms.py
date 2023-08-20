from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Product_cls, Product, Item_cls, Customer, Supplier, ItemStatus, ItemClsDiffer, AuthUser


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form=-control'
            }
        )
    )

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    class Meta:
        model = AuthUser
        fields = { 'username', 'password1', 'password2', 'email', 'is_admin','is_manager', 'is_salesperson'}
class UpdateFormPC(forms.ModelForm):
    class Meta:
        model = Product_cls
        fields = [
            'product_cls_id',
            'product_cls_name'
        ]


class UpdateFormItem(forms.ModelForm):
    class Meta:
        model = ItemStatus
        fields = [
            'selling_price',
            'discount',
            'image'
        ]


class UpdateFormP(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_id',
            'product_name',
            'product_product_cls'
        ]


class UpdateFormIC(forms.ModelForm):
    class Meta:
        model = Item_cls
        fields = [
            'item_cls_id',
            'item_cls_name',
            'item_product'
        ]




class UpdateFormC(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'custom_id',
            'first_name',
            'last_name',
            'custom_contact',
            'custom_add'
        ]


class UpdateFormS(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'supplier_id',
            'supplier_name',
            'supplier_phone'
        ]



class UpdateFormItemDiffer(forms.ModelForm):
    class Meta:
        model = ItemClsDiffer
        fields = [
            'item_cls_id',
            'item_cls_differ_id',
            'specification'
        ]
