var chemicalElementCompositionSimplePopupOptions = {
    width: 800,
    title: "Chemical Composition",
    create: function(event, ui) {
        // Initialization
        $(this).find('.sample-row').hide();
        $(this).find('.saved-data').hide();
    },
}

saveChemicalElementCompositionSimpleData = function() {
    var hiddenSavedElements = openPopUp.find('.saved:hidden');
    $.each(hiddenSavedElements, function(index, hiddenElement) {
        $(hiddenElement).remove();
    });

    var elementList = openPopUp.find('.element-list tbody');
    var data = [];
    $.each(elementList.find('tr'), function(index, element) {
        var $element = $(element);
        var elementData = {};

        if(!$element.hasClass('empty')) {
            // name
            elementData.name = $element.find('.name').text();
            // qty
            elementData.qty = $element.find('.qty input').val();
            $element.find('.qty :input').attr('value', elementData.qty);
            // pur
            elementData.pur = $element.find('.pur input').val();
            $element.find('.pur :input').attr('value', elementData.pur);

            data.push(elementData);
        }
    });

    return {'elementList': JSON.stringify(data)};
}

configurePopUp('module-chemical-composition-simple',
                chemicalElementCompositionSimplePopupOptions,
                saveChemicalElementCompositionSimpleData);


