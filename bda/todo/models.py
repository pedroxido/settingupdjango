from django.db import models
from django.contrib.auth.models import User

class main(models.Model):
	description = models.CharField(max_length=200)
	amount = models.DecimalField(max_digits=5, decimal_places=2)
	pub_date = models.DateField()
	ready = models.BooleanField()
	id_user = models.ForeignKey(User)
	
	def __unicode__(self):
		return '%s %.2f %s %r %2f' % (self.description, self.amount, str(self.pub_date), self.ready, self.id_user)

# Create your models here.
