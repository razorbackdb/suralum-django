# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccProducto(models.Model):
    id_producto = models.OneToOneField('Productos', models.DO_NOTHING, db_column='id_producto', primary_key=True)
    id_accesorio = models.ForeignKey('Accesorios', models.DO_NOTHING, db_column='id_accesorio')
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'acc_producto'
        unique_together = (('id_producto', 'id_accesorio'),)


class AccesorioProveedores(models.Model):
    id_proveedor = models.OneToOneField('Proveedores', models.DO_NOTHING, db_column='id_proveedor', primary_key=True)
    id_accesorio = models.ForeignKey('Accesorios', models.DO_NOTHING, db_column='id_accesorio')
    costo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accesorio_proveedores'
        unique_together = (('id_proveedor', 'id_accesorio'),)


class Accesorios(models.Model):
    id_accesorio = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    id_tipo_acc = models.ForeignKey('TipoAccesorio', models.DO_NOTHING, db_column='id_tipo_acc', blank=True, null=True)
    precio = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    costo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    stock_minimo = models.FloatField(blank=True, null=True)
    ctaid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accesorios'


class AccesoriosAct(models.Model):
    id_accesorio = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    fecha_act = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accesorios_act'


class AccsAsocMerma(models.Model):
    id_merma = models.OneToOneField('Merma', models.DO_NOTHING, db_column='id_merma', primary_key=True)
    id_accesorio = models.ForeignKey(Accesorios, models.DO_NOTHING, db_column='id_accesorio')
    cantidad = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accs_asoc_merma'
        unique_together = (('id_merma', 'id_accesorio'),)


class AccsAsocPedido(models.Model):
    id_accesorio = models.OneToOneField(Accesorios, models.DO_NOTHING, db_column='id_accesorio', primary_key=True)
    id_pedido = models.ForeignKey('Pedidos', models.DO_NOTHING, db_column='id_pedido')
    cantidad = models.FloatField(blank=True, null=True)
    stock_descontado = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accs_asoc_pedido'
        unique_together = (('id_accesorio', 'id_pedido'),)


class Adjuntosdte(models.Model):
    adjcorrelativo = models.FloatField(primary_key=True)
    corcorrelativo = models.ForeignKey('Correosdte', models.DO_NOTHING, db_column='corcorrelativo')
    adjnombre = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'adjuntosdte'


class Bancos(models.Model):
    banid = models.IntegerField(primary_key=True)
    bannombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bancos'


class Cafs(models.Model):
    cafcorrelativo = models.FloatField(primary_key=True)
    cafid = models.CharField(max_length=100, blank=True, null=True)
    caffoliodesde = models.FloatField(blank=True, null=True)
    caffoliohasta = models.FloatField(blank=True, null=True)
    caffecha = models.DateField(blank=True, null=True)
    socrut = models.CharField(max_length=10, blank=True, null=True)
    sucid = models.IntegerField(blank=True, null=True)
    caffoldisponibles = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cafs'


class Casillasdte(models.Model):
    casid = models.IntegerField(primary_key=True)
    socrut = models.CharField(max_length=9, blank=True, null=True)
    casemail = models.CharField(max_length=100, blank=True, null=True)
    casnombre = models.CharField(max_length=250, blank=True, null=True)
    partipoemailserver = models.BooleanField(blank=True, null=True)
    casserverin = models.CharField(max_length=100, blank=True, null=True)
    casportin = models.CharField(max_length=10, blank=True, null=True)
    casusasslin = models.CharField(max_length=1, blank=True, null=True)
    casusuario = models.CharField(max_length=100, blank=True, null=True)
    casclave = models.CharField(max_length=100, blank=True, null=True)
    casactiva = models.CharField(max_length=1, blank=True, null=True)
    casfecingreso = models.DateField(blank=True, null=True)
    casfecactualiza = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'casillasdte'


class Clicuenta(models.Model):
    cctacorrelativo = models.FloatField(primary_key=True)
    cctacorrelativoorig = models.FloatField(blank=True, null=True)
    opeid = models.IntegerField(blank=True, null=True)
    clirut = models.CharField(max_length=9, blank=True, null=True)
    cctafecha = models.DateField(blank=True, null=True)
    cctamtodebe = models.FloatField(blank=True, null=True)
    cctamtohaber = models.FloatField(blank=True, null=True)
    cctacorrelativocalce = models.FloatField(blank=True, null=True)
    cctafechacalce = models.DateField(blank=True, null=True)
    cliuniid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clicuenta'


