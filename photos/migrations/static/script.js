
function imgWindow() {
    window.open("image")
  }
  $(document).ready(function () {
    $(function () {
      $('.photoUrl').click(function () {
        $(this).focus();
        $(this).select();
        document.execCommand('copy');
        alert("Copied to clipboard");
      });
    });
  });
  