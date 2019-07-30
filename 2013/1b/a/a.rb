T = gets.chomp.to_i

T.times do |t|
  a, n = gets.chomp.split.map(&:to_i)
  others = gets.chomp.split.map(&:to_i).sort!
  ops = 0
  i = 0
  start = -1
  while i < n
    o = others[i]
    if a > o
      a += o
      i += 1
    else
      temp_ops = 0
      while i < n
        if a > o
          a += o
          i += 1
          ops += temp_ops
        else
          a += a - 1
          temp_ops += 1
        end
      end
    end
  end

  puts "Case ##{t+1}: #{ops}"
end
