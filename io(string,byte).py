import io

text_stream = io.StringIO("Hello, world!")

print(text_stream.read()) 

# Write to StringIO
text_stream.write(" More text.")
text_stream.seek(0) 
print(text_stream.read()) 

text_stream.close()


#example 2:

from io import BytesIO

b = BytesIO(b"Hello, world!")
# Read from it
print(b.read())
b.write(b" Goodbye!")

b.seek(0)
print(b.read())

#example 3:

b = bytes([72, 101, 108, 108, 111])
print(b) 

#example 4:

data = bytearray(b"Hello, world!")
mv = memoryview(data)
print(mv[0:5].tobytes())
