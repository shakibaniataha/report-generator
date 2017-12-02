$("#api-select").on('change', function(){
    if($(this).val() !== "None"){
        $.ajax({
            url: '/getAPIRequests/',
            data: {
                'api_id': $(this).val()
            },
            dataType: 'json',
            success: function (data) {
                var requests = $('#requests');
                if(!requests.is(":visible")){
                    requests.show()
                }
                requests.DataTable({
                    "aaData": data,
                    "aoColumns": [
                        { "mDataProp": "id" },
                        { "mDataProp": "api_name" },
                        { "mDataProp": "preferred_run_date" },
                        { "mDataProp": "params" },
                        { "mDataProp": "status" }
                    ],
                    destroy: true
                });
            }
        });
    }
});