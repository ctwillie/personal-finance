import React, { useState } from "react";

export default function Welcome() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h1>Welcome</h1>

      <p>Count: {count}</p>
      <p>Click to increment</p>
      <button onClick={() => setCount((c) => c + 1)}>+</button>
    </div>
  );
}
