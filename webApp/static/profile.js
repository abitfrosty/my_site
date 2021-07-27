function listener() {

    const notifications = document.getElementById('notifications');
    rebindSubmit(document.getElementById('formNameUpdate'));
    rebindSubmit(document.getElementById('formEmailUpdate'));
    rebindSubmit(document.getElementById('formPasswordUpdate'));
    rebindSubmit(document.getElementById('formProfileUpdate'));
    
    function update(myForm, lastInput) {
        const xhr = new XMLHttpRequest();

        xhr.onload = function() {
          if (xhr.readyState === xhr.DONE && xhr.status === 200) {
            notifications.insertAdjacentHTML('afterbegin', xhr.response);
            alertTimer();
            // Bootstrap's button focus fix
            lastInput.focus(); lastInput.blur();
              }
          }

        xhr.onerror = function() {
          dump("Error while getting xhr.");
        }
        let myFormData = new FormData(myForm);
        appendCheckBoxes(myForm, myFormData);
        
        xhr.open(myForm.method, myForm.action, true);
        xhr.responseType = "json";
        xhr.send(myFormData);
    }
    
    function appendCheckBoxes(form, formData) {
        [...form.elements].forEach(function(elem){
            if (elem.type === 'checkbox'){
                formData.set(elem.name, Number(elem.checked))
            }
        });
    }

    
    function rebindSubmit(submitForm) {
        submitForm.addEventListener('submit', function(evt) {
            evt.preventDefault();
            update(submitForm, submitForm.elements[submitForm.length-2]);
        });
    }
        
    function alertTimer() {
        $(".alert").first().hide().slideDown(500).delay(4000).slideUp(200, function(){
            $(this).remove(); 
        });
    }
    
    $('#formPasswordUpdate').on('submit', function() {
        $(this).each(function() {
             this.reset();
        });
    });
    
}


document.addEventListener('DOMContentLoaded', listener);
