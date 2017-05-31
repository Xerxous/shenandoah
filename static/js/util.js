function display(show, hide) {
  document.getElementById(show).style.display = "";
  document.getElementById(hide).style.display = "none";
  document.getElementById(show + "-tab").className = "active";
  document.getElementById(hide + "-tab").className = "";
}
