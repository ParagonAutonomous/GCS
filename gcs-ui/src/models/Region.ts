import { Coordinate } from "./Coordinate";

export class Region {
  name: string;
  coordinates: Coordinate[];

  constructor(name: string, coordinates: Coordinate[]) {
    this.name = name;
    this.coordinates = coordinates;
  }

  toString(): string {
    return `Region(name=${this.name}, coordinates=[${this.coordinates.map(coord => coord.toString()).join(", ")}])`;
  }
}