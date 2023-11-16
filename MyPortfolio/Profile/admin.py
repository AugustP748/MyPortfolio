from django.contrib import admin
from . models import PictureProfile, Language, Profile, Skill, Education

# Register your models here.
@admin.register(PictureProfile)
class PictureProfileAdmin(admin.ModelAdmin):
    list_display = ["visible","created","updated"]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ["language_name","created","updated"]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","updated"]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["Skill_name","visible","created","updated"]

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["institute","title","visible","created","updated"]