class Clientes(models.Model):
    rut_cliente = models.CharField(primary_key=True, max_length=12)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=25, blank=True, null=True)
    apellido_materno = models.CharField(max_length=25, blank=True, null=True)
    giro = models.CharField(max_length=50, blank=True, null=True)
    descuento1 = models.FloatField(blank=True, null=True)
    descripcion_descuento1 = models.CharField(max_length=40, blank=True, null=True)
    descuento2 = models.FloatField(blank=True, null=True)
    descripcion_descuento2 = models.CharField(max_length=40, blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    cuenta_banco = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    nombre_empresa = models.CharField(max_length=50, blank=True, null=True)
    vigente = models.BooleanField(blank=True, null=True)
    usu_ingresa = models.IntegerField(blank=True, null=True)
    fecha_ingresa = models.DateField(blank=True, null=True)
    usu_actualiza = models.IntegerField(blank=True, null=True)
    fecha_actualiza = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class Cliunidades(models.Model):
    clirut = models.CharField(primary_key=True, max_length=10)
    cliuniid = models.IntegerField()
    #id_comuna = models.FloatField(blank=True, null=True)
    #direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    cliemail = models.CharField(max_length=100, blank=True, null=True)
    cliemailfe = models.CharField(max_length=100, blank=True, null=True)
    vigente = models.BooleanField(blank=True, null=True)
    usu_ingresa = models.IntegerField(blank=True, null=True)
    fecha_ingresa = models.DateField(blank=True, null=True)
    usu_actualiza = models.IntegerField(blank=True, null=True)
    fecha_actualiza = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliunidades'
        unique_together = (('clirut', 'cliuniid'),)


class CompraProductos(models.Model):
    comcorrelativo = models.OneToOneField('Compras', models.DO_NOTHING, db_column='comcorrelativo', primary_key=True)
    pronombre = models.CharField(max_length=50, blank=True, null=True)
    procantidad = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    proprecio = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    id_producto_asoc = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto_asoc', blank=True, null=True)
    proexento = models.CharField(max_length=1, blank=True, null=True)
    nrolinea = models.IntegerField()
    ctaid = models.IntegerField(blank=True, null=True)
    mtodscto = models.BigIntegerField(blank=True, null=True)
    mtototallinea = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compra_productos'
        unique_together = (('comcorrelativo', 'nrolinea'),)


class Compras(models.Model):
    comcorrelativo = models.FloatField(primary_key=True)
    opeid = models.IntegerField(blank=True, null=True)
    prvrut = models.CharField(max_length=12, blank=True, null=True)
    sucid = models.IntegerField(blank=True, null=True)
    comfolio = models.FloatField(blank=True, null=True)
    comfecingreso = models.DateField(blank=True, null=True)
    comfecha = models.DateField(blank=True, null=True)
    comfechavenc = models.DateField(blank=True, null=True)
    parpagtipo = models.BooleanField(blank=True, null=True)
    paropeestado = models.BooleanField(blank=True, null=True)
    commtosubtotal = models.FloatField(blank=True, null=True)
    commtoneto = models.FloatField(blank=True, null=True)
    commtoexento = models.FloatField(blank=True, null=True)
    commtoiva = models.FloatField(blank=True, null=True)
    commtototal = models.FloatField(blank=True, null=True)
    usuingresa = models.FloatField(blank=True, null=True)
    usuactualiza = models.FloatField(blank=True, null=True)
    comtasaiva = models.FloatField(blank=True, null=True)
    indmtobruto = models.CharField(max_length=1, blank=True, null=True)
    centralizado = models.CharField(max_length=1, blank=True, null=True)
    periodocentraliza = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras'


class ComprasDsctoRec(models.Model):
    comcorrelativo = models.OneToOneField(Compras, models.DO_NOTHING, db_column='comcorrelativo', primary_key=True)
    nrolinea = models.IntegerField()
    tpomov = models.CharField(max_length=1, blank=True, null=True)
    glosadr = models.CharField(max_length=45, blank=True, null=True)
    tpovalor = models.CharField(max_length=1, blank=True, null=True)
    valordr = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    indexedr = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras_dscto_rec'
        unique_together = (('comcorrelativo', 'nrolinea'),)


class ComprasImpuestos(models.Model):
    comcorrelativo = models.OneToOneField(Compras, models.DO_NOTHING, db_column='comcorrelativo', primary_key=True)
    comcodimpto = models.IntegerField()
    comtasaimpto = models.FloatField()
    commtoimpto = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras_impuestos'
        unique_together = (('comcorrelativo', 'comcodimpto', 'comtasaimpto'),)


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nombre_comuna = models.CharField(max_length=100, blank=True, null=True)
    id_provincia = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='id_provincia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna'


class ComunaClientes(models.Model):
    #id_comuna = models.OneToOneField(Comuna, models.DO_NOTHING, db_column='id_comuna', primary_key=True)
    rut_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='rut_cliente')
    #direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna_clientes'
        #unique_together = (('id_comuna', 'rut_cliente', 'direccion'),)


class Config(models.Model):
    parnombre = models.CharField(primary_key=True, max_length=50)
    parvalor = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config'


class Correosdte(models.Model):
    corcorrelativo = models.IntegerField(primary_key=True)
    casid = models.ForeignKey(Casillasdte, models.DO_NOTHING, db_column='casid', blank=True, null=True)
    coridserver = models.CharField(max_length=100, blank=True, null=True)
    cordesde = models.CharField(max_length=500, blank=True, null=True)
    corfecha = models.DateField(blank=True, null=True)
    cortieneadjuntos = models.CharField(max_length=1, blank=True, null=True)
    cormensaje = models.CharField(max_length=4000, blank=True, null=True)
    corfecingreso = models.DateField(blank=True, null=True)
    corasunto = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'correosdte'


class Cuentas(models.Model):
    ctaid = models.IntegerField(primary_key=True)
    ctanombre = models.CharField(max_length=60, blank=True, null=True)
    ctadescripcion = models.CharField(max_length=100, blank=True, null=True)
    ctavigencia = models.CharField(max_length=1, blank=True, null=True)
    partipocuenta = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuentas'


class EnvioRcof(models.Model):
    envio_rcof_id = models.IntegerField(primary_key=True)
    fecha_rcof = models.DateField()
    estado = models.BooleanField()
    socrut = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'envio_rcof'


class EnvioRcofSec(models.Model):
    envio_rcof_sec_id = models.IntegerField(primary_key=True)
    fk_envio_rcof = models.ForeignKey(EnvioRcof, models.DO_NOTHING)
    fecha_envio_sii = models.DateField()
    secuencia = models.IntegerField()
    trackid = models.CharField(max_length=20)
    envio_rcof_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'envio_rcof_sec'


class Enviosdte(models.Model):
    envcorrelativo = models.FloatField(primary_key=True)
    socid = models.FloatField(blank=True, null=True)
    sucid = models.FloatField(blank=True, null=True)
    opeid = models.FloatField(blank=True, null=True)
    envid = models.CharField(max_length=80, blank=True, null=True)
    envfecha = models.DateField(blank=True, null=True)
    envtrackid = models.CharField(max_length=20, blank=True, null=True)
    parenvestado = models.BooleanField(blank=True, null=True)
    envusuid = models.FloatField(blank=True, null=True)
    fecactualiza = models.DateField(blank=True, null=True)
    usuactualiza = models.FloatField(blank=True, null=True)
    envestadodetalle = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enviosdte'


