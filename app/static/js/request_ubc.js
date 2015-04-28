$( document ).ready(function() {

    //alert("READY!");
});

var assay_id = 0; // Unitialized assay_id.

function monitor_assay() {
    var machine_id = "mach1";
    var user_id = "user123";

    var assay_finished = false;


    $.get( "http://localhost:5000/query_assay", { machine_id: machine_id, user_id : user_id })
        .done(function(data) {
            alert("Received progress data" + data);

            if (float(data) > 1) {
                alert("Finished :D");
            }
            else {
                $("#RunnindAssayProgressDiv").html("<p>"+data+"</p>");
                setTimeout(monitor_assay(), 1000);
            }
        });

}

function request_ubc_assay() {
    $.get( "http://localhost:5000/request_assay", function( data ) {
        alert( "Assay start requested! Received assay_id = " + data );
        assay_id = data;        

        $("#StartAssayDiv")[0].style.visibility = "hidden";

        if (assay_id > 0) {
            $("#RunningAssayDiv")[0].style.visibility = "visible";
            setTimeout(monitor_assay(), 1000);
        } 
        else {
            $("#FailedAssayDiv")[0].style.visibility = "visible";
        }
    });

    alert("Redirect this to the assay result page!");
}

function cancel_ubc_assay() {
    alert("Assay " + assay_id + " canceled!");
    assay_id = 0;
}
    

