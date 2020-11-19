from django.contrib import admin
from products.models import Product, Images, Showcase, ShowcaseInfo


def make_published(modeladmin, request, queryset):
    queryset.update(active=True)


make_published.short_description = "Active"


def make_unpublished(modeladmin, request, queryset):
    queryset.update(active=False)


make_unpublished.short_description = "Deactive"


class ProductAdmin(admin.ModelAdmin):
    exclude = ('id', 'owner',)
    list_filter = (
        ('active', admin.BooleanFieldListFilter),
    )
    list_display = ('name', 'active', 'price', 'unit_price')
    list_editable = ('active', 'price')
    actions = [make_published, make_unpublished]

    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)


class ShowcaseAdmin(admin.ModelAdmin):
    exclude = ('id', 'owner')

    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(ShowcaseAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)


class ShowcaseInfoAdmin(admin.ModelAdmin):
    exclude = ('id', 'owner', 'showcase')

    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(ShowcaseInfoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)


admin.site.register(Product, ProductAdmin)
admin.site.register(Showcase, ShowcaseAdmin)
admin.site.register(ShowcaseInfo, ShowcaseInfoAdmin)
