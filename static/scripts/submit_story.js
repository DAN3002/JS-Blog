$(document).ready(function (e) {
    const fullContentArea = new SimpleMDE({ element: $("#fullContent")[0], spellChecker: false });

    $("form").submit(function (e) {
        e.preventDefault();
        // let body = {
        //     title: $("#title").val(),
        //     image: $("#image").val(),
        //     sortContent: sortContentArea.options.previewRender(sortContentArea.value()),
        //     fullContent: fullContentArea.options.previewRender(fullContentArea.value()),
        // };
        // $.post("/PRJ321x_ASM4/upload", body, res => {
        //     window.location.href = "/PRJ321x_ASM4/admin/page";
        // });
    });
});
