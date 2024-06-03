export interface Satellite {
  id: string; //UUID
  name: string;
  altitude: number;
  velocity: number;
  // latitude: number;
  // longitude: number;
  // status: enum;
  // lastContactTime: time;
  imageUrl?: string;
}

export type SatelliteCardProps = {
  satellite: Satellite;
  onRequestImage: (id: string) => void;  // Assuming id is needed to request image
}
