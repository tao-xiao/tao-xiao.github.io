# Compatibility patch for Ruby 3.2+ / 4.0+ 
# Some older gems (like Liquid 4) use .tainted?, which was removed in Ruby 3.2.

puts "--- Loading Ruby Compatibility Patch for tainted? ---"

class Object
  unless method_defined?(:tainted?)
    def tainted?
      false
    end
  end
  
  unless method_defined?(:taint)
    def taint
      self
    end
  end
  
  unless method_defined?(:untaint)
    def untaint
      self
    end
  end
end

puts "--- Patch Loaded Successfully ---"
