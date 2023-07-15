let signup = document.querySelector(".signup");
let login = document.querySelector(".login");
let slider = document.querySelector(".slider");
let formSection = document.querySelector(".form-section");

login.addEventListener("click", () => {
    slider.classList.remove("moveslider");
    formSection.classList.remove("form-section-move");
});

document.getElementById('login-submit').addEventListener('click', function (event) {
    // Prevent the form from submitting the traditional way
    event.preventDefault();

    var username = document.querySelector('.login-box .username').value;
    var password = document.querySelector('.login-box .password').value;

    // Create a FormData object
    var login_data = {}
    login_data.username = username;
    login_data.password = password;

    // Send an HTTP request with fetch
    fetch('http://127.0.0.1:8000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(login_data),
    })
        .then(response => {
            if (!response.ok) {
                alert('Error: Login failed');
                throw new Error('Login failed!');
            }
            return response.json()
        }) // assuming the response is JSON
        .then(data => {
            if (data) {
                window.location.href = "http://127.0.0.1:5500/chat/index.html";
            } else {
                alert('Error: Login failed'); // handle login failure
            }
        })
        .catch(error => {
            console.error('Error:', error); // handle any errors
        });
});
