$( document ).ready(function() {

    //alert("READY!");
});

var machine_id = "mach1";
var user_id = "user123";


var assay_id; // Unitialized assay_id.

function monitor_assay() {
    $.get( "/query_assay", { machine_id: machine_id, user_id : user_id })
        .done(function(data) {
            var progress = parseFloat(data);

            if (progress > 100.0) {
                window.location = "/view_assay";
            }
            else {
                $("#RunnindAssayProgressDiv").html("<p> Running assay with assay_id = "+assay_id+"</p>"+"<p> Please wait...  "+progress+"%</p>");
                setTimeout(monitor_assay, 1000);
            }
        });
}

function request_ubc_assay() {
    $.get( "/request_assay", function( data ) {
        assay_id = data;        

        $("#StartAssayDiv")[0].style.visibility = "hidden";
        $("#RunningAssayDiv")[0].style.visibility = "visible";
        monitor_assay();
    });
}

function cancel_ubc_assay() {
    $.get("/cancel_assay", { assay_id : String(assay_id) })
        .done(function(data) {
            if (data == "False") {
                alert("Assay id =" + assay_id + " cancel failed.");
            }
            window.location("/start_assay");
            assay_id = 0;            
        });
}
    

