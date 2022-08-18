window.onload = onBodyLoad;

function hideTopAnnouncement() {
    hide('top-announcement-container');
}

function onBodyLoad() {
    $('#modal-offer-of-day').modal('show')
}

window.onscroll = () => {
    if (document.body.scrollTop > 100) {
        document.getElementById("btn-scroll-to-top").style.display = "block";
    }
    else {
        document.getElementById("btn-scroll-to-top").style.display = "none";
    }
}