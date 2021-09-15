function postForm(value, url, input_name) {
 
    var form = document.createElement('form');
    var request = document.createElement('input');
 
    form.method = 'POST';
    form.action = url;
 
    request.type = 'hidden';
    request.name = input_name;
    request.value = value;
 
    form.appendChild(request);
    document.body.appendChild(form);
 
    form.submit();

}