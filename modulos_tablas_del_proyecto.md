# sistema de inventario

## Modulos

### Módulo de Productos:
- Tipo de producto (Consumible, Servicio, Almacenable)
- Nombre del producto
- Precio de venta
- Impuestos del cliente (IVA u otros)
- Costo de compra
- Categoría de producto
- Peso (Kg)
- Volumen (m³)
- Rutas (Fabricación, Compra, Bajo pedido)

### Módulo de Datos de la Compañía:

- Nombre de la compañía
- Logo
- Dirección (Calle, Calle 2, Ciudad, Estado, Código Postal, País)
- Teléfono
- Móvil
- Correo electrónico
- Color de la empresa

### Módulo de Ventas:

- Número de venta (REF0001)
- Fecha de creación de la venta
- Fecha de entrega prevista
- Fecha de entrega real
- Actividad relacionada con la venta
- Base imponible
- Impuesto
- Total de la venta
- Categoría de venta
- Estado de la venta (Presupuesto enviado, Cancelado, Presupuesto, Pedido de venta, etc.)
- Estado de la factura relacionada con la venta (Facturado, Nada que facturar, A facturar)

### Módulo de Facturación:

- Producto(s) vendido(s)
- Cantidad de productos
- Precio unitario
- Tasa de impuesto aplicada


### Módulo de Gestión de Clientes:

- Nombre del cliente
- Datos de contacto (Teléfono, Correo electrónico)
- Dirección de facturación
- Historial de compras
- Límite de crédito (si aplicable)
- Notas y comentarios

### Módulo de Gestión de Proveedores:

- Nombre del proveedor
- Datos de contacto (Teléfono, Correo electrónico)
- Dirección del proveedor
- Historial de compras
- Términos de pago (Plazo de crédito, condiciones de pago)
- Notas y comentarios

### Módulo de Generación de Informes Financieros:

- Estado de resultados (Ingresos, Gastos, Utilidades)
- *Balance general (Activos, Pasivos, Patrimonio)
- *Flujo de efectivo
- *Informes de cuentas por cobrar y cuentas por pagar
- *Informes de ventas y compras
- *Informes de impuestos (IVA, Retenciones, etc.)

### Módulo de Generación de Informes de Inventario:

- Valor del inventario
- Informes de inventario por producto
- Informes de movimientos de inventario (entradas, salidas, transferencias)
- Niveles de stock mínimo y máximo
- *Informes de depreciación de activos (si aplicable)

### Módulo de Gestión de Pagos y Recibos:

- Registro de pagos recibidos de clientes
- Registro de pagos realizados a proveedores
- *Conciliación bancaria
- *Notas de crédito y débito
- *Registros de transacciones financieras
- *Estado de cuentas de clientes y proveedores



# Tablas Principales:
    Tabla de Productos:
        ID_Producto (Clave Primaria)
        Tipo de Producto
        Nombre
        Precio de Venta
        Impuestos del Cliente (Referencia a tabla de Impuestos)
        Costo
        Categoría de Producto
        Peso (Kg)
        Volumen (m³)
        Rutas

    Tabla de Datos de la Compañía:
        ID_Compañia (Clave Primaria)
        Nombre de la Compañía
        Logo
        Dirección
        Teléfono
        Móvil
        Correo Electrónico
        Color

    Tabla de Ventas:
        ID_Venta (Clave Primaria)
        Número de Venta
        Fecha de Creación
        Fecha de Entrega Prevista
        Fecha de Entrega Real
        Actividad
        Base Imponible
        Impuesto
        Total de Venta
        Categoría de Venta
        Estado de Venta
        Estado de Factura (Referencia a tabla de Estados de Factura)
        Cliente (Referencia a tabla de Clientes)

    Tabla de Factura:
        ID_Factura (Clave Primaria)
        Producto (Referencia a tabla de Productos)
        Cantidad
        Precio Unitario
        Tasa de Impuesto

    Tabla de Compras:
        ID_Compra (Clave Primaria)
        Número de Orden de Compra
        Fecha de Creación
        Fecha de Entrega Prevista
        Proveedor (Referencia a tabla de Proveedores)
        Estado de Orden de Compra
        Total de Orden de Compra

    Tabla de Detalle de Compra:
        ID_Detalle_Compra (Clave Primaria)
        Orden de Compra (Referencia a tabla de Compras)
        Producto (Referencia a tabla de Productos)
        Cantidad
        Precio Unitario
        Total por Línea de Producto
        Impuestos Aplicados

    Tabla de Recepción de Mercancía:
        ID_Recepción (Clave Primaria)
        Fecha de Recepción
        Cantidad Recibida por Producto
        Número de Factura de Proveedor Relacionada
        Verificación de Calidad
        Observaciones
        Detalle de Compra (Referencia a tabla de Detalle de Compra)

## Tablas Adicionales:

    Tabla de Clientes:
        ID_Cliente (Clave Primaria)
        Nombre del Cliente
        Datos de Contacto
        Dirección de Facturación
        Historial de Compras
        Categoría de Cliente
        Saldo del Cliente

    Tabla de Proveedores:
        ID_Proveedor (Clave Primaria)
        Nombre del Proveedor
        Datos de Contacto
        Dirección del Proveedor
        Historial de Compras
        Categoría de Proveedor
        Saldo del Proveedor
        Términos de Pago

    Tabla de Estados de Venta:
        ID_Estado_Venta (Clave Primaria)
        Nombre del Estado

    Tabla de Estados de Factura:
        ID_Estado_Factura (Clave Primaria)
        Nombre del Estado

    Tabla de Impuestos:
        ID_Impuesto (Clave Primaria)
        Nombre del Impuesto
        Tasa del Impuesto
