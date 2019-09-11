#!/usr/bin/env ruby
require 'digest'

prefix = ARGV[0]
difficulty = ARGV[1].to_i()
zeros = '0' * difficulty

def hex2bin(hex)
  hex.hex.to_s(2).rjust(hex.size*4, '0')
end

i = 0
digest = ''
until hex2bin(digest).start_with?(zeros) do
  digest = Digest::SHA256.hexdigest prefix + i.to_s()
  i += 1
end
p i
