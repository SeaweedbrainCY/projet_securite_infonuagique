 async function registerUser() {
        const username = document.getElementById('regUsername').value;
        const password = document.getElementById('regPassword').value;

        try {
            const response = await fetch('http://api.badauth.demo.stchepinsky.net/register?username='+username+'&password='+password, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            const data = await response.json();
            document.getElementById('result').innerHTML = '<p>Registration Response:</p><pre>' + JSON.stringify(data, null, 2) + '</pre>';

        } catch (error) {
            console.error('Error:', error);
            document.getElementById('result').innerHTML = '<p>Error occurred. Check console for details.</p>';
        }
    }

    async function login() {
        const username = document.getElementById('loginUsername').value;
        const password = document.getElementById('loginPassword').value;

        try {
            const response = await fetch('http://api.badauth.demo.stchepinsky.net/token?username='+username+'&password='+password, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            const data = await response.json();

            // Store the token in a secure cookie
            document.cookie = `access_token=${data.access_token}; secure; samesite=Strict`;
            window.location.href = '/connected.html';

        } catch (error) {
            console.error('Error:', error);
            document.getElementById('resourceContent').innerText = 'Error occurred. Check console for details.';
        }
    }

    async function getProtectedResource() {
        const token = getCookie('access_token');

        if (!token) {
            document.getElementById('resourceContent').innerText = 'Token not found. Please log in.';
            return;
        }

        try {
            const response = await fetch('http://api.badauth.demo.stchepinsky.net/protected_resource', {
                method: 'GET',
                headers: {
                    'Authorization': 'Bearer ' + token,
                },
            });

            const data = await response.json();
            document.getElementById('resourceContent').innerText = data.message;

        } catch (error) {
            console.error('Error:', error);
            document.getElementById('resourceContent').innerText = 'Error occurred. Check console for details.';
        }
    }

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }

    // Load protected resource on page load
    document.addEventListener('DOMContentLoaded', getProtectedResource);