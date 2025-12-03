// DOM Elements
const chatMessages = document.getElementById('chatMessages');
const userInput = document.getElementById('userInput');
const sendButton = document.getElementById('sendButton');
const quickRepliesContainer = document.getElementById('quickReplies');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    loadQuickReplies();
    setupEventListeners();
});

// Event Listeners
function setupEventListeners() {
    sendButton.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
}

// Load Quick Replies
async function loadQuickReplies() {
    try {
        const response = await fetch('/quick-replies');
        const data = await response.json();

        if (data.success) {
            quickRepliesContainer.innerHTML = '';
            data.replies.forEach(reply => {
                const button = document.createElement('button');
                button.className = 'quick-reply-btn';
                button.textContent = reply;
                button.addEventListener('click', () => {
                    userInput.value = reply;
                    sendMessage();
                });
                quickRepliesContainer.appendChild(button);
            });
        }
    } catch (error) {
        console.error('Error loading quick replies:', error);
    }
}

// Send Message
async function sendMessage() {
    const message = userInput.value.trim();

    if (!message) return;

    // Add user message to chat
    addMessage(message, 'user');

    // Clear input
    userInput.value = '';

    // Disable send button
    sendButton.disabled = true;

    // Show typing indicator
    const typingId = showTypingIndicator();

    try {
        // Send to backend
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

        // Remove typing indicator
        removeTypingIndicator(typingId);

        // Add bot response
        if (data.success) {
            addMessage(data.message, 'bot');
        } else {
            addMessage('Sorry, something went wrong. Please try again.', 'bot');
        }

    } catch (error) {
        console.error('Error sending message:', error);
        removeTypingIndicator(typingId);
        addMessage('Sorry, I encountered an error. Please try again.', 'bot');
    } finally {
        // Re-enable send button
        sendButton.disabled = false;
        userInput.focus();
    }
}

// Add Message to Chat
function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;

    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';

    // Format message with markdown-like syntax
    const formattedText = formatMessage(text);
    contentDiv.innerHTML = formattedText;

    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);

    // Scroll to bottom with smooth animation
    setTimeout(() => {
        chatMessages.scrollTo({
            top: chatMessages.scrollHeight,
            behavior: 'smooth'
        });
    }, 100);
}

// Format Message
function formatMessage(text) {
    // Convert **text** to bold
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

    // Convert line breaks to <br>
    text = text.replace(/\n/g, '<br>');

    // Convert bullet points
    text = text.replace(/•/g, '<span style="color: #ffd700;">•</span>');

    return text;
}

// Show Typing Indicator
function showTypingIndicator() {
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot-message';
    typingDiv.id = 'typing-indicator';

    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content typing-indicator';

    for (let i = 0; i < 3; i++) {
        const dot = document.createElement('div');
        dot.className = 'typing-dot';
        contentDiv.appendChild(dot);
    }

    typingDiv.appendChild(contentDiv);
    chatMessages.appendChild(typingDiv);

    chatMessages.scrollTo({
        top: chatMessages.scrollHeight,
        behavior: 'smooth'
    });

    return 'typing-indicator';
}

// Remove Typing Indicator
function removeTypingIndicator(id) {
    const indicator = document.getElementById(id);
    if (indicator) {
        indicator.remove();
    }
}

// Focus input on load
userInput.focus();
