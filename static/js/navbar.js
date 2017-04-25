$(document).ready(function() {
    $('#multiselect').multiselect();
    $(".num-input").keydown(function(e) {
        if($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110]) !== -1 ||
          (e.keyCode == 65 && (e.ctrlKey === true || e.metaKey === true)) ||
          (e.keyCode == 67 && (e.ctrlKey === true || e.metaKey === true)) ||
          (e.keyCode == 88 && (e.ctrlKey === true || e.metaKey === true)) ||
          (e.keyCode >= 35 && e.keyCode <= 39)){
            return;
        }
        if((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)){
            e.preventDefault();
        }
    });
  document.getElementById('exception').onchange = function() {
    document.getElementById('low').disabled = this.checked;
    document.getElementById('high').disabled = this.checked;
  };
});
