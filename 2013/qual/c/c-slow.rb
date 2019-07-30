class Fixnum
  def is_sq?
    s = Math.sqrt(self)
    s == s.to_i
  end
  def is_palindrome?
    s = self.to_s
    s.reverse == s
  end
  def is_fair_and_sq?
    s = Math.sqrt(self).to_i
    (s * s == self) and (self.is_palindrome?) and (s.is_palindrome?)
  end
end

T = gets.chomp.to_i
T.times do |t|
  a, b = gets.chomp.split.map &:to_i
  fair_and_sqs = 0
  (a..b).each do |x|
    if x.is_fair_and_sq?
      fair_and_sqs += 1
    end
  end
  puts "Case ##{t+1}: #{fair_and_sqs}"
end
