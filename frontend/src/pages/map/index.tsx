import { MapContainer, TileLayer } from "react-leaflet";
import "leaflet/dist/leaflet.css";

export default function MapPage() {
  return (
    <div>
      <MapContainer center={[54.39, -0.937]} zoom={12} style={{ width: "900px", maxWidth: "100vw", minHeight: "600px" }}>
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
      </MapContainer>
    </div>
  );
}
