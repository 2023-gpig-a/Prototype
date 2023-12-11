import { Link } from "react-router-dom";

export default function HomePage() {
  return (
    <div>
      <h1>GPIG Demo</h1>
      <Link to="/map">Map</Link>
    </div>
  )
}