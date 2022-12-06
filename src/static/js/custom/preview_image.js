
$('.image_preview').change(function(event) {
  var fileName = event.target.files[0].name;
  $("#file").val(fileName);
  console.log(event.target.id)
  var preview_name = "preview_of_"+event.target.id
  console.log(preview_name)
  try {
    $( "#"+preview_name )?.remove();
  } catch (e){console.error(e)}
  var preview_el = document.getElementById(preview_name)
  if(!preview_el) {
    let img = document.createElement('img');
    img.id = preview_name;
    img.classList.add("img-thumbnail")
    img.style.width = '250px'
    this.after(img)
     preview_el = document.getElementById(preview_name)
  }

  var reader = new FileReader();
  reader.onload = function(e) {
    // get loaded data and render thumbnail.
    preview_el.src = e.target.result;
  };
  // read the image file as a data URL.
  reader.readAsDataURL(this.files[0]);
});
