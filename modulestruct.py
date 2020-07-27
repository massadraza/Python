from struct import * 

# Store as bytes data
packed_data = pack('iif', 6, 15, 4.42) 
print(packed_data) 

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iiff'))

# To get byte data back to normal readable text
original_data = unpack('iif', packed_data) 
print(original_data) 
print(unpack('iif', b'\x06\x00\x00\x00\x0f\x00\x00\x00\xa4p\x8d@')) 

# Learning about struct