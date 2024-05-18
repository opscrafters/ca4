document.addEventListener('DOMContentLoaded', () => {
    fetch('http://localhost:5000/api/data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('data').innerText = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
