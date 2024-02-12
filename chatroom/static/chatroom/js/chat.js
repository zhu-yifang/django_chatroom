document.addEventListener('DOMContentLoaded', function () {
    const roomId = document.getElementById('chat-data').dataset.roomId;
    // Connect to websocket
    const chatSocket = new WebSocket(
        'wss://' + window.location.host + '/ws/chat/' + roomId + '/'
    );
    // Receive message from websocket
    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        const chatLog = document.querySelector('#chat-log');
        const newMessage = document.createElement('li');
        newMessage.innerHTML = `<strong>${data.username}</strong>: ${data.message} <small class="text-muted">${data.timestamp}</small>`;
        chatLog.appendChild(newMessage);
        // Print message to console
        console.log('message received: ' + data.message);
    };

    // Handle errors
    chatSocket.onclose = function (e) {
        console.error('Chat socket closed unexpectedly');
    };

    const messageInputDom = document.querySelector('#chat-message-input');
    const sendMessage = function () {
        const message = messageInputDom.value;
        chatSocket.send(JSON.stringify({ 'message': message }));
        console.log('message sent: ' + message);
        messageInputDom.value = '';
    };

    // Send message when button is clicked
    document.querySelector('#chat-message-submit').onclick = function (e) {
        sendMessage();
    };

    // Send message when Enter key is pressed
    messageInputDom.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            e.preventDefault(); // Prevent default Enter key behavior (like submitting a form)
            sendMessage();
        }
    });
});