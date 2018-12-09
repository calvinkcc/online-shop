$(document).ready(function(){
    setVisible();

    /* when your select country */
    $("select#id_country").change(function () {
        $("select#id_country option:selected").each(function(){
            var country = $(this).text();
            if (country == 'United States'){
                doStateFieldSelectable();
            }else{
                undoStateFieldSelectable();
            }
        });
    }).change();

    /* When the form is submitted */
    $('form#new_billing_address').submit(function(){
        var inputStateField = $('input#id_state');
        if (inputStateField.attr('state') == 'hidden'){
            $("select#id_state_select option:selected").each(function(){
                var stateValue = $(this).val();
                $('input#id_state').attr('value', stateValue);
            });
        }
    });
});

function doStateFieldSelectable(){
    hideStateField();
    createSelectField();
    setStates();
}

function undoStateFieldSelectable(){
    removeSelectField();
    showStateField();
}

function createSelectField(){
    var inputStateField = $('input#id_state');
    optionFields = setStates();
    var selectField = '<select id="id_state_select" class="form-control" >'+ optionFields +'</select>';
    inputStateField.after(selectField);
}

function createSelectFieldOptions(abbrs, names){
    var optionTemplate;
    for (var i=0; i<abbrs.length; i++){
        optionTemplate += '<option value="' + abbrs[i] + '">' + names[i] + '</option>';
    }
    return optionTemplate;
}

function removeSelectField(){
    $('select#id_state_select').remove();
}

function setStates(){
    var abbreviations = [
        'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
        'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
        'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
        'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
        'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
    ];
    var names = [
        'Alabama', 'Alaska', 'Arizona', 'Arkanasa', 'California',
        'Colorado', 'connecucut', 'Delaware', 'Florida', 'Georgia',
        'Hawaii', 'Idaho', 'Illinuis', 'Indiana', 'Iowa',
        'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
        'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri',
        'Montana', 'Nabraska', 'Nevada', 'New Hampshire', 'New Jersey',
        'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
        'Oklahoma', 'Oregon', 'Pensylvania', 'Rhode Island', 'South Carolina',
        'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
        'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
    ];
    return createSelectFieldOptions(abbreviations, names);
}

function hideStateField(){
    $('input#id_state').hide();
    setHidden();
}

function showStateField(){
    $('input#id_state').show();
    setVisible();
}

function setVisible(){
    $('input#id_state').attr('state', 'visible');
}

function setHidden(){
    $('input#id_state').attr('state', 'hidden');
}
