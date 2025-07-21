// Swiper for Featured Projects
if (document.querySelector('.featured-swiper')) {
    new Swiper('.featured-swiper', {
        slidesPerView: 3,
        spaceBetween: 30,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        breakpoints: {
            0: { slidesPerView: 1 },
            768: { slidesPerView: 2 },
            992: { slidesPerView: 3 }
        }
    });
}

// Swiper for Featured Videos
if (document.querySelector('.featured-videos-swiper')) {
    new Swiper('.featured-videos-swiper', {
        slidesPerView: 3,
        spaceBetween: 30,
        // Remove navigation arrows
        // navigation: {
        //     nextEl: '.featured-videos-next',
        //     prevEl: '.featured-videos-prev',
        // },
        pagination: false,
        grabCursor: true,
        mousewheel: true,
        scrollbar: {
            el: '.featured-videos-scrollbar',
            draggable: true,
            hide: false,
        },
        breakpoints: {
            0: { slidesPerView: 1 },
            768: { slidesPerView: 2 },
            992: { slidesPerView: 3 }
        }
    });
}

// Swiper for Featured Images
if (document.querySelector('.featured-images-swiper')) {
    new Swiper('.featured-images-swiper', {
        slidesPerView: 3,
        spaceBetween: 30,
        grabCursor: true,
        mousewheel: true,
        scrollbar: {
            el: '.featured-images-scrollbar',
            draggable: true,
            hide: false,
        },
        breakpoints: {
            0: { slidesPerView: 1 },
            768: { slidesPerView: 2 },
            992: { slidesPerView: 3 }
        }
    });
}

// Responsive Image Modal Logic
if (typeof window !== 'undefined') {
  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.view-image-btn').forEach(function(btn) {
      btn.addEventListener('click', function() {
        var imgSrc = this.getAttribute('data-img-src');
        var modal = document.getElementById('imageModal');
        var modalImg = document.getElementById('modalImage');
        modalImg.src = imgSrc;
        modal.style.display = 'block';
      });
    });
    var closeBtn = document.getElementById('closeImageModal');
    if (closeBtn) {
      closeBtn.onclick = function() {
        document.getElementById('imageModal').style.display = 'none';
      };
    }
    window.onclick = function(event) {
      var modal = document.getElementById('imageModal');
      if (event.target === modal) {
        modal.style.display = 'none';
      }
    };
  });
}
// End Responsive Image Modal Logic
