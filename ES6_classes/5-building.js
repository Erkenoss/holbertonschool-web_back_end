export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building && !this.evacuationWarningMessage) {
      throw Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = Building.valnumber(sqft, 'Sqft');
  }

  get sqft() {
    return this._sqft;
  }

  static valnumber(value, propertyName) {
    if (typeof value ==! 'number') {
      throw new TypeError(`${propertyName} Must be a number`);
    }
    return value;
  }
}