class EnviosdteVentas(models.Model):
    envcorrelativo = models.OneToOneField(Enviosdte, models.DO_NOTHING, db_column='envcorrelativo', primary_key=True)
    vencorrelativo = models.ForeignKey('Ventas', models.DO_NOTHING, db_column='vencorrelativo')
    pardteestado = models.FloatField(blank=True, null=True)
    resestado = models.CharField(max_length=100, blank=True, null=True)
    resdetalle = models.CharField(max_length=2000, blank=True, null=True)
    fecactualiza = models.DateField(blank=True, null=True)
    usuactualiza = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enviosdte_ventas'
        unique_together = (('envcorrelativo', 'vencorrelativo'),)


class Enviosiecv(models.Model):
    envinfcorrelativo = models.FloatField(primary_key=True)
    socrut = models.CharField(max_length=12, blank=True, null=True)
    envinfperiodo = models.CharField(max_length=7, blank=True, null=True)
    envinffecenvio = models.DateField(blank=True, null=True)
    parenvinftipolibro = models.BooleanField(blank=True, null=True)
    parenvinftipoenvio = models.BooleanField(blank=True, null=True)
    parenvinftipooperacion = models.BooleanField(blank=True, null=True)
    envinffolionotif = models.FloatField(blank=True, null=True)
    parenvinfestado = models.BooleanField(blank=True, null=True)
    envinfestadodetalle = models.CharField(max_length=4000, blank=True, null=True)
    envinfnrosegmento = models.IntegerField(blank=True, null=True)
    envinftrackid = models.CharField(max_length=20, blank=True, null=True)
    usuenvia = models.FloatField(blank=True, null=True)
    envinfid = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enviosiecv'


class EnviosiecvCompras(models.Model):
    envinfcorrelativo = models.OneToOneField(Enviosiecv, models.DO_NOTHING, db_column='envinfcorrelativo', primary_key=True)
    comcorrelativo = models.FloatField()

    class Meta:
        managed = False
        db_table = 'enviosiecv_compras'
        unique_together = (('envinfcorrelativo', 'comcorrelativo'),)


class EnviosiecvComprasivanorec(models.Model):
    envinfcorrelativo = models.OneToOneField(Enviosiecv, models.DO_NOTHING, db_column='envinfcorrelativo', primary_key=True)
    comcorrelativo = models.FloatField()
    comcodivanorec = models.BooleanField()
    commtoivanorec = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enviosiecv_comprasivanorec'
        unique_together = (('envinfcorrelativo', 'comcorrelativo', 'comcodivanorec'),)


class EnviosiecvImpuestos(models.Model):
    envinfcorrelativo = models.ForeignKey(Enviosiecv, models.DO_NOTHING, db_column='envinfcorrelativo', blank=True, null=True)
    opeidsii = models.IntegerField(blank=True, null=True)
    envinfcodimpto = models.IntegerField(blank=True, null=True)
    envinfmtoimpto = models.FloatField(blank=True, null=True)
    envinftasaimpto = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enviosiecv_impuestos'


class EnviosiecvTotales(models.Model):
    envinfcorrelativo = models.OneToOneField(Enviosiecv, models.DO_NOTHING, db_column='envinfcorrelativo', primary_key=True)
    opeidsii = models.IntegerField()
    totmtoneto = models.FloatField(blank=True, null=True)
    totmtoexe = models.FloatField(blank=True, null=True)
    totmtoiva = models.FloatField(blank=True, null=True)
    totmtototal = models.FloatField(blank=True, null=True)
    totdoc = models.IntegerField(blank=True, null=True)
    totanulado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enviosiecv_totales'
        unique_together = (('envinfcorrelativo', 'opeidsii'),)


class EnviosiecvVentas(models.Model):
    envinfcorrelativo = models.OneToOneField(Enviosiecv, models.DO_NOTHING, db_column='envinfcorrelativo', primary_key=True)
    vencorrelativo = models.FloatField()

    class Meta:
        managed = False
        db_table = 'enviosiecv_ventas'
        unique_together = (('envinfcorrelativo', 'vencorrelativo'),)


class Enviosrecibidosdte(models.Model):
    envreccorrelativo = models.IntegerField(primary_key=True)
    socrut = models.CharField(max_length=9, blank=True, null=True)
    envrecid = models.CharField(max_length=80, blank=True, null=True)
    prvrut = models.CharField(max_length=9, blank=True, null=True)
    envrecfecha = models.DateField(blank=True, null=True)
    parenvrecestado = models.BooleanField(blank=True, null=True)
    envrecusuid = models.IntegerField(blank=True, null=True)
    envrecarchivo = models.CharField(max_length=150, blank=True, null=True)
    adjcorrelativo = models.ForeignKey(Adjuntosdte, models.DO_NOTHING, db_column='adjcorrelativo', blank=True, null=True)
    fecactualiza = models.DateField(blank=True, null=True)
    usuactualiza = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enviosrecibidosdte'


class EnviosrecibidosdteDetalle(models.Model):
    envreccorrelativo = models.IntegerField()
    envrectipodte = models.IntegerField()
    envrecfoliodte = models.BigIntegerField()
    envrecfechadte = models.DateField(blank=True, null=True)
    envrecrutreceptordte = models.CharField(max_length=9, blank=True, null=True)
    envrecmontototaldte = models.IntegerField(blank=True, null=True)
    pardteestadorecepcion = models.BooleanField(blank=True, null=True)
    envrecobservaciondte = models.CharField(max_length=255, blank=True, null=True)
    fecactualiza = models.DateField(blank=True, null=True)
    sucid = models.IntegerField(blank=True, null=True)
    pardteestadoacepta = models.BooleanField(blank=True, null=True)
    envrecglosaacepta = models.CharField(max_length=255, blank=True, null=True)
    envrecdetcorrelativo = models.FloatField(primary_key=True)
    envreciddte = models.CharField(max_length=80, blank=True, null=True)
    envrecrutemisordte = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'enviosrecibidosdte_detalle'
        unique_together = (('envreccorrelativo', 'envrectipodte', 'envrecfoliodte', 'envrecrutemisordte'),)


