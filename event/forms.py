from django import forms
from event.models import Event,Category,Participant


# Styling form of django using tailwind css
class FormCssMixin:
    defaultCss = "border-2 rounded-md border-gray-200 p-3 focus:border-rose-400 focus:ring-rose-500"
    def applyCss(self):
        for field_name,field in self.fields.items():
            if isinstance(field.widget,forms.TextInput):
                field.widget.attrs.update({
                    'class':f'{self.defaultCss} w-full',
                    'placeholder':f'{field_name.lower().replace('_'," ")}'
                })
            elif isinstance(field.widget,forms.Textarea):
                field.widget.attrs.update({
                    'class':f'{self.defaultCss} w-full',
                    'placeholder':f'Type {field_name.lower().replace('_'," ") } in detail..',
                    'rows':2 if field_name == 'location' else 5
                })
            elif isinstance(field.widget,forms.Select):
                field.widget.attrs.update({
                    'class':f'{self.defaultCss}'
                })
            elif isinstance(field.widget,forms.DateInput):
                field.widget.attrs.update({
                    'class':f'{self.defaultCss}'
                })
            
            elif isinstance(field.widget,forms.TimeInput):
                field.widget.attrs.update({
                    'class':f'{self.defaultCss}'
                })
            elif isinstance(field.widget,forms.EmailInput):
                field.widget.attrs.update({
                    'class':f'{self.defaultCss} w-full',
                    'placeholder':f'{field_name}'
                })
       
# --------------------------CREATE FORMS ----------------------------------------------------
class Category_add(FormCssMixin,forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description']
        widgets={
            'name':forms.TextInput(),
            'description':forms.Textarea()
        }
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applyCss()


class Event_add(FormCssMixin,forms.ModelForm):

    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category']
        widgets = {
            'name':forms.TextInput(),
            'description':forms.Textarea(), 
            'date':forms.DateInput(attrs={'type':'date'}), 
            'time':forms.TimeInput(attrs={'type':'time'}), 
            'location':forms.Textarea(), 
            'category':forms.Select()
        }
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applyCss()

class Create_participant(FormCssMixin,forms.ModelForm):
    
    class Meta:
        model = Participant
        fields = ['name','email','registered_events']
        widgets = {
            'name':forms.TextInput(),
            'email':forms.EmailInput(),
            'registered_events':forms.CheckboxSelectMultiple()
        }
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applyCss()
