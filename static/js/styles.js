var dataSet = [
    [ "write-good", "System Architect", "Naive linter for English prose for developers who can't write good and wanna learn to do other stuff good too." ],
];

$(document).ready(function() {
    $('#example').DataTable( {
        data: dataSet,
        columns: [
            { title: "Name" },
            { title: "Categories" },
            { title: "Description" }
        ],
        "paging":   false,
        "ordering": false,
        "info":     false,
        "searching": false
    } );
} );
