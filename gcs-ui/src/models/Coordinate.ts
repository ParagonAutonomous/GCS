export class Coordinate {
  lat: number;
  long: number;
  
  constructor(lat: number, long: number) {
    this.lat = lat;
    this.long = long;
  }
  
  toString(): string {
    return `Coordinate(lat=${this.lat}, long=${this.long})`;
  }
}