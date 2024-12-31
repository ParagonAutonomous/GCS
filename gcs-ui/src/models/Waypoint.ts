import { Coordinate } from "./Coordinate";

export class Waypoint extends Coordinate {
  alt: number;

  constructor(lat: number, long: number, alt: number) {
    super(lat, long);
    this.alt = alt;
  }

  toString(): string {
    return `Waypoint(lat=${this.lat}, long=${this.long}, alt=${this.alt})`;
  }
}