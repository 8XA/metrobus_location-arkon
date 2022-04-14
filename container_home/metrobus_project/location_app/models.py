from django.db import models


class UnidadesModel(models.Model):
    """
    Basic model with the relevant fields for the query endpoints.
    The label is a unique number for each metrobus unit, then it can work as an primary key ID unit.
    """

    #Works as an ID
    label = models.IntegerField(unique=True, primary_key=True)
    
    #Position
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    #Locality name
    alcaldia = models.TextField()

    class Meta:
        #Table name
        db_table = "Unidades"

        #Order by
        ordering = ['label']

        #Names for the admin panel
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"

    def __str__(self):
        return 'Unidad {} en {}'.format(self.label, self.alcaldia)
