import { Region } from "./Region";
import { Waypoint } from "./Waypoint";

export class FlightPath {
  name: string;
  region: Region;
  waypoints: Waypoint[];

  constructor(name: string, region: Region, waypoints: Waypoint[]) {
    this.name = name;
    this.region = region;
    this.waypoints = waypoints;
  }

  toString(): string {
    return `FlightPath(name=${this.name}, region=${this.region.name}, waypoints=[${this.waypoints.map(wp => wp.toString()).join(", ")}])`;
  }
}