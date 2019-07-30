def wins(board, x, y, player, left, dx, dy)
  if (x > 3) or (x < 0) or (y < 0) or (y > 3)
    if left == 0
      return player
    else
      return false
    end
  elsif board[y][x] == player or board[y][x] == 'T'
    return wins(board, x + dx, y + dy, player, left - 1, dx, dy)
  else
    return false
  end
end

T = gets.chomp.to_i

T.times do |i|
  board = []
  4.times do |x|
    board << gets.chomp.split("")
  end
  gets

  res = false
  board.each_with_index do |row, y|
    row.each_with_index do |player, x|
      if (player == 'T') or (player == '.')
        next
      end
      for dx in -1..1
        for dy in -1..1
          if (dx == 0) and (dy == 0)
            next
          end
          res ||= wins(board, x, y, player, 4, dx, dy)
        end
      end
    end
  end

  if res
    puts "Case ##{i+1}: #{res} won"
  else
    completed = true
    board.each do |row|
      completed &&= row.all? { |n| n != '.' }
    end
    if completed
      puts "Case ##{i+1}: Draw"
    else
      puts "Case ##{i+1}: Game has not completed"
    end
  end

end
