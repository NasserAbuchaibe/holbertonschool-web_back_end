export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const original = this;
    return Object.assign(Object.create(Object.getPrototypeOf(original)), {
      _brand: undefined,
      _motor: undefined,
      _color: undefined,
    });
  }
}
