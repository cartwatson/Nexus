import React, { useState, useEffect } from 'react';
import { List, Spin } from 'antd';
import { Satellite } from '../../types/satellite';
import SatelliteCard from './dash-components/SatelliteCard'; 

const SatelliteTrackingDashboard: React.FC = () => {
  const [loading, setLoading] = useState<boolean>(true);
  const [satellites, setSatellites] = useState<Satellite[]>([]);

  useEffect(() => {
    // Fetch satellite data from the API or mock data
    const fetchSatellites = async () => {
      setLoading(true);
      try {
        // Example: Fetch satellites from an API
        // const response = await fetch('api/satellites');
        // const data = await response.json();
        // setSatellites(data);

        // Example: Mock data
        const mockSatellites: Satellite[] = [
          { id: "1", name: 'Satellite 1', altitude: 500, velocity: 10000 },
          { id: "2", name: 'Satellite 2', altitude: 600, velocity: 11000 },
          // Add more mock satellites as needed
        ];
        setSatellites(mockSatellites);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching satellites:', error);
        setLoading(false);
      }
    };

    fetchSatellites();
  }, []);

  const handleRequestImage = (id: string) => {
    console.log('Requesting image for Satellite ID:', id);
    // TODO: Add logic to request an image here
  };

  return (
    <div>
      <h1>Satellite Tracking Dashboard</h1>
      {loading ? (
        <Spin size="large" />
      ) : (
        <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'left' }}>
          {satellites.map(satellite => (
            <SatelliteCard 
              key={satellite.id}
              satellite={satellite}
              onRequestImage={handleRequestImage}
            />
          ))}
        </div>
      )}
    </div>
  );
};

export default SatelliteTrackingDashboard;
