from django.contrib import admin
from .models import Customer, Product_cls, Product, Item_cls, Supplier, Purchase, Purchase2,ItemStock,ItemStatus,ItemClsDiffer,Sale,SaleEntry,AuthUser
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product_cls)
admin.site.register(AuthUser)
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['sales_item_id','quantity','rate','sale_id']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_product_cls']
@admin.register(Item_cls)
class ItemClsAdmin(admin.ModelAdmin):
    list_display = ['item_cls_id','packed','same','item_cls_name','no_of_diff']
admin.site.register(Supplier)
admin.site.register(Purchase)
admin.site.register(SaleEntry)
@admin.register(ItemClsDiffer)
class ItemClsDiffer(admin.ModelAdmin):
    list_display = ['specification','item_cls_id','item_cls_differ_id']
@admin.register(Purchase2)
class PurchaseTwoAdmin(admin.ModelAdmin):
    list_display = ['purchase_id','purchase_item_cls']
@admin.register(ItemStock)
class ItemStockAdmin(admin.ModelAdmin):
    list_display = ['quantity', 'item_cls_id']
@admin.register(ItemStatus)
class ItemStatusAdmin(admin.ModelAdmin):
    list_display = ['item_id','barcode', 'purchase_rate','item_cls_status_id','sales_status','purchase_id','status_qty']