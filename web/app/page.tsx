"use client"

import React, { useState } from 'react';

export default function Home() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');

  const sendQuery = async () => {
      try {
          const res = await fetch('http://localhost:8000/chat', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({ query }),
          });

          if (!res.ok) {
              throw new Error(`Error: ${res.status}`);
          }

          const data = await res.json();
          setResponse(data.response);
      } catch (error) {
          console.error("Failed to fetch:", error);
      }
  };


    return (
        <div className="container w-full justify-center items-center mx-auto p-4">
          <h1 className='mb-8'>好奇的黑猫</h1>
            <div className="mb-4">
                <input 
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    className="border p-2 rounded w-full"
                    placeholder="喵~"
                />
            </div>
            <div className="mb-4">
                <button 
                    onClick={sendQuery}
                    className="bg-blue-500 text-white p-2 rounded"
                >
                    Send
                </button>
            </div>
            <div className="response">
                <p>Response: {response}</p>
            </div>
        </div>
    );
}
