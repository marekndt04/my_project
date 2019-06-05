from django import forms


class PaintingCostForm(forms.Form):
    running_metre = forms.DecimalField(label='Metry bieżące malowania', min_value=0.01)
    flat_height = forms.DecimalField(label='Wysokość mieszkania', min_value=2.5)
    slot_area = forms.DecimalField(label='Powierzchnia otworów', min_value=0.1, initial=0)


class DoorWindowSizeCalc(forms.Form):
    window_height = forms.DecimalField(label='Wysokość [m]', min_value=0.1, required=False)
    window_weight = forms.DecimalField(label='Szerokość [m]', min_value=0.1, required=False)
