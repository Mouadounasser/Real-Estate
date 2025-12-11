{
    'name': 'Real Estate Management',
    'version': '18.0.1.0.0',
    'category': 'Real Estate',
    'summary': 'Manage real estate properties, contracts, and maintenance',
    'description': """
        <div class="row">
            <div class="col-md-12">
                <h2 class="text-center">Real Estate Management Module</h2>
                <h3 class="text-center text-muted">A comprehensive solution for managing properties, contracts, and tenants.</h3>
            </div>
        </div>
        <hr/>
        <div class="row mt-4">
            <div class="col-md-12">
                <h4>Key Features:</h4>
                <ul>
                    <li><i class="fa fa-building"></i> <strong>Property Management:</strong> Track property details, status, and history.</li>
                    <li><i class="fa fa-file-text"></i> <strong>Contract Management:</strong> Handle rental and sales contracts efficiently.</li>
                    <li><i class="fa fa-wrench"></i> <strong>Maintenance:</strong> Log and track maintenance requests and costs.</li>
                    <li><i class="fa fa-bar-chart"></i> <strong>Dashboard:</strong> Visual insights into your real estate portfolio.</li>
                </ul>
            </div>
        </div>
    """,
    'images': ['static/description/cover.png'],
    'author': 'Alan',
    'depends': ['base', 'mail', 'web'],
    'data': [
        'security/real_estate_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/property_views.xml',
        'views/contract_views.xml',
        'views/maintenance_views.xml',
        'views/dashboard_views.xml',
        'views/menu_items.xml',
    ],
    'assets': {
        'web.assets_backend': [
             'real_estate_management_advanced/static/src/components/**/*.js',
             'real_estate_management_advanced/static/src/components/**/*.xml',
        ],
    },
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
