const chatbotMessages = document.getElementById('chatbot-messages');
const chatbotInput = document.getElementById('chatbot-input');
const chatbotSubmit = document.getElementById('chatbot-submit');

chatbotSend.addEventListener('click', () => {
    const userMessage = chatbotInput.value;
    if (userMessage) {
        addMessage('user', userMessage);
        chatbotInput.value = '';

        setTimeout(() => {
            addMessage('bot', 'Doporučujeme vám produkt...')
        }, 1000);
    }
});

function addMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.innerHTML = message;
    chatbotMessages.appendChild(messageElement);
    chatbotMessages,scrollTop = chatbotMessages.scrollHeight;
}

const userId = 1;
fetch('http://127.0.0.1:5000/recommend', {
    method: 'POST',
    headers: {
        'content-Type': 'application/json',
    },
    body: JSON.stringify({ user_id: userId}),
})
.then(response => response.json())
.then(data => {
    console.log('Doporučené produkty:', data.recommendations);
});