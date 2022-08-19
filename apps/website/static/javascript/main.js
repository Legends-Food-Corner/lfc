window.onload = onBodyLoad;

function setOfferOfDayModal(state) {
    let s = state == true ? 'show' : 'hide';
    $('#modal-offer-of-day').modal(s)
}

function hideTopAnnouncement() {
    hide('top-announcement-container');
}

function onBodyLoad() {
    setOfferOfDayModal(true);
}

window.onscroll = () => {
    if (document.body.scrollTop > 100) {
        document.getElementById("btn-scroll-to-top").style.display = "block";
    }
    else {
        document.getElementById("btn-scroll-to-top").style.display = "none";
    }
}