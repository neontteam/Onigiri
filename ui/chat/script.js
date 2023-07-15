// Get necessary DOM elements
const chatContainer = document.querySelector('.chat-container');
const inputField = document.querySelector('.input-field');
const sendIcon = document.querySelector('.send-icon');
const uploadIcon = document.querySelector('.upload-icon');

// Function to handle sending messages
function sendMessage() {
  const messageContent = inputField.value;
  if (messageContent.trim() === '') {
    return;
  }

  const message = document.createElement('div');
  message.classList.add('message');

  const sender = document.createElement('span');
  sender.classList.add('sender');
  sender.textContent = 'You';

  const content = document.createElement('div');
  content.classList.add('content');
  content.textContent = messageContent;

  message.appendChild(sender);
  message.appendChild(content);

  chatContainer.appendChild(message);

  // Clear input field
  inputField.value = '';

  // Scroll to the bottom of the chat container
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Event listener for sending message on Enter key press
inputField.addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
    event.preventDefault();
    sendMessage();
  }
});

// Event listener for sending message on button click
sendIcon.addEventListener('click', sendMessage);

// Event listener for uploading files
uploadIcon.addEventListener('click', function() {
  // Handle file upload logic here
  console.log('File upload clicked');
});
