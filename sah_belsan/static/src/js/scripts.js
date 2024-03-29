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
   /* Initiate the wowjs animation library*/
   if($(".wow").length){
       new WOW().init();
   }
//   var myVar;
//   $('#wrap').on('click', function(){
//      myVar = setTimeout(showPage, 3000);
//    });
//
//   function showPage() {
//      document.getElementById("loader").style.display = "none";
//      document.getElementById("wrap").style.display = "block";
//    }
})

//var myVar;
//function loaderFunction() {
//  myVar = setTimeout(showPage, 1000);
//}
//function showPage() {
//  document.getElementById("loader").style.display = "none";
//  document.getElementById("wrap").style.display = "block";
//}

$(function() {
    'use strict';
    $('.owl-quick-access').owlCarousel({
        loop: true,
        autoplay : true,
        nav: false,
        margin: 5,
        rtl:true,
        dots: false,
        responsive: {
            0: {
                items: 1
            },
            300: {
                items: 2
            },
            576: {
                items: 3
            },
            768: {
                items: 4
            },
            992: {
                items: 5
            },
            1200: {
                items: 7
            }
        },
    })
    $('.owl-product-home').owlCarousel({
        items: 4,
        margin: 1,
        nav: true,
        autoplay : true,
        rtl:true,
        dots: false,
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 2
            },
            992: {
                items: 4
            }
        },
    });
    $('.product_brand_slider').owlCarousel({
        items: 5,
        margin: 1,
        autoplay : true,
        nav: true,
        rtl:true,
        loop:true,
        dots: false,
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 3
            },
            992: {
                items: 5
            }
        },
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