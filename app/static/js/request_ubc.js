$( document ).ready(function() {

    //alert("READY!");
});

var machine_id = "mach1";
var user_id = "user123";


var assay_id = ""; // Unitialized assay_id.


function monitor_assay() {
    assay_id = getCookie("assay_id");

    $.get( "/query_assay", { machine_id: machine_id, user_id : user_id })
        .done(function(data) {
            var progress = parseFloat(data);

            if (progress > 100.0) {
                window.location = "/view_assay";
            }
            else {
                //$("#RunnindAssayProgressDiv").html("<p> Running assay with assay_id = "+assay_id+"</p>");
                
                $("#RunningAssayProgress").val(String(progress)).trigger("change");

                setTimeout(monitor_assay, 1000);
            }
        });
}

function request_ubc_assay() {
    $.get( "/request_assay", function( data ) {

        assay_id = data;

        setCookie("assay_id", assay_id, 1); // lasts for 1 day

        window.location = "/running_assay";

        monitor_assay();
    });
}

function cancel_ubc_assay() {
    assay_id = getCookie("assay_id");

    $.get("/cancel_assay", { assay_id : assay_id })
        .done(function(data) {
            window.location = "/start_assay";
            setCookie("assay_id", "", 1);
        });
}
    

