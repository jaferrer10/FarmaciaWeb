from django.db import models

# Create your models here.
class cliente(models.Model):
    Apellido = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=50)
    documento = models.CharField(max_length=8)
    Telefono = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=100)
    Fechanacimiento = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')
    sexos = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=sexos, default='M')

    def NombreCompleto(self):
        cadena = "{0}, {1} - ({2})"
        return cadena.format(self.Apellido, self.Nombre, self.documento)

    def __str__(self):
        return self.NombreCompleto()

class rubro(models.Model):
    codigo = models.IntegerField(null=False, blank=False)
    descripcion = models.CharField(max_length=50)

    def Rubros(self):
        NombreRubro = "{0} ({1})"
        return NombreRubro.format(self.descripcion, self.codigo)

    def __str__(self):
        return self.Rubros()


class producto(models.Model):
    codigo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    Cantidad = models.IntegerField()
    precio_Costo = models.FloatField()
    margen = models.IntegerField()
    iva = models.IntegerField()
    precio_contado = models.FloatField()
    precio_lista = models.FloatField()
    rubro = models.ForeignKey(rubro, null=False, blank=False, on_delete=models.CASCADE)
    observaciones = models.CharField(max_length=100)

class cuentacorriente(models.Model):
    cliente = models.ForeignKey(cliente, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=True)
    troquel = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    cantidad = models.FloatField()
    precio = models.FloatField()
    Importe = models.FloatField()
    observaciones = models.CharField(max_length=100)

    def __str__(self):
        return "{0},{1}".format(self.cliente, self.fecha)


class venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)

    turnos=(("M", "Mañana"), ("T", "Tarde"))
    turno = models.CharField(max_length=1, choices=turnos, default="M")

    Importe = models.FloatField()

class proveedor(models.Model):
    codigo = models.IntegerField()
    Nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=150)
    cuit = models.CharField(max_length=13)
    email = models.CharField(max_length=100, blank=True)
    observaciones = models.CharField(max_length=150)

    def __str__(self):
        return "{0}, {1} ({2})".format(self.codigo, self.Nombre, self.cuit)

class compra(models.Model):
    factura = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now=True)
    proveedor = models.ForeignKey(proveedor, null=False, blank=False, on_delete=models.CASCADE)

