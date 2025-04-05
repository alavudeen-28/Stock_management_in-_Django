from django import forms
from .models import Stock
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required')

        # Optional: Prevent duplicate category
        for instance in Stock.objects.all():
            if instance.category == category:
                raise forms.ValidationError('Category already exists')
        return category

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required')
        return item_name
class StockSearchForm(forms.ModelForm):
   export_to_CSV = forms.BooleanField(required=False)

   class Meta:
     model = Stock
     fields = ['category', 'item_name']
#    def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.layout = Layout(
#             Row(
#                 Column('category', css_class='form-group col-md-6 mb-0'),
#                 Column('item_name', css_class='form-group col-md-6 mb-0'),
#                 css_class='form-row'
#             ),
#             Submit('submit', 'Search')
#         )
#    def __init__(self, *args, **kwargs):
#         super(StockSearchForm, self).__init__(*args, **kwargs)
#         self.fields['category'].required = False
#         self.fields['item_name'].required = False
class StockUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category', 'item_name', 'quantity']
class IssueForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['issue_quantity', 'issue_to']


class ReceiveForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['receive_quantity']