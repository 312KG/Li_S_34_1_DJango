from django.contrib import admin
from post.models import Equipment, HashTag, Review, Category

# admin.site.register(Equipment)

@admin.register(Equipment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'rate', 'created_at']
    list_editable = ['rate']
    list_filter = ['hashtags']
    list_per_page = 8
    search_fields = ['title', 'content', 'hashtags__title']

    def has_add_permission(self, request):
        return True

    # def has_delete_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request):
    #     return False


admin.site.register(HashTag)
admin.site.register(Category)
admin.site.register(Review)
