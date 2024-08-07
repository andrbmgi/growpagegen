document.addEventListener('DOMContentLoaded', () => {
    const graphDiv = document.getElementById('graph');
    const hoverImage = document.getElementById('hover-image');
    const imagesFolder = 'images/';  // Folder where images are stored
    var imageTimestamps = null;
    var imageDates = null;
    fetch('content.json').then(response => response.json()).then(data => {
        imageTimestamps = data;
        console.log(imageTimestamps);
        imageDates = imageTimestamps.map(ts => new Date(ts));
    });

    window.initializeHoverFunctionality = function() {
        graphDiv.on('plotly_hover', (data) => {
            const hoverTime = new Date(data.points[0].x);
            const closestImage = getClosestImage(hoverTime, imageDates);

            if (closestImage) {
                hoverImage.src = `${imagesFolder}${closestImage}.jpg`;
                hoverImage.style.left = `${data.event.pageX + 10}px`;
                hoverImage.style.top = `${data.event.pageY + 10}px`;
                hoverImage.style.display = 'block';
                console.log(hoverImage.src);
            } else {
                hoverImage.style.display = 'none';
            }
        });

        graphDiv.on('plotly_unhover', () => {
            hoverImage.style.display = 'none';
        });
    }

    function getClosestImage(hoverTime, imageDates) {
        // find the index of the closest date to the hover time
        const closestIndex = imageDates.reduce((closestIndex, currentDate, currentIndex) => {
            const closestTime = imageDates[closestIndex];
            const currentTime = currentDate;
            return Math.abs(currentTime - hoverTime) < Math.abs(closestTime - hoverTime) ? currentIndex : closestIndex;
        }, 0);

        return imageTimestamps[closestIndex];
    }
});