class Familia(models.Model):
    id_familia = models.IntegerField(primary_key=True)
    descripcion_familia = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'familia'


class FasesAccesorio(models.Model):
    id_fase = models.OneToOneField('FasesProduccion', models.DO_NOTHING, db_column='id_fase', primary_key=True)
    id_accesorio = models.ForeignKey(Accesorios, models.DO_NOTHING, db_column='id_accesorio')
    costo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fases_accesorio'
        unique_together = (('id_fase', 'id_accesorio'),)


class FasesProduccion(models.Model):
    id_fase = models.FloatField(primary_key=True)
    descripcion_fase = models.CharField(max_length=25, blank=True, null=True)
    porcentaje = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fases_produccion'


class FasesProducto(models.Model):
    id_fase = models.OneToOneField(FasesProduccion, models.DO_NOTHING, db_column='id_fase', primary_key=True)
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')
    costo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fases_producto'
        unique_together = (('id_fase', 'id_producto'),)


class FasesTrabajo(models.Model):
    id_trabajador = models.OneToOneField('Trabajadores', models.DO_NOTHING, db_column='id_trabajador', primary_key=True)
    id_orden_trabajo = models.ForeignKey('OrdenTrabajo', models.DO_NOTHING, db_column='id_orden_trabajo')
    id_fase = models.ForeignKey(FasesProduccion, models.DO_NOTHING, db_column='id_fase')

    class Meta:
        managed = False
        db_table = 'fases_trabajo'
        unique_together = (('id_trabajador', 'id_orden_trabajo', 'id_fase'),)


