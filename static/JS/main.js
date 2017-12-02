$("#api-select").on('change', function(){
    if($(this).val() !== "None"){
        $.ajax({
            url: '/getAPIRequests/',
            data: {
                'api_id': $(this).val()
            },
            dataType: 'json',
            success: function (result) {
                var requests = $('#requests');
                if(!requests.is(":visible")){
                    requests.show()
                }
                requests.DataTable({
                    "aaData": result,
                    "aoColumns": [
                        { "mDataProp": "id" },
                        { "mDataProp": "api_name" },
                        { "mDataProp": "preferred_run_date" },
                        { "mDataProp": "params" },
                        { "mDataProp": "status" },
                        {
                            data: 'id',
                            render: function (data) {
                                return '<input type="button" id="'+data+'" value="Run" class="script-run-btn"/>';
                            }
                        }

                    ],
                    destroy: true
                });
            }
        })
        .done(function(){
            $('.script-run-btn').on('click', function(){
                alert(this.id);
            });
        });
    }
});