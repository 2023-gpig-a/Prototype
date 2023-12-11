import { StrictMode } from 'react'
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import './App.css'
import HomePage from './pages/home';
import MapPage from './pages/map';

const router = createBrowserRouter([
  {
    path: "/",
    element: <HomePage />,
  }, {
    path: "/map",
    element: <MapPage />,
  }
]);

function App() {
  return (
    <>
      <StrictMode>
        <RouterProvider router={router} />
      </StrictMode>
    </>
  )
}

export default App
