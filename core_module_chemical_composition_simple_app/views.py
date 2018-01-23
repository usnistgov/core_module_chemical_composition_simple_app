""" Chemical composition simple module view
"""
import json

from core_parser_app.tools.modules.views.builtin.popup_module import AbstractPopupModule
from core_parser_app.tools.modules.views.module import AbstractModule
from core_module_chemical_composition_app.views import render_chemical_composition


class ChemicalCompositionSimpleModule(AbstractPopupModule):
    def __init__(self):

        template = AbstractModule.render_template('core_module_periodic_table_app/periodic.html')
        popup_content = AbstractModule.render_template('core_module_chemical_composition_simple_app/'
                                                       'chemical_composition_simple.html',
                                                       {'periodic_table': template})

        AbstractPopupModule.__init__(self, popup_content=popup_content, button_label='Select Element',
                                     styles=['core_module_periodic_table_app/css/periodic.css',
                                             'core_module_chemical_composition_app/css/'
                                             'chemical_element_composition.css'],
                                     scripts=['core_module_chemical_composition_app/js/events.js',
                                              'core_module_chemical_composition_simple_app/js/'
                                              'chemical_element_composition_simple.js'])

    def _retrieve_data(self, request):
        """ Retrieve module's data

        Args:
            request:

        Returns:

        """
        data = ''
        if request.method == 'GET':
            if 'data' in request.GET:
                data = request.GET['data']
        elif request.method == 'POST':
            if 'elementList' in request.POST:
                element_list = json.loads(request.POST['elementList'])
                if len(element_list) > 0:
                    element_list_xml = ""
                    for element in element_list:
                        element_list_xml += '<constituent>'
                        element_list_xml += "<element>" + element['name'] + "</element>"
                        element_list_xml += "<quantity>" + element['qty'] + "</quantity>"
                        if element['pur'] != '':
                            element_list_xml += "<purity>" + element['pur'] + "</purity>"

                        element_list_xml += '</constituent>'
                    # set the data
                    data = element_list_xml
        return data

    def _render_data(self, request):
        """ Return module's data rendering

        Args:
            request:

        Returns:

        """
        return render_chemical_composition(self.data, True, False)
