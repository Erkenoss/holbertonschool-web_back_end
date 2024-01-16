/* eslint desable */
import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = Pricing.valnumber(amount, 'Amount');
    this._currency = Pricing.classtest(currency, Currency, 'Currency');
  }

  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }

  set amount(newAmount) {
    this._amount = Pricing.valnumber(newAmount, 'Amount');
  }

  set currency(newCurrency) {
    this._currency = Pricing.classtest(newCurrency, Currency, 'Currency');
  }

  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, convertRate) {
    return amount * convertRate;
  }

  static valnumber(value, propertyName) {
    if (typeof value !== 'number') {
      throw new TypeError(`${propertyName} Must be a number`)
    }
    return value;
  }

  static classtest(value, classType, propertyName) {
    if (value instanceof classType) {
      return value;
    } else {
    throw new TypeError(`${classType.name} expected for ${propertyName}`);
    }
  }
}
