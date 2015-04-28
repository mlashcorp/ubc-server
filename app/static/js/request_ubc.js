$( document ).ready(function() {

    //alert("READY!");
});

var machine_id = "mach1";
var user_id = "user123";


var assay_id = 0; // Unitialized assay_id.

function monitor_assay() {
    $.get( "/query_assay", { machine_id: machine_id, user_id : user_id })
        .done(function(data) {
            //alert("Received progress data " + data);

            var progress = parseFloat(data);

            if (progress > 100.0) {
                alert("Finished :D");                
                window.location = "/view_assay";
            }
            else {
                $("#RunnindAssayProgressDiv").html("<p> Please wait...  "+progress+"%</p>");
                setTimeout(monitor_assay(), 10000);
            }
        });
}

function request_ubc_assay() {
    $.get( "/request_assay", function( data ) {
        alert( "Assay start requested! Received assay_id = " + data );
        assay_id = parseInt(data);        

        $("#StartAssayDiv")[0].style.visibility = "hidden";

        if (assay_id > 0) {
            $("#RunningAssayDiv")[0].style.visibility = "visible";
            monitor_assay();
        } 
        else {
            $("#FailedAssayDiv")[0].style.visibility = "visible";
        }
    });
}

function cancel_ubc_assay() {
    if (assay_id > 0) {
        alert("Assay " + assay_id + " canceled! (TODO)");
        assay_id = 0;
    } else {
        alert("No assay is running right now");
    }
}
    

