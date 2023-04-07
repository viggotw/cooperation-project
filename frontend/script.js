const button = document.querySelector('button');
button.addEventListener('click', async () => {
    try {
        const response = await fetch('http://localhost:5000/api/hello', {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const data = await response.json();
        console.log('Received response:', data);
        document.querySelector('#result').textContent = `${data.message}\nN=${data.N}`;
    } catch (error) {
        console.error('Error:', error);
    }
});