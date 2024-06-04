import React from 'react';
import { Card, Button, Image } from 'antd';
import { SatelliteCardProps } from 'types/satellite';
import noImageFound from '../../../assets/no-image-found.png'

const SatelliteCard: React.FC<SatelliteCardProps> = ({ satellite, onRequestImage }) => {
  return (
    <Card
      title={satellite.name || satellite.id || "Unknown"}
      style={{ width: 300, margin: 16, flex: '0 0 300px', minHeight: 400 }}
      actions={[
        <Button key="request" onClick={() => onRequestImage(satellite.id)}>Request Image</Button>
      ]}
    >
      <Image
        style={{ width: '100%', height: 'auto' }}
        src={satellite.imageUrl || noImageFound }
        alt={satellite.name}
        fallback={noImageFound}
      />
      <p>ID: {satellite.id}</p>
      <p>Altitude: {satellite.altitude !== null ? `${satellite.altitude} km` : "Unknown"}</p>
      <p>Velocity: {satellite.velocity !== null ? `${satellite.velocity} km/h` : "Unknown"}</p>
    </Card>
  );
};

export default SatelliteCard;
