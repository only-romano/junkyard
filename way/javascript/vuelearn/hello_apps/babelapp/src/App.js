class User {
  constructor(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }

  get fullName() {
    return `${this.firstName} ${this.lastName}`;
  }
};

export default {
  name: 'app',
  data () {
    return {
      user: new User('Sergey', 'Romanov')
    }
  }
}