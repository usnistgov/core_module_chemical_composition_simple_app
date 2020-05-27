""" Url router for the chemical composition simple module
"""

from django.urls import re_path

from core_module_chemical_composition_simple_app.views import (
    ChemicalCompositionSimpleModule,
)

urlpatterns = [
    re_path(
        r"module-chemical-composition-simple",
        ChemicalCompositionSimpleModule.as_view(),
        name="core_module_chemical_composition_simple",
    ),
]
