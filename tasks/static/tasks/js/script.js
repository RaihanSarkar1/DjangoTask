$(document).ready(function () {

    $('[data-toggle="tooltip"]').tooltip();


    $(".edit-todo-input").on("click", function (event) {
        console.log("clicked"); 
        var url = $(this).data("target");
        console.log(url);
        location.replace(url);
    });
});
