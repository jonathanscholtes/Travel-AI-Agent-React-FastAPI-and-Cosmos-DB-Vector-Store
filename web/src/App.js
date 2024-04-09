import * as React from 'react';
import { Routes, Route } from 'react-router-dom';
import Main from './Main';

export default function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Main />} />

      </Routes>
    </div>
  );
}
