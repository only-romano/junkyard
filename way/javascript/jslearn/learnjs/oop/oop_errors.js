var json = {"name": "Vasily", "age": 30};

function CustomError(message) {
  this.name = "Custom Error";
  this.message = message;
    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, this.constructor);
    } else {
      this.stack = (new Error()).stack;
    }
}

CustomError.prototype = Object.create(Error.prototype);
CustomError.prototype.constructor = CustomError;

function PropertyError(property) {
  CustomError.call(this, "Error in property " + property);
    this.name = "Property Error";
    this.property = property;
}

PropertyError.prototype = Object.create(CustomError.prototype);
PropertyError.prototype.constructor = PropertyError;

function readUser(data) {
  var user = JSON.parse(data);
    if (!user.age) {
      throw new PropertyError("age");
    }
    if (!user.name) {
      throw new PropertyError("name");
    }

    return user;
}

try {
  var user = readUser('{ "age": 25 }');
} catch (err) {
  if (err instanceof PropertyError) {
    if (err.property == 'name') {
      console.log( 'Hello, anonymous!' );
    } else {
      console.log( err.message );
    }
  } else if (err instanceof SyntaxError) {
    console.log( 'Data syntax error: ' + err.message );
  } else {
    throw err;
  }
}

function PropertyRequiredError(property) {
  PropertyError.apply(this, arguments);
  this.name = 'PropertyRequiredError';
  this.message = 'Missing property: ' + property;
}

PropertyRequiredError.prototype = Object.create(PropertyError.prototype);
PropertyRequiredError.prototype.constructor = PropertyRequiredError;

var err = new PropertyRequiredError('age');
console.log( err instanceof PropertyRequiredError );
console.log( err instanceof PropertyError );
console.log( err instanceof CustomError );
console.log( err instanceof Error );


function FormatError(property) {
  this.name = 'FormatError';
  this.message = property;
    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, this.constructor);
    } else {
      this.stack = (new Error()).stack;
    }
}

FormatError.prototype = Object.create(SyntaxError.prototype);
FormatError.prototype.constructor = FormatError;

var errF = new FormatError('Formatting error');
console.log( errF.message );
console.log( errF.name );
console.log( errF.stack );
console.log( errF instanceof SyntaxError );