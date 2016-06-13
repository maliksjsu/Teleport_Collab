/* ECOMMERCE */
var footer = $('.section-footer');
var footerHeight = footer.outerHeight();
var documentHeight = $(document).height();
var windowHeight = $(window).height();
var distanceToBottom = 0;
var scrollPos = $(window).scrollTop();

$(window).scroll(function() {
    'use strict';
    scrollPos = $(window).scrollTop();
    distanceToBottom = $(document).height() - ($(window).scrollTop() + $(window).height());
    if(distanceToBottom < footerHeight) {
        var asideBottom = footerHeight - distanceToBottom - 30;
        $('#aside').css('top', 'auto').css('bottom', asideBottom);
    }
    else {
        $('#aside').css('top', '').css('bottom', '');
    }
});

 $(window).ready(function() {
    if($('.product-quickview').length && $.fn.magnificPopup){
        $('.product-quickview').magnificPopup({
            image: {
              markup: '<div class="quickview-zoom">'+
                        '<div class="row">'+
                            '<div class="col-md-5">'+
                                '<div class="mfp-img"></div>'+
                            '</div>'+
                            '<div class="col-md-7">'+
                                '<h3 class="section-title">Custom Title</h3>'+
                                '<p class="price">$<span>21.99</span></p>'+
                                '<p class="description"></p>'+
                                '<div class="">'+
                                    '<div class="rateit" data-rateit-value="3.5" data-rateit-resetable="false" data-rateit-readonly="true"></div>'+
                                '</div>'+
                                '<a href="#" class="btn btn-buy btn-dark btn-animated"><i class="line-icon-basket"></i> Buy</a>'+
                            '</div>'+
                          '</div>'+
                      '</div>', 
              titleSrc: 'title',
              verticalFit: true
            },
            type: 'image',
            callbacks: {
                open: function() {
                    var mp = $.magnificPopup.instance;
                    cur = mp.st.el;
                    productTitle = cur.attr('data-title');
                    productPrice = cur.attr('data-price');
                    productDescription = cur.attr('data-description');
                    productRating = cur.attr('data-rating');
                    $('.quickview-zoom .section-title').text(productTitle);
                    $('.quickview-zoom .price span').text(productPrice);
                    $('.quickview-zoom .description').text(productDescription);
                    $('.rateit').rateit().rateit('value', productRating);
                }
            }
        });
    }
    

    $('.toggle-aside').on('click', function(e){
        e.preventDefault();
        setTimeout(function(){
            $('#ecommerce-sidebar').addClass('open');
        },100);
    });

    document.addEventListener('click', function(ev) {
        if($('#ecommerce-sidebar').hasClass('open')){
            var ecommerceSidebar = document.getElementById('ecommerce-sidebar');
            var target = ev.target;
            if( target !== ecommerceSidebar) {
                if($('#ecommerce-sidebar').hasClass('open')){
                    $('#ecommerce-sidebar').removeClass('open');
                }
            }
        }
    });
    $('.small-images img').on('click', function(){
        var imgSrc = $(this).attr('src');
        var mainImg = $('.main-image');
        mainImg.fadeOut(200, function(){
            mainImg.attr('src', imgSrc);
            $('.magnific').attr('data-mfp-src', imgSrc);
            mainImg.fadeIn('200');
        });
    });

    /* Remove Elements */
    $(".shopping-cart-table .remove-item").on('click', function(){
        $(this).closest('tr').fadeOut(200, function(){
            $(this).closest('tr').remove();
            var total = 0;
            $('.item-total').each(function(){
                total += +($(this).text());
            });
            $('.total p').text(total+'.00');
        });
    });

    /* Update total on quantity change */
    $(".shopping-cart-table .quantity").on('change', function(){
        var quantity = $(this).val();
        var itemPrice = $(this).closest('tr').find('.item-price').text();
        var itemTotal = quantity * itemPrice;
        $(this).closest('tr').find('.item-total').text(itemTotal+'.00');

        var total = 0;
        $('.item-total').each(function(){
        
            total += +($(this).text());
        });
        $('.total p').text(total+'.00');
    });
    if ($('[data-rel="tooltip"]').length && $.fn.tooltip) {
        $('[data-rel="tooltip"]').tooltip();
    }

    if($(".shopping-cart").length){
        cartWizard();
    }
    formValidation();
    

});

function cartWizard(){
    setTimeout(function(){
        $(".shopping-cart form").stepFormWizard({
            height: "auto",
            theme: 'sky',
            finishBtn: $('<input class="finish-btn sf-right sf-btn" type="submit" value="Confirm Payment"/>')
        });
    },100);
 }

function formValidation(){
    if($('.form-validation').length && $.fn.validate){
        /* We add an addition rule to show you. Example : 4 + 8. You can other rules if you want */
        $.validator.methods.operation = function(value, element, param) {
            return value == param;
        };
        $('.form-validation').each(function(){
            var formValidation = $(this).validate({
                success: "valid",
                submitHandler: function() { alert("Form is valid! We submit it") },
                errorClass: "form-error",
                validClass: "form-success",
                errorElement: "div",
                ignore: [],
                rules: {       
                    avatar: {extension:"jpg|png|gif|jpeg|doc|docx|pdf|xls|rar|zip"},
                    password2: {equalTo: '#password'},
                    calcul: {operation: 12},
                    url: {url: true}
                },
                messages:{
                    name: {required: 'Enter your name'},
                    lastname: {required: 'Enter your last name'},
                    firstname: {required: 'Enter your first name'},
                    email: {required: 'Enter email address', email: 'Enter a valid email address'},
                    language: {required: 'Enter your language'},
                    mobile: {required: 'Enter your phone number'},
                    avatar: {required: 'You must upload your avatar'},
                    password: {required: 'Write your password'},
                    password2: {required: 'Write your password',equalTo: '2 passwords must be the same'},
                    calcul: {required: 'Enter the result of 4 + 8',operation: 'Result is false. Try again!'},
                    terms: {required: 'You must agree with terms'}
                },
                highlight: function(element, errorClass, validClass) {
                    $(element).closest('.form-control').addClass(errorClass).removeClass(validClass);
                },
                unhighlight: function(element, errorClass, validClass) {
                    $(element).closest('.form-control').removeClass(errorClass).addClass(validClass);
                },
                errorPlacement: function(error, element) {
                   if (element.hasClass("custom-file") || element.hasClass("checkbox-type") || element.hasClass("language")) {
                        element.closest('.option-group').after(error);
                   }
                   else if (element.is(":radio") || element.is(":checkbox"))  {
                        element.closest('.option-group').after(error);
                   }
                   else if (element.parent().hasClass('input-group'))  {
                        element.parent().after(error);
                   }
                   else{
                       error.insertAfter(element);
                   }
                },
                invalidHandler: function(event, validator) {
                    var errors = validator.numberOfInvalids();            
                    adjustMaincontentHeight(50);  
                }      
            });
            $(".form-validation .cancel").click(function() {
                formValidation.resetForm();
            });
        });
    }
}

