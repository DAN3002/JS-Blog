$(document).ready(function (e) {
    const fullContentArea = new SimpleMDE({ element: $("#fullContent")[0], spellChecker: false });

    $("form").submit(function (e) {
        e.preventDefault();
            const body = {
                name: $("#name").val(),
                role: $("#role").val(),
                subtitle: $("#subtitle").val(),
                image: $("#image").prop('files')[0],
                fullContent: fullContentArea.options.previewRender(fullContentArea.value()),
            };
            const fd = new FormData();  
            fd.append("image", body.image);
            fd.append("name", body.name);
            fd.append("role", body.role);
            fd.append("subtitle", body.subtitle);
            fd.append("fullContent", body.fullContent);


            // Clear Inputs
            $("#name").val("");
            $("#role").val("");
            $("#subtitle").val("");
            $("#image").val("");
            fullContentArea.value("");

            $.ajax({
                type: "POST",
                url: "/blog/upload",
                data: fd,
                processData: false,
                contentType: false,
                success: function (data) {
                    // Alert using Swal
                    Swal.fire({
                        title: "Success!",
                        text: "Your story has been uploaded!",
                        icon: "success",
                    }).then(() => {
                        window.location.href = "/";
                    });
                },
                error: function (err) {
                    Swal.fire({
                        title: "Error!",
                        text: "Something went wrong!",
                        icon: "error",
                    });
                }
            });
    });
});
