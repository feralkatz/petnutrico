{
    'name': 'PetNutriCo Demo',
    'version': '19.0.1.0.0',
    'summary': 'Datos de demo para el caso práctico PetNutriCo (onboarding Tecnicora)',
    'description': """
Módulo de datos de demo para el caso práctico "PetNutriCo" usado en el
onboarding de partners de Tecnicora.

Configura:
- Empresa en México (corrige el país por defecto de la base de prueba)
- 2 productos terminados (comida perro / gato) con variantes 30kg y 6kg
- Materias primas y listas de materiales (BoM) por variante
- 3 almacenes (Puebla, CDMX, Guadalajara) con ubicaciones internas
- Reglas de reabastecimiento (mínimo 300 piezas por variante)
- Puntos de control de calidad en fabricación
- Cliente mayorista con términos de pago a 30 días y límite de crédito
- Plan de suscripción mensual para clientes de e-commerce
    """,
    'author': 'Tecnicora',
    'website': 'https://tecnicora.com',
    'license': 'LGPL-3',
    'category': 'Manufacturing',
    'depends': [
        'base_setup',
        'sale_management',
        'purchase',
        'stock',
        'mrp',
        'quality',
        'quality_mrp',
        'sale_subscription',
        'hr',
        'hr_recruitment',
        'hr_referral',
        'website_sale',
        'l10n_mx',
    ],
    'data': [
        'data/res_company_data.xml',
    ],
    'demo': [
        'demo/product_demo.xml',
        'demo/mrp_bom_demo.xml',
        'demo/stock_warehouse_demo.xml',
        'demo/stock_orderpoint_demo.xml',
        'demo/quality_point_demo.xml',
        'demo/res_partner_demo.xml',
        'demo/sale_subscription_plan_demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
