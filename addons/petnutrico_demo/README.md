# PetNutriCo Demo

Módulo de datos de demo para el caso práctico "PetNutriCo" (onboarding de partners Tecnicora). No tiene modelos Python propios — es 100% datos: empresa, productos, BoM, almacenes, reglas de reabastecimiento, puntos de calidad, cliente mayorista y plan de suscripción.

## Requisitos

- **Odoo 19.0 Enterprise** (Calidad, Suscripciones y Referencias son Enterprise-only; sin Enterprise el módulo fallará al instalar por dependencias faltantes).
- Base nueva, de preferencia recién creada (ver nota sobre país más abajo).

## Instalación

1. Copia la carpeta `petnutrico_demo/` a tu carpeta de addons (o al repo/branch de Odoo.sh que uses para la demo).
2. Actualiza la lista de aplicaciones (Ajustes → Apps → Actualizar lista de aplicaciones, con modo desarrollador activo).
3. Busca "PetNutriCo Demo" e instálalo. Esto instalará automáticamente todas sus dependencias: Fabricación, Calidad, Compras, Ventas, Inventario, Sitio Web, Suscripciones, Empleados, Reclutamiento, Referencias y Localización México.
4. **Instala con datos de demo activados** — los archivos bajo `demo/` solo cargan si la base tiene el modo demo habilitado (es el default en una base de prueba nueva de Odoo Online / Odoo.sh).

## Qué resuelve este módulo del caso

| Requerimiento del caso | Dónde está en el módulo |
|---|---|
| Empresa en México (corrige el país por defecto) | `data/res_company_data.xml` |
| 2 productos × 2 presentaciones | `demo/product_demo.xml` (4 productos independientes, ver nota de diseño abajo) |
| Materias primas + comparación de precio de proveedor | `demo/product_demo.xml` (2 proveedores con distinto precio en `seller_ids`) |
| Listas de materiales | `demo/mrp_bom_demo.xml` |
| 3 almacenes (Puebla/CDMX/Guadalajara) + ubicaciones internas | `demo/stock_warehouse_demo.xml` |
| Mínimo 300 piezas por variante | `demo/stock_orderpoint_demo.xml` |
| Puntos de control de calidad | `demo/quality_point_demo.xml` |
| Cliente mayorista, 30 días, límite $135,000 | `demo/res_partner_demo.xml` |
| Suscripción mensual para e-commerce | `demo/product_demo.xml` + `demo/sale_subscription_plan_demo.xml` |

## Lo que este módulo NO configura (y hay que hacer a mano)

Documentado así a propósito — son ajustes que dependen de configuración global de la empresa (`res.config.settings`) y no es seguro forzarlos desde datos XML sin verificarlos en tu instancia real:

1. **Lotes, Números de Serie y Fechas de Caducidad**: actívalos en Inventario → Configuración → Ajustes → Trazabilidad, antes de que las reglas de caducidad de los productos surtan efecto.
2. **Límite de Crédito de Ventas**: actívalo en Contabilidad → Configuración → Ajustes → Facturas de Clientes → "Límite de Crédito de Ventas". El campo `credit_limit` del cliente ya está puesto en $135,000, pero sin este ajuste activado Odoo no muestra la advertencia.
3. **Tipo de punto de control de calidad**: entra a cada punto de control (Calidad → Puntos de Control) y en el campo "Tipo" selecciona "Pass - Fail". No se fija por XML porque no pude confirmar con certeza el external ID exacto de ese registro en 19.0.
4. **Plan de suscripción en el producto**: en el producto "Suscripción mensual - Comida Perro 6kg", pestaña Ventas, asocia el plan "Mensual" que ya viene creado.
5. **Carta Porte (l10n_mx_edi_stock)**: no está en las dependencias de este módulo a propósito — es una pieza pesada (trae también la app Flotilla) y conviene instalarla y probarla por separado, después de validar el resto del flujo.

## Nota de diseño: por qué 4 productos y no 1 con variantes

El caso describe "2 productos, cada uno en 2 presentaciones", que en Odoo normalmente se modelaría con un atributo "Presentación" (30kg/6kg) generando variantes. Se decidió **no** hacerlo así en este módulo porque los IDs de variante (`product.product`) que Odoo genera automáticamente a partir de una plantilla con atributos no son estables ni predecibles desde datos XML — intentar referenciarlos rompe la reproducibilidad del módulo. En su lugar, se declaran 4 `product.product` independientes. Si prefieres modelarlo con variantes para que la demo se vea más "real" de cara al cliente, es un cambio manual sobre esta base, no algo que convenga automatizar en datos de instalación.

## Testing rápido

```bash
python odoo-bin -c odoo.conf -i petnutrico_demo -d nombre_de_tu_base --stop-after-init
```

Si algo falla al instalar, lo más probable es un external ID de dependencia (`account.account_payment_term_30days`, `mrp.picking_type_manufacturing`, etc.) que cambió de nombre en tu versión exacta — revisa el mensaje de error, que en Odoo siempre indica el external ID que no encontró.
