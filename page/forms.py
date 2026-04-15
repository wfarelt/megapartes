from django import forms

from .models import Ejecutivo, Marca, Sucursal


class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['nombre', 'direccion', 'telefono', 'imagen', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'estado':
                field.widget.attrs['class'] = 'form-check-input'
            else:
                css_class = 'form-control'
                if name == 'direccion':
                    css_class += ' form-control-lg'
                field.widget.attrs['class'] = css_class


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'industria', 'imagen', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'estado':
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class EjecutivoForm(forms.ModelForm):
    class Meta:
        model = Ejecutivo
        fields = ['nombre', 'telefono', 'correo', 'imagen', 'sucursal', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'estado':
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'