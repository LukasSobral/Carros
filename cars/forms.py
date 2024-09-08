from django import forms
from cars.models import Car


class CarModelForm (forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
    
    #valida o campo value, se for menor que 20mil retorna erro.
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value','O valor minimo para cadastro é de R$20,000.')
        return value
    
    #valida o campo ano de fabricação caso for maior menor que 1998 retorna erro
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1998:
            self.add_error('factory_year','O carro deve ter no minimo até o ano de 1998.')
        return factory_year
    
    #valida o campo placa, se tiver mais que oito caracteres retorna erro 
    def clean_plate(self):
        plate = self.cleaned_data.get('plate')
        if len(plate) > 8:
            self.add_error('plate','ensira uma placa valida')
        return plate