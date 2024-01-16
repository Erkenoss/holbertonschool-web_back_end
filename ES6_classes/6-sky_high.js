/* eslint-disable */
import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = SkyHighBuilding.valnumber(floors, 'Floors');
    if (this.constructor !== SkyHighBuilding && !this.vacuationWarningMessage) {
      throw Error(`Evacuate slowly the ${this.floors} floors`);
    }
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }

  get floors() {
    return this._floors;
  }

  static valnumber(value, propertyName) {
    if (typeof value !== 'number') {
      throw new TypeError(`${propertyName} Must be a number`);
    }
    return value;
  }
}
