from django.db import models

# Create your models here.
class Topic(models.Model):
	"""Un tema que esta aprendiendo el usuario."""
	text = models.CharField(max_length=200) #----------------Creo el atributo text, que es un "CharField", que son datos compuestos por caracteres o texto. Se usa cuando se necesita crear pequeñas cantidades de texto como nombres de usuarios, titulos o nombres de ciudades. Cuando creamos uno hay que especificar cuanto espacio django va a necesitar.
	date_added = models.DateTimeField(auto_now_add=True) #---Creo el atributo de fecha, que es un DateTimeField, conjunto de datos que guarda la hora y la fecha. Le pasamos a Django auto_now_add=True, que automaticamente añade esta informacion cuando se cree una nueva entrada de los usuarios.

	def __str__(self):
		"""Devuelve un string representando el modelo."""
		return self.text

class Entry(models.Model):
	"""Something specific learned about a topic."""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Return a string representation of the model."""
		if len(self.text) > 50:
			return f"{self.text[:50]}..."
		
		else:
			return f"{self.text}"