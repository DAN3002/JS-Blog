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


            console.log(fd);

            $.ajax({
                type: "POST",
                url: "/blog/upload",
                data: fd,
                processData: false,
                contentType: false,
                success: function (data) {
                    console.log(data);
                },
                error: function (err) {
                    console.log(err);
                }
            });

            // $.post("/blog/upload", body, res => {
            //     console.log(res);
            //     // window.location.href = "/PRJ321x_ASM4/admin/page";
            // });
    });
});
