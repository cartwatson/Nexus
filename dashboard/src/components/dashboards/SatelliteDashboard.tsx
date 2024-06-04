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
        // query api
        const response = await fetch('http://localhost:5000/track-satellite');
        const data = await response.json();

        // validate data
        if (data.Success && Array.isArray(data.Data)) {
          setSatellites(data.Data);
        } else {
          console.log("Received data is not formatted correct.", data);
        }
        setLoading(false);

      } catch (error) {
        console.error('Error fetching satellites:', error);
        setLoading(false);
      }
    };

    fetchSatellites();
  }, []);

  const handleRequestImage = async (id: string) => {
    console.log('Requesting image for Satellite ID:', id);
    try {
      const response = await fetch(`http://localhost:5000/request-image?id=${id}`);
      console.log(response);
      const data = await response.json();
      if (data.Success) {
        // TODO: Send toast 
      }
    } catch (error) {
      console.error(`Error requesting image of satellite with name ${id}:`, error);
    }
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
              onRequestImage={() => handleRequestImage(satellite.id)}
            />
          ))}
        </div>
      )}
    </div>
  );
};

export default SatelliteTrackingDashboard;
