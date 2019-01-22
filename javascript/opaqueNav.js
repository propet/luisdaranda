$(document).ready(function()
  {

    // Opaque navbar from first section
    $(window).scroll(function()
      {
        if ($(this).scrollTop() > $("#presentacion").height() -
          5 &&
          (!$('#botonNav')[0].hasAttribute(
            'aria-expanded')))
        {
          $('.navbar').addClass('opaque');
        }
        else
        {
          if (!$('#botonNav')[0].hasAttribute(
            'aria-expanded'))
          {
            $('.navbar').removeClass('opaque');
          }
        }
      });

    // Solo quita la barra negra del boton si se ha pulsado
    // anteriormente alguna vez y esta expandido antes de pulsarlo de nuevo.
    $('#botonNav').on('click', function()
      {
        if ($('#botonNav')[0].hasAttribute(
          'aria-expanded') &&
          ($('#botonNav').attr('aria-expanded') ==
            "true"))
        {
          $('.navbar').removeClass('opaque');
        }
        else
        {
          $('.navbar').addClass('opaque');
        }
      });

    // Slide animation
    $(window).scroll(function()
      {
        $(".slideanim").each(function()
          {
            var pos = $(this).offset().top;

            var winTop = $(window).scrollTop();
            if (pos < winTop + 800)
            {
              $(this).addClass("slide");
            }
          });
      });

    // Mueve el molinillo cada vez que se le haga click a un enlace
    // de la barra de navegacion
    $('.navbar a').on('click', function()
      {
        $('#molino').addClass('spin');
        setTimeout(function()
          {
            $('#molino').removeClass('spin');
          }, 900);
      });


    // scroll page to current location 1 px down, then 1 pixel up,
    // to update the animations triggered by scrolling
    $(window).scrollTop($(window).scrollTop() + 1);
    $(window).scrollTop($(window).scrollTop() - 1);

  }); //end of document.ready
