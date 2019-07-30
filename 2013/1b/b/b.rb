T = gets.chomp.to_i

T.times do |t|
  r, paint = gets.chomp.split.map(&:to_i)
  max = 0
  while true
    curr_area =  r * r  # units of pi
    next_area = (r + 1) * (r + 1)
    if paint < next_area - curr_area
      break
    else
      paint -= next_area - curr_area
      curr_area = next_area
      max += 1
      r += 2
    end
  end

  puts "Case ##{t+1}: #{max}"
end
