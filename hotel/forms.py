from django import forms

class AvailableForm(forms.Form):
    ROOM_CATEGORIES =(
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE','QUEEN'),
    )
    room_categories = forms.ChoiceField(choices=ROOM_CATEGORIES)