document.getElementById("add-friend-form").addEventListener("submit", async function(event) {
    event.preventDefault();
    const user_id = document.getElementById("user_id").value;
    const friend_user_id = document.getElementById("friend_user_id").value;
    const relationship_type = document.getElementById("relationship_type").value;
    const response = await fetch('/add_friend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user_id: user_id,
            friend_user_id: friend_user_id,
            relationship_type: relationship_type
        })
    });
    const result = await response.json();
    alert(result.message);
});
function cancelAdd() {
    document.getElementById("add-friend-form").reset();
}