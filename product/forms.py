from django import forms  
from product.models import Deleted,Product


class ProductForm(forms.ModelForm):  
    class Meta:  
        model =  Product
        fields = "__all__"  

class  DeletedForm(forms.ModelForm):
    class Meta:
        model = Deleted
        fields = "__all__"