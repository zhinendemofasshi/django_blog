$(document).ready(function (){
    ClassicEditor
    .create(document.querySelector('#id_content'), {

        licenseKey: '',


    })
    .then(editor => {
        window.editor = editor;


    })
    .catch(error => {
        console.error('Oops, something went wrong!');
        console.error('Please, report the following error on https://github.com/ckeditor/ckeditor5/issues with the build id and the error stack trace:');
        console.warn('Build id: 49kbmk7lb4lf-va616ze6u36o');
        console.error(error);
    });
})
