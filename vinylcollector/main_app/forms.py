from django.forms import ModelForm
from .models import Purchased

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchased
        fields = ['date']