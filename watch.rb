# To use this script:
#   gem install listen
#   gem install colorize
#
# then
#
#   ruby watch.rb [path]
#
# [path] defaults to ".git"
#

require 'listen'
require 'colorize'

folder = ARGV.first || '.git'
COLORS = { added: :green, modified: :yellow, removed: :red }

def emit(action, files)
  return if files.empty?

  puts "#{action.to_s.capitalize}:"

  files.map { |f| f.sub(/^.git\//,'')}.each do |path|
    puts "     #{path.colorize(COLORS[action])}"
  end

end
listener = Listen.to(folder, relative: true, ignore: /logs/) do |modified, added, removed|
  emit(:added, added)
  emit(:modified, modified)
  emit(:removed, removed)
  puts "-" * 40
  puts
end

puts "Watching #{folder}"
puts "Press CTRL-C to stop.\n"

listener.start
sleep
