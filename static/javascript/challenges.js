function acceptChallenge(challengeId) {
    fetch('/accept_challenge', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            challenge_id: challengeId
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        const button = document.querySelector(`button[onclick="acceptChallenge(${challengeId})"]`);
        button.textContent = 'Accepted';
        button.disabled = true;
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while accepting the challenge.');
    });
}
