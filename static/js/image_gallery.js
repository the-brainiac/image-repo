// Delete Comment
function delete_image(url, csrf_token) {
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to recover this once deleted!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            $.ajax({
                url: url,
                type: "DELETE",
                headers: {
                    'X-CSRFToken': csrf_token,
                },
                dataType: "json",
                success: function(data, status) {
                    Swal.fire(
                            'Deleted!',
                            'Comment has been deleted.',
                            'success'
                        )
                        .then(ok => {
                            if (ok) {
                                location.reload();
                            }
                        });
                },
                error: function(data, status) {
                    swal.fire("opps!", "some error occured please try again", "error");
                    console.log(data);
                    console.log(status);
                }
            });
        }
    })
}

// Add Catagory
function add_catagory(url, csrf_token) {
    Swal.fire({
        title: "Add Catagory",
        text: "Catagory Name:",
        input: 'text',
        showCancelButton: true,
        confirmButtonText: 'Add'
    }).then((result) => {
        if (result.value == "") {
            Swal.fire({
                text: 'Catagory Name can not be Empty'
            });
        } else {
            $.ajax({
                url: url,
                type: "POST",
                headers: {
                    'X-CSRFToken': csrf_token,
                },
                data: JSON.stringify({ "name": result.value }),
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                success: function(data, status) {
                    var option = `<option value="${data.id}" selected>${data.name}</option>`;
                    $('#id_catagory').append(option);

                },
                error: function(data, status) {
                    var error = '';
                    for (var text in data.responseJSON) {
                        error += data.responseJSON[text];
                    }
                    swal.fire("oops!", error, "warning");
                }
            });
        }
    });
}