class Folios(models.Model):
    folcorrelativo = models.FloatField(primary_key=True)
    socrut = models.CharField(max_length=10, blank=True, null=True)
    sucid = models.IntegerField(blank=True, null=True)
    opeid = models.FloatField(blank=True, null=True)
    folnumero = models.FloatField(blank=True, null=True)
    vencorrelativo = models.FloatField(blank=True, null=True)
    parfolestado = models.BooleanField(blank=True, null=True)
    cafcorrelativo = models.ForeignKey(Cafs, models.DO_NOTHING, db_column='cafcorrelativo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'folios'


class FunRecursos(models.Model):
    funid = models.FloatField(blank=True, null=True)
    recnombre = models.CharField(max_length=100, blank=True, null=True)
    treid = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fun_recursos'


class Funciones(models.Model):
    funid = models.FloatField(blank=True, null=True)
    funnombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funciones'


class GuiaDespacho(models.Model):
    id_guia_despacho = models.FloatField(primary_key=True)
    nro_guia_despacho = models.FloatField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    rut_cliente = models.CharField(max_length=9, blank=True, null=True)
    #direccion = models.CharField(max_length=100, blank=True, null=True)
    #id_comuna = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    localidad = models.CharField(max_length=20, blank=True, null=True)
    fecha_actualizacion = models.DateField(blank=True, null=True)
    observaciones = models.CharField(max_length=100, blank=True, null=True)
    id_empresa = models.BooleanField(blank=True, null=True)
    fecingresa = models.DateField(blank=True, null=True)
    usuingresa = models.IntegerField(blank=True, null=True)
    usuactualiza = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_despacho'


class GuiaDespachoVenta(models.Model):
    id_guia_despacho = models.OneToOneField(GuiaDespacho, models.DO_NOTHING, db_column='id_guia_despacho', primary_key=True)
    id_venta = models.ForeignKey('Ventas', models.DO_NOTHING, db_column='id_venta')

    class Meta:
        managed = False
        db_table = 'guia_despacho_venta'
        unique_together = (('id_guia_despacho', 'id_venta'),)


class GuiaProductos(models.Model):
    id_guia_despacho = models.OneToOneField(GuiaDespacho, models.DO_NOTHING, db_column='id_guia_despacho', primary_key=True)
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')
    id_accesorio = models.ForeignKey(Accesorios, models.DO_NOTHING, db_column='id_accesorio')
    cantidad = models.FloatField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_productos'
        unique_together = (('id_guia_despacho', 'id_producto', 'id_accesorio'),)


class ListaPrecio(models.Model):
    lista_precio_id = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'lista_precio'


class ListaPrecioDet(models.Model):
    lista_precio_det_id = models.IntegerField(primary_key=True)
    fk_lista_precio = models.ForeignKey(ListaPrecio, models.DO_NOTHING)
    fk_id_producto_acc = models.IntegerField()
    par_tipo_producto = models.BooleanField()
    precio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lista_precio_det'
        unique_together = (('fk_lista_precio', 'fk_id_producto_acc', 'par_tipo_producto'),)


class MatPrimaAccesorio(models.Model):
    id_materia_prima = models.OneToOneField('MateriaPrima', models.DO_NOTHING, db_column='id_materia_prima', primary_key=True)
    id_accesorio = models.ForeignKey(Accesorios, models.DO_NOTHING, db_column='id_accesorio')
    relacion = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mat_prima_accesorio'
        unique_together = (('id_materia_prima', 'id_accesorio'),)


class MatPrimaProducto(models.Model):
    id_materia_prima = models.OneToOneField('MateriaPrima', models.DO_NOTHING, db_column='id_materia_prima', primary_key=True)
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')
    relacion = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'mat_prima_producto'
        unique_together = (('id_materia_prima', 'id_producto'),)


class MateriaPrima(models.Model):
    id_materia_prima = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    dimensiones = models.CharField(max_length=15, blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    stock_minimo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materia_prima'


class MateriaPrimaProveedores(models.Model):
    id_materia_prima = models.OneToOneField(MateriaPrima, models.DO_NOTHING, db_column='id_materia_prima', primary_key=True)
    id_proveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='id_proveedor')
    costo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materia_prima_proveedores'
        unique_together = (('id_materia_prima', 'id_proveedor'),)


class Mediospago(models.Model):
    mpaid = models.FloatField(primary_key=True)
    mpadescripcion = models.CharField(max_length=30, blank=True, null=True)
    mpasii = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mediospago'


class Merma(models.Model):
    id_merma = models.FloatField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    observaciones = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merma'


class MermaAccesorios(models.Model):
    id_merma = models.OneToOneField(Merma, models.DO_NOTHING, db_column='id_merma', primary_key=True)
    id_accesorio = models.ForeignKey(Accesorios, models.DO_NOTHING, db_column='id_accesorio')
    cantidad = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merma_accesorios'
        unique_together = (('id_merma', 'id_accesorio'),)


class MermaProductos(models.Model):
    id_merma = models.OneToOneField(Merma, models.DO_NOTHING, db_column='id_merma', primary_key=True)
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merma_productos'
        unique_together = (('id_merma', 'id_producto'),)


class Movcontdet(models.Model):
    movcontdetid = models.BigIntegerField(primary_key=True)
    socid = models.BooleanField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    tpocomprob = models.IntegerField(blank=True, null=True)
    movcontencid = models.BigIntegerField(blank=True, null=True)
    numlinea = models.IntegerField(blank=True, null=True)
    movconestado = models.BooleanField(blank=True, null=True)
    tpodoccontable = models.IntegerField(blank=True, null=True)
    debe = models.BigIntegerField(blank=True, null=True)
    haber = models.BigIntegerField(blank=True, null=True)
    ctaid = models.IntegerField(blank=True, null=True)
    glosa = models.CharField(max_length=100, blank=True, null=True)
    tipodocumento = models.CharField(max_length=50, blank=True, null=True)
    nrodocumento = models.BigIntegerField(blank=True, null=True)
    fechavenc = models.DateField(blank=True, null=True)
    prvrut = models.CharField(max_length=12, blank=True, null=True)
    clirut = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movcontdet'


class Movcontenc(models.Model):
    movcontencid = models.BigIntegerField(primary_key=True)
    socid = models.BooleanField()
    tpocomprob = models.BooleanField(blank=True, null=True)
    movcontmtototal = models.BigIntegerField(blank=True, null=True)
    movcontestado = models.BooleanField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    fechamov = models.DateField(blank=True, null=True)
    foliocomp = models.IntegerField(blank=True, null=True)
    periodo = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movcontenc'


class OrdenCompra(models.Model):
    id_orden = models.IntegerField(primary_key=True)
    id_proveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='id_proveedor', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    observacion = models.CharField(max_length=300, blank=True, null=True)
    estado = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_compra'


class OrdenCompraAcc(models.Model):
    id_orden = models.OneToOneField(OrdenCompra, models.DO_NOTHING, db_column='id_orden', primary_key=True)
    id_accesorio = models.ForeignKey(Accesorios, models.DO_NOTHING, db_column='id_accesorio')
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orden_compra_acc'
        unique_together = (('id_orden', 'id_accesorio'),)


class OrdenCompraMp(models.Model):
    id_orden = models.OneToOneField(OrdenCompra, models.DO_NOTHING, db_column='id_orden', primary_key=True)
    id_materia_prima = models.ForeignKey(MateriaPrima, models.DO_NOTHING, db_column='id_materia_prima')
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orden_compra_mp'
        unique_together = (('id_orden', 'id_materia_prima'),)


class OrdenCompraPedido(models.Model):
    id_pedido = models.OneToOneField('Pedidos', models.DO_NOTHING, db_column='id_pedido', primary_key=True)
    id_orden_compra = models.ForeignKey(OrdenCompra, models.DO_NOTHING, db_column='id_orden_compra')

    class Meta:
        managed = False
        db_table = 'orden_compra_pedido'
        unique_together = (('id_pedido', 'id_orden_compra'),)


class OrdenTrabajo(models.Model):
    id_orden_trabajo = models.FloatField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    fecha_ultima_modificacion = models.DateField(blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    fecha_anulacion = models.DateField(blank=True, null=True)
    usu_ingresa = models.FloatField(blank=True, null=True)
    usu_anulacion = models.FloatField(blank=True, null=True)
    tipo_orden = models.BooleanField(blank=True, null=True)
    forma_pago = models.BooleanField(blank=True, null=True)
    monto_pago = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_trabajo'


class OtAccesorios(models.Model):
    id_orden_trabajo = models.OneToOneField(OrdenTrabajo, models.DO_NOTHING, db_column='id_orden_trabajo', primary_key=True)
    id_accesorio = models.ForeignKey(Accesorios, models.DO_NOTHING, db_column='id_accesorio')
    cantidad = models.IntegerField()
    costo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ot_accesorios'
        unique_together = (('id_orden_trabajo', 'id_accesorio'),)


class OtProd(models.Model):
    id_orden_trabajo = models.OneToOneField(OrdenTrabajo, models.DO_NOTHING, db_column='id_orden_trabajo', primary_key=True)
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.IntegerField()
    costo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ot_prod'
        unique_together = (('id_orden_trabajo', 'id_producto'),)


class Parametros(models.Model):
    parid = models.CharField(primary_key=True, max_length=50)
    parsubid = models.FloatField()
    pardescripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametros'
        unique_together = (('parid', 'parsubid'),)


class PedidoProductos(models.Model):
    id_pedido = models.OneToOneField('Pedidos', models.DO_NOTHING, db_column='id_pedido', primary_key=True)
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')
    id_accesorio = models.ForeignKey(Accesorios, models.DO_NOTHING, db_column='id_accesorio')
    cantidad = models.FloatField(blank=True, null=True)
    stock_descontado = models.FloatField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    orden = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido_productos'
        unique_together = (('id_pedido', 'id_accesorio', 'id_producto'),)


class Pedidos(models.Model):
    id_pedido = models.FloatField(primary_key=True)
    rut_cliente = models.ForeignKey(ComunaClientes, models.DO_NOTHING, db_column='rut_cliente', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    nro_factura_asoc = models.FloatField(blank=True, null=True)
    #id_orden_trabajo_1 = models.ForeignKey(OrdenTrabajo, models.DO_NOTHING, db_column='id_orden_trabajo_1', blank=True, null=True)
    #id_orden_trabajo_2 = models.ForeignKey(OrdenTrabajo, models.DO_NOTHING, db_column='id_orden_trabajo_2', blank=True, null=True)
    id_familia = models.ForeignKey(Familia, models.DO_NOTHING, db_column='id_familia', blank=True, null=True)
    #id_comuna = models.ForeignKey(ComunaClientes, models.DO_NOTHING, db_column='id_comuna', blank=True, null=True)
    #direccion = models.ForeignKey(ComunaClientes, models.DO_NOTHING, db_column='direccion', blank=True, null=True)
    descuento1 = models.FloatField(blank=True, null=True)
    descripcion_descuento1 = models.CharField(max_length=40, blank=True, null=True)
    descuento2 = models.FloatField(blank=True, null=True)
    descripcion_descuento2 = models.CharField(max_length=40, blank=True, null=True)
    recuperacion_flete = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    fecingresa = models.DateField(blank=True, null=True)
    fecactualiza = models.DateField(blank=True, null=True)
    usuingresa = models.FloatField(blank=True, null=True)
    usuactualiza = models.FloatField(blank=True, null=True)
    cliuniid = models.FloatField(blank=True, null=True)
    sucid = models.FloatField(blank=True, null=True)
    observacion = models.CharField(max_length=350, blank=True, null=True)
    envemailinterno = models.BooleanField(blank=True, null=True)
    envemailcliente = models.BooleanField(blank=True, null=True)
    usurevisa = models.FloatField(blank=True, null=True)
    id_vendedor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos'


class Productos(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    precio = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    id_familia = models.ForeignKey(Familia, models.DO_NOTHING, db_column='id_familia', blank=True, null=True)
    costo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    id_producto_mixto = models.FloatField(blank=True, null=True)
    stock_minimo = models.FloatField(blank=True, null=True)
    orden = models.FloatField(blank=True, null=True)
    ctaid = models.IntegerField(blank=True, null=True)
    vigente = models.BooleanField(blank=True, null=True)
    usu_ingresa = models.IntegerField(blank=True, null=True)
    fecha_ingresa = models.DateField(blank=True, null=True)
    usu_actualiza = models.IntegerField(blank=True, null=True)
    fecha_actualiza = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'


class Productos20130211(models.Model):
    id_producto = models.IntegerField()
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    precio = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    id_familia = models.IntegerField(blank=True, null=True)
    costo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    id_producto_mixto = models.FloatField(blank=True, null=True)
    stock_minimo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos_20130211'


class Productos20130512(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    precio = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    id_familia = models.ForeignKey(Familia, models.DO_NOTHING, db_column='id_familia', blank=True, null=True)
    costo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    id_producto_mixto = models.FloatField(blank=True, null=True)
    stock_minimo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos_20130512'


class Productos20131006(models.Model):
    id_producto = models.IntegerField()
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    precio = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    id_familia = models.IntegerField(blank=True, null=True)
    costo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    id_producto_mixto = models.FloatField(blank=True, null=True)
    stock_minimo = models.FloatField(blank=True, null=True)
    orden = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos_20131006'


class ProductosAct(models.Model):
    id_producto = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    fecha_act = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos_act'


class ProductosError20130218(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    precio = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    id_familia = models.ForeignKey(Familia, models.DO_NOTHING, db_column='id_familia', blank=True, null=True)
    costo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    id_producto_mixto = models.ForeignKey('self', models.DO_NOTHING, db_column='id_producto_mixto', blank=True, null=True)
    stock_minimo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos_error_20130218'


class ProductosMixtos(models.Model):
    #id_producto1 = models.OneToOneField(Productos, models.DO_NOTHING, db_column='id_producto1', primary_key=True)
    #id_producto2 = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto2')
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    stock = models.FloatField(blank=True, null=True)
    codigo_mixto = models.CharField(max_length=10, blank=True, null=True)
    orden = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos_mixtos'
        #unique_together = (('id_producto1', 'id_producto2'),)


class Proveedores(models.Model):
    id_proveedor = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    #id_comuna = models.FloatField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=25, blank=True, null=True)
    apellido_materno = models.CharField(max_length=25, blank=True, null=True)
    #direccion = models.CharField(max_length=100, blank=True, null=True)
    nombre_empresa = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    rut = models.CharField(unique=True, max_length=9, blank=True, null=True)
    observaciones = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedores'


class Provincia(models.Model):
    id_provincia = models.IntegerField(primary_key=True)
    nombre_provincia = models.CharField(max_length=100, blank=True, null=True)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincia'


class Recaudacion(models.Model):
    reccorrelativo = models.FloatField(primary_key=True)
    opeid = models.IntegerField(blank=True, null=True)
    clirut = models.CharField(max_length=10, blank=True, null=True)
    cliuniid = models.FloatField(blank=True, null=True)
    recfolio = models.FloatField(blank=True, null=True)
    recdocfecingreso = models.DateField(blank=True, null=True)
    recfecha = models.DateField(blank=True, null=True)
    parrecestado = models.BooleanField(blank=True, null=True)
    recmtototal = models.FloatField(blank=True, null=True)
    usuingresa = models.FloatField(blank=True, null=True)
    usuactualiza = models.FloatField(blank=True, null=True)
    reccorrelativorev = models.FloatField(blank=True, null=True)
    recfecharev = models.DateField(blank=True, null=True)
    recabonos = models.FloatField(blank=True, null=True)
    parrectipo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recaudacion'


class Recdetalle(models.Model):
    reccorrelativo = models.ForeignKey(Recaudacion, models.DO_NOTHING, db_column='reccorrelativo', blank=True, null=True)
    reclinea = models.IntegerField(blank=True, null=True)
    banid = models.IntegerField(blank=True, null=True)
    clirut = models.CharField(max_length=10, blank=True, null=True)
    mpaid = models.IntegerField(blank=True, null=True)
    recmonto = models.FloatField(blank=True, null=True)
    reccuenta = models.CharField(max_length=50, blank=True, null=True)
    recdocnum = models.CharField(max_length=20, blank=True, null=True)
    recdoctitular = models.CharField(max_length=100, blank=True, null=True)
    recdocplaza = models.FloatField(blank=True, null=True)
    recdocfecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recdetalle'


class Recursos(models.Model):
    recnombre = models.CharField(max_length=100, blank=True, null=True)
    treid = models.IntegerField(blank=True, null=True)
    recdescripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recursos'


class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nombre_region = models.CharField(max_length=100, blank=True, null=True)
    id_zona = models.ForeignKey('Zona', models.DO_NOTHING, db_column='id_zona', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'


class Respuestasdte(models.Model):
    rescorrelativo = models.IntegerField(primary_key=True)
    socrut = models.CharField(max_length=9, blank=True, null=True)
    prvrut = models.CharField(max_length=9, blank=True, null=True)
    resfecha = models.DateField(blank=True, null=True)
    pardterestipo = models.BooleanField(blank=True, null=True)
    envreccorrelativo = models.IntegerField(blank=True, null=True)
    rescorrelativoacuse = models.IntegerField(blank=True, null=True)
    resarchivo = models.CharField(max_length=150, blank=True, null=True)
    resenviada = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'respuestasdte'


class RespuestasdteDetalle(models.Model):
    rescorrelativo = models.IntegerField(primary_key=True)
    restipodte = models.BooleanField()
    resfoliodte = models.BigIntegerField()
    resrutemisordte = models.CharField(max_length=9)
    resrutreceptordte = models.CharField(max_length=9, blank=True, null=True)
    resmontototaldte = models.IntegerField(blank=True, null=True)
    pardteestadoacepta = models.BooleanField(blank=True, null=True)
    resobservaciondte = models.CharField(max_length=255, blank=True, null=True)
    fecactualiza = models.DateField(blank=True, null=True)
    resfechadte = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'respuestasdte_detalle'
        unique_together = (('rescorrelativo', 'restipodte', 'resfoliodte', 'resrutemisordte'),)


class RespuestasrecdteAcuseventas(models.Model):
    resreccorrelativo = models.IntegerField(primary_key=True)
    envcorrelativo = models.IntegerField()
    vencorrelativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'respuestasrecdte_acuseventas'
        unique_together = (('resreccorrelativo', 'envcorrelativo', 'vencorrelativo'),)


class RespuestasrecdteEnvios(models.Model):
    resreccorrelativo = models.IntegerField(primary_key=True)
    envcorrelativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'respuestasrecdte_envios'
        unique_together = (('resreccorrelativo', 'envcorrelativo'),)


class RespuestasrecdteVentas(models.Model):
    resreccorrelativo = models.IntegerField(primary_key=True)
    vencorrelativo = models.IntegerField()
    resrecorrelativoacuse = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'respuestasrecdte_ventas'
        unique_together = (('resreccorrelativo', 'vencorrelativo'),)


class Respuestasrecibidasdte(models.Model):
    resreccorrelativo = models.IntegerField(primary_key=True)
    socrut = models.CharField(max_length=9, blank=True, null=True)
    clirut = models.CharField(max_length=9, blank=True, null=True)
    resrecid = models.BigIntegerField(blank=True, null=True)
    pardterestipo = models.IntegerField(blank=True, null=True)
    resrecnumdetalles = models.IntegerField(blank=True, null=True)
    resreccontacto = models.CharField(max_length=40, blank=True, null=True)
    resrecfonocontacto = models.CharField(max_length=40, blank=True, null=True)
    resrecemailcontacto = models.CharField(max_length=100, blank=True, null=True)
    resrecarchivo = models.CharField(max_length=150, blank=True, null=True)
    resrecfecha = models.DateField(blank=True, null=True)
    fecactualiza = models.DateField(blank=True, null=True)
    adjcorrelativo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'respuestasrecibidasdte'


class RolFuncion(models.Model):
    rolid = models.FloatField(blank=True, null=True)
    funid = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol_funcion'


class Roles(models.Model):
    rolid = models.IntegerField(blank=True, null=True)
    rolnombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Sociedades(models.Model):
    socid = models.BooleanField(primary_key=True)
    socrut = models.CharField(max_length=9, blank=True, null=True)
    socactividad = models.CharField(max_length=150, blank=True, null=True)
    socdireccion = models.CharField(max_length=150, blank=True, null=True)
    socfono = models.CharField(max_length=20, blank=True, null=True)
    socemail = models.CharField(max_length=50, blank=True, null=True)
    socvigencia = models.CharField(max_length=1, blank=True, null=True)
    socactecosii = models.CharField(max_length=20, blank=True, null=True)
    socciudad = models.CharField(max_length=50, blank=True, null=True)
    socrazonsocial = models.CharField(max_length=100, blank=True, null=True)
    socnombrecorto = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sociedades'


class Sucursales(models.Model):
    sucid = models.IntegerField(primary_key=True)
    sucnombre = models.CharField(max_length=50, blank=True, null=True)
    socid = models.ForeignKey(Sociedades, models.DO_NOTHING, db_column='socid', blank=True, null=True)
    sucdireccion = models.CharField(max_length=150, blank=True, null=True)
    sucfono = models.CharField(max_length=20, blank=True, null=True)
    sucfax = models.CharField(max_length=20, blank=True, null=True)
    succiucodigo = models.IntegerField(blank=True, null=True)
    sucvigencia = models.CharField(max_length=1, blank=True, null=True)
    succodsii = models.CharField(max_length=20, blank=True, null=True)
    escasamatriz = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursales'


class TipoAccesorio(models.Model):
    id_tipo_acc = models.FloatField(primary_key=True)
    descripcion_tipo_acc = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_accesorio'


class Tipooperacion(models.Model):
    opeid = models.FloatField(blank=True, null=True)
    openombre = models.CharField(max_length=40, blank=True, null=True)
    opedescripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipooperacion'


class Tipooperacioncompra(models.Model):
    opeid = models.IntegerField(blank=True, null=True)
    openombre = models.CharField(max_length=40, blank=True, null=True)
    opedescripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipooperacioncompra'


class Trabajadores(models.Model):
    id_trabajador = models.FloatField(primary_key=True)
    rut_trabajador = models.CharField(max_length=9, blank=True, null=True)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=25, blank=True, null=True)
    apellido_materno = models.CharField(max_length=25, blank=True, null=True)
    #direccion = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trabajadores'


class Users(models.Model):
    id_user = models.FloatField(primary_key=True)
    username = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    vigente = models.CharField(max_length=1, blank=True, null=True)
    id_vendedor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsuarioRol(models.Model):
    usrid = models.FloatField(blank=True, null=True)
    rolid = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_rol'


class Vendedores(models.Model):
    id_vendedor = models.FloatField(primary_key=True)
    rut_vendedor = models.CharField(max_length=9, blank=True, null=True)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=25, blank=True, null=True)
    apellido_materno = models.CharField(max_length=25, blank=True, null=True)
    #direccion = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendedores'


class Vendocrelaciona(models.Model):
    id_venta1 = models.FloatField(blank=True, null=True)
    id_venta2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendocrelaciona'


class VentaProductos(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    id_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto')
    id_accesorio = models.ForeignKey(Accesorios, models.DO_NOTHING, db_column='id_accesorio')
    cantidad = models.IntegerField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    ctaid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta_productos'
        unique_together = (('id_venta', 'id_producto', 'id_accesorio'),)


class Ventas(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    rut_cliente = models.ForeignKey(ComunaClientes, models.DO_NOTHING, db_column='rut_cliente', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    descuento1 = models.FloatField(blank=True, null=True)
    descripcion_descuento1 = models.CharField(max_length=40, blank=True, null=True)
    descuento2 = models.FloatField(blank=True, null=True)
    descripcion_descuento2 = models.CharField(max_length=40, blank=True, null=True)
    recuperacion_flete = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    nro_factura = models.FloatField(blank=True, null=True)
    id_vendedor = models.ForeignKey(Vendedores, models.DO_NOTHING, db_column='id_vendedor', blank=True, null=True)
    #id_comuna = models.ForeignKey(ComunaClientes, models.DO_NOTHING, db_column='id_comuna', blank=True, null=True)
    #direccion = models.ForeignKey(ComunaClientes, models.DO_NOTHING, db_column='direccion', blank=True, null=True)
    localidad = models.CharField(max_length=20, blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    opeid = models.FloatField(blank=True, null=True)
    paropeestado = models.FloatField(blank=True, null=True)
    pardteestado = models.FloatField(blank=True, null=True)
    venmtoneto = models.FloatField(blank=True, null=True)
    venmtoexento = models.FloatField(blank=True, null=True)
    venmtoimptoespecifico = models.FloatField(blank=True, null=True)
    venmtoiva = models.FloatField(blank=True, null=True)
    ventasaiva = models.FloatField(blank=True, null=True)
    usuingresa = models.IntegerField(blank=True, null=True)
    usuactualiza = models.IntegerField(blank=True, null=True)
    fecactualiza = models.DateField(blank=True, null=True)
    vennumpedido = models.CharField(max_length=20, blank=True, null=True)
    parpagtipo = models.FloatField(blank=True, null=True)
    venfechavencimiento = models.DateField(blank=True, null=True)
    recfecha = models.DateField(blank=True, null=True)
    usuaprueba = models.IntegerField(blank=True, null=True)
    venfechaaprueba = models.DateField(blank=True, null=True)
    cliuniid = models.IntegerField(blank=True, null=True)
    partipreversa = models.BooleanField(blank=True, null=True)
    vencorrelativorev = models.FloatField(blank=True, null=True)
    venrevdescripcion = models.CharField(max_length=100, blank=True, null=True)
    venfecreversa = models.DateField(blank=True, null=True)
    sucid = models.ForeignKey(Sucursales, models.DO_NOTHING, db_column='sucid', blank=True, null=True)
    mpasii = models.CharField(max_length=2, blank=True, null=True)
    centralizado = models.CharField(max_length=1, blank=True, null=True)
    periodocentraliza = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas'


class VentasImpuestos(models.Model):
    vencorrelativo = models.OneToOneField(Ventas, models.DO_NOTHING, db_column='vencorrelativo', primary_key=True)
    vencodimpto = models.IntegerField()
    ventasaimpto = models.FloatField()
    venmtoimpto = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas_impuestos'
        unique_together = (('vencorrelativo', 'vencodimpto', 'ventasaimpto'),)


class VentasMensaje(models.Model):
    vencorrelativo = models.FloatField(blank=True, null=True)
    venmensaje = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas_mensaje'


class VentasPedidos(models.Model):
    id_venta = models.FloatField(blank=True, null=True)
    id_pedido = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas_pedidos'


class Zona(models.Model):
    id_zona = models.IntegerField(primary_key=True)
    nombre_zona = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zona'
