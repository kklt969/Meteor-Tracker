function openModal(memberId) {
    const modal = document.getElementById('modal');
    const modalContent = document.getElementById('modalContent');

    const memberData = {
        alex: "Alex Johnson is the visionary behind our company, driving innovation and strategic growth.",
        sarah: "Sarah Lee brings creativity and passion to our marketing strategies, connecting us with our audience.",
        michael: "Michael Brown is our tech guru, developing solutions that keep us ahead of the curve.",
        emma: "Emma Davis ensures our projects are on track and run smoothly, a vital part of our team."
    };

    modalContent.innerHTML = memberData[memberId];
    modal.style.display = "block";
}

function closeModal() {
    const modal = document.getElementById('modal');
    modal.style.display = "none";
}

// Close modal when clicking outside of it
window.onclick = function(event) {
    const modal = document.getElementById('modal');
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
