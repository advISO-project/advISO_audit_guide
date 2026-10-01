document.addEventListener("DOMContentLoaded", function() {
    // Handle the Next button
    var nextBtn = document.querySelector('.rst-footer-buttons .btn-neutral.float-right');
    if (nextBtn) {
        // Read the actual page title stored in the element's title attribute
        var pageTitle = nextBtn.getAttribute('title');
        if (pageTitle) {
            // Keep the arrow icon if present, but replace "Next" with the title
            var icon = nextBtn.querySelector('span');
            var iconHtml = icon ? icon.outerHTML : ' &rarr;';
            
            nextBtn.innerHTML = pageTitle + ' ' + iconHtml;
        }
    }

    // Handle the Previous button
    var prevBtn = document.querySelector('.rst-footer-buttons .btn-neutral.float-left');
    if (prevBtn) {
        var pageTitle = prevBtn.getAttribute('title');
        if (pageTitle) {
            var icon = prevBtn.querySelector('span');
            var iconHtml = icon ? icon.outerHTML : '&larr; ';
            
            prevBtn.innerHTML = iconHtml + ' ' + pageTitle;
        }
    }
});