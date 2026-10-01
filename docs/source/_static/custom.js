// _static/js/custom_footer.js
document.addEventListener("DOMContentLoaded", function() {
    // Target the Next button
    var nextBtn = document.querySelector('.rst-footer-buttons .btn-neutral.float-right');
    if (nextBtn) {
        // Extract the title text (the anchor text inside the button)
        var nextLink = nextBtn.querySelector('a');
        if (nextLink) {
            var titleText = nextLink.textContent.trim();
            // Prepend "Next: " to the title
            nextLink.innerHTML = "Next: " + titleText + " &rarr;";
        }
    }

    // Target the Previous button
    var prevBtn = document.querySelector('.rst-footer-buttons .btn-neutral.float-left');
    if (prevBtn) {
        var prevLink = prevBtn.querySelector('a');
        if (prevLink) {
            var titleText = prevLink.textContent.trim();
            // Prepend "Previous: " to the title
            prevLink.innerHTML = "&larr; Previous: " + titleText;
        }
    }
});