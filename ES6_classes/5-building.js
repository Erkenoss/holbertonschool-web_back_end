export default class Building {
  constructor(sqft) {
    this._sqft = Building.valnumber(sqft, 'Sqft');
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }

  static valnumber(value, propertyName) {
    if (typeof value ==! 'number') {
      throw new TypeError(`${propertyName} Must be a number`);
    }
    return value;
  }
}
