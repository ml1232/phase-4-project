import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isCreatingAccount, setIsCreatingAccount] = useState(false);
  const history = useHistory();

  const handleSignIn = () => {
    // Add logic for signing in here.
    // Check username and password, and if they are correct, redirect to the welcome page.
    // Use an authentication library or your own logic for signing in.
    if (username === 'exampleUser' && password === 'examplePassword') {
      history.push('/welcome'); // Redirect to the welcome page upon successful sign-in.
    } else {
      alert('Incorrect username or password');
    }
  };

  const handleCreateAccount = () => {
    setIsCreatingAccount(true);
    // Redirect to the account creation page.
    history.push('/create-account');
  };

  const handleCancelCreateAccount = () => {
    setIsCreatingAccount(false);
  };

  const handleCreateAccountSubmit = () => {

    // Validate user input (e.g., check if username and password are not empty)

    if (!username || !password) {
      alert('Please enter a username and password');
      return;
    }
  
    // use backend API endpoint for creating accounts, you can make a POST request

    fetch('/api/create-account', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username,
        password,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          // Account creation was successful, redirect to the welcome page.
          history.push('/welcome');
        } else {
          // Account creation failed, handle the error.
          alert(data.message); // You can display an error message to the user.
        }
      })
      .catch((error) => {
        // Handle network or other errors.
        alert('An error occurred while creating the account. Please try again later.');
      });
  };
  
  return (
    <div>
      {isCreatingAccount ? (
        <div>
          <h2>Create Account</h2>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button onClick={handleCreateAccountSubmit}>Create Account</button>
          <button onClick={handleCancelCreateAccount}>Cancel</button>
        </div>
      ) : (
        <div>
          <h2>Sign In</h2>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button onClick={handleSignIn}>Sign In</button>
          <button onClick={handleCreateAccount}>Create Account</button>
        </div>
      )}
    </div>
  );
}

export default Login;
