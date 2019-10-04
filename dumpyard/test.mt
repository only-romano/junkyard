class File {
  private var fname
  private var line = 1
  
  fn isinit() {
    return fname != null
  }
  
  fn read() {
    if(!isinit()) Std.error("I/O operation on closed file")
    return Std.fread(fname)
  }
  
  fn readline(n) {
    if(!isinit()) Std.error("I/O operation on closed file")
    if(!n) { n = line; line += 1 }
    n = Int(n)
    var data = read()
    var lines = data.split("\n")
    if(n > lines.length) return null
    return lines[n-1]
  }
  
  fn write(data="") {
    if(!isinit()) Std.error("I/O operation on closed file")
    Std.fwrite(fname, String(data))
  }
  
  fn append(data="\n") {
    if(!isinit()) Std.error("I/O operation on closed file")
    var old = read()
    write(old+String(data))
  }
  
  fn close() {
    line = 1
    fname = null
  }
  
  
  fn init(filename) {
    fname = String(filename)
  }
  fn deinit() {
    line = 1
    fname = null
  }
}

fn open(fname) {
  return File(fname);
}


fn main() {
  var f = open("test.txt")
  f.write()
  var data = "Aloha!
hozy hehs
omf fucj".split("\n")
  for(var n in data) f.append(n+"\n")
  var line = f.readline()
  repeat {
    Std.print(line)
    line = f.readline()
  } while(line != null)
  f.close()
}