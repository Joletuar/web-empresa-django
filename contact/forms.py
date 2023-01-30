# Aquí es donde vamos a definir nuestros formularios
# Funciona igual que los modelos
# Definimos una clase con todos los parametros y django se encargará implementar todo el código html respectivo

from django import forms

# Hereda de la clase Form. Similar al procedimiento de los models
class ContactForm(forms.Form):
    
    # Param label: crea una etiqueta html de tipo label
    # Param required: inidica que el campo debe ser obligatorio, es decir, no puede quedar vacío
    # Param widget: permite darle un aspecto diferente aunque siga siendo un campo de texto, tambien permite extender la configuración
    # Los atributos se declaran usando attrs y se le paso como parámetro un diccionario
    
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'Tu nombre'
        }
    ), min_length=3, max_length=100)
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder': 'example@example.com'
        }
    ), min_length=3, max_length=100)
    # Para los campos que contienen un texto largo se utiliza esto
    content = forms.CharField(label='Contenido', required=True, widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'rows': 3,
            'placeholder': "Ingrese un breve mensaje"
        }
    ), min_length=10, max_length=1000)