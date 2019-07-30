def check(lawn, h, x, y)
  possible = true
  $m.times do |x0|
    possible &&= h >= lawn[y][x0]
  end
  return possible if possible

  possible = true
  $n.times do |y0|
    possible &&= h >= lawn[y0][x]
  end
  return possible

end

T = gets.chomp.to_i

T.times do |t|
  $n, $m = gets.chomp.split.map &:to_i
  lawn = Array.new
  $n.times do |i|
    lawn << gets.chomp.split.map(&:to_i)
  end

  possible = true
  lawn.each_with_index do |row, y|
    row.each_with_index do |h, x|
      if not check(lawn, h, x, y)
        possible = false
      end
      if not possible
        break
      end
    end
    if not possible
      break
    end
  end
  puts (possible ? "Case ##{t+1}: YES" : "Case ##{t+1}: NO")

end
