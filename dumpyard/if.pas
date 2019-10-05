var a, b: integer;

begin
  writeln('Введите а:');
  readln(a);

  writeln('Введите b:');
  readln(b);

  if (a > b) then
  begin
    writeln('a больше b на ', a - b);
  end else if (a < b) then
  begin
    writeln('a меньше b на ', b - a);
  end else
  begin
    writeln('a равно b');
  end;

end.