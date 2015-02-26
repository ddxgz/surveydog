from django.contrib import admin

from surveydog.models import Survey, SingleChoice, SingleChoiceQuestion, \
    MultiChoiceQuestion, FreeQuestion, MultiChoice


class SingleChoiceInline(admin.TabularInline):
    model = SingleChoice
    extra = 2


class MultiChoiceInline(admin.TabularInline):
    model = MultiChoice
    extra = 2


class SingleChoiceQuestionInline(admin.TabularInline):
    model = SingleChoiceQuestion
    extra = 1


class MultiChoiceQuestionInline(admin.TabularInline):
    model = MultiChoiceQuestion
    extra = 1


class FreeQuestionInline(admin.TabularInline):
    model = FreeQuestion
    extra = 1


class SurveyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['survey_head']}),
        (None, {'fields': ['survey_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [SingleChoiceQuestionInline,
               MultiChoiceQuestionInline,
               FreeQuestionInline]
    # inlines = [SingleChoiceQuestionInline,]
    list_display = ('survey_head', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['survey_head', 'survey_text']


class SingleChoiceQuestionAdmin(admin.ModelAdmin):
   # fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Belong to Survey', {'fields': ['survey']}),
        (None, {'fields': ['question_text']}),
        # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [SingleChoiceInline]
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_display = ('question_text', 'survey')
    # list_filter = ['pub_date']
    search_fields = ['question_text']


class MultiChoiceQuestionAdmin(admin.ModelAdmin):
   # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [MultiChoiceInline]
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_display = ('question_text', 'survey')
    # list_filter = ['pub_date']
    search_fields = ['question_text']


class FreeQuestionAdmin(admin.ModelAdmin):
   # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # inlines = [FreeAnswerInline]
    list_display = ('question_text', 'survey')
    # list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Survey, SurveyAdmin)
admin.site.register(SingleChoiceQuestion, SingleChoiceQuestionAdmin)
admin.site.register(MultiChoiceQuestion, MultiChoiceQuestionAdmin)
admin.site.register(FreeQuestion, FreeQuestionAdmin)
admin.site.register(SingleChoice)
admin.site.register(MultiChoice)

