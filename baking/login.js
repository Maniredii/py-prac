import React, { useState } from 'react';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  return (
    <div>
      <h1>Login</h1>
      <input type='text' placeholder='Username' value={username} onChange={(e) => setUsername(e.target.value)} />\n      <input type='password' placeholder='Password' value={password} onChange={(e) => setPassword(e.target.value)} />\n      <button onClick={() => alert(`Login with: ${username}, ${password}`)}>Login</button>
    </div>
  );
};

export default Login;