$(function() {
    'use strict';
    $('.langs_dropdown').on('click', function() {
        $(this).find('ul').toggle();
    });
    $('body').on('click', '.o_header_affix .langs_dropdown, .o_header_affix .langs_dropdown ul', function() {
        $(this).find('ul').toggle();
    });
    $(document).on('click', function() {
        $('.nav_menu_language').hide();
    });
    $(document).on('click', '.o_header_affix .langs_dropdown .nav_menu_language', function() {
        $(this).hide();
    });
    $('.langs_dropdown').on('click', function(e) {
        e.stopPropagation();
    });
    $('body').on('click', '.o_header_affix .langs_dropdown', function(e) {
        e.stopPropagation();
    });
})
function searchFun() {
  var x = document.getElementById("belsan_header_search_input");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}