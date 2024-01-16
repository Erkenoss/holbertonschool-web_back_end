export default class Currency {
  constructor(code, name) {
    this._code = Currency.valstring(code, 'Code');
    this._name = Currency.valstring(name, 'Name');
  }

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  set code(newCode) {
    this._code = Currency.valstring(newCode, 'Code');
  }

  set name(newName) {
    this._name = Currency.valstring(newName, 'Name');
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }

  static valstring(value, propertyName) {
    if (typeof value !== 'string') {
      throw new TypeError(`${propertyName} Must be a string`);
    }
    return value;
  }
}