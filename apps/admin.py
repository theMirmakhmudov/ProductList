from django.contrib import admin
from django.utils.html import format_html

from .models import Users, Product, Home1, Home2, Images, About1, AboutPerson, Persons, ContactForm, Contact


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    ...


@admin.register(Home1)
class Home1Admin(admin.ModelAdmin):
    list_display = ["image_tag", "txt", "description"]
    search_field = ["txt"]

    def image_tag(self, obj):
        return format_html(f'''<a href="{obj.image.image.url}" target="_blank"><img src="{obj.image.image.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')


@admin.register(Home2)
class Home2Admin(admin.ModelAdmin):
    list_display = ["product_name", "image_tag"]

    def image_tag(self, obj):
        return format_html(
            f'''<a href="{obj.recently_product.image.image.url}" target="_blank"><img src="{obj.recently_product.image.image.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')

    def product_name(self, obj):
        return format_html(f"<b>{obj.recently_product.product_name}</b>")


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ["image_tag"]

    def image_tag(self, obj):
        return format_html(f'''<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["image_tag", "product_name", "description", "price"]
    search_fields = ["product_name", "price"]

    def image_tag(self, obj):
        return format_html(f'''<a href="{obj.image.image.url}" target="_blank"><img src="{obj.image.image.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')


@admin.register(Persons)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["image_tag"]

    def image_tag(self, obj):
        return format_html(f'''<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')


@admin.register(About1)
class About1Admin(admin.ModelAdmin):
    list_display = ["image_tag", "txt", "description"]

    def image_tag(self, obj):
        return format_html(f'''<a href="{obj.image.image.url}" target="_blank"><img src="{obj.image.image.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')


@admin.register(AboutPerson)
class AboutPersonAdmin(admin.ModelAdmin):
    list_display = ["person_name", "staff", "image_tag"]

    def image_tag(self, obj):
        return format_html(f'''<a href="{obj.image.image.url}" target="_blank"><img src="{obj.image.image.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message"]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["address", "phone", "email", "image_tag"]

    def image_tag(self, obj):
        return format_html(f'''<a href="{obj.image.image.url}" target="_blank"><img src="{obj.image.image.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')
