'''class fib: 
 def __init__(self, max):
  self.max = max
 def __iter__(self):
  self.a = 0
  self.b = 1
  return self
 def __next__(self):
  fib = self.a
  if fib > self.max:
   raise StopIteration
  self.a, self.b = self.b, self.a + self.b
  return fib
  '''

'''exchange_rate = 1.65

# Define the initial amount in euros
euro = 1

# Print the header of the table
print(f"{'Euros':<10}{'Canadian Dollars':<15}")

# Generate the conversion table
for i in range(4):
    # Calculate the equivalent amount in Canadian dollars
    cad = euro * exchange_rate

    # Print the current row of the table
    print(f"{euro:<10} euro(s) = {cad:<15.2f} dollar(s)")

    # Update the amount in euros for the next row
    euro *= 2
    '''

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['January', 'February', 'March', 'April', 'May', 'June',
'July', 'August', 'September', 'October', 'November', 'December']

t3 = []
for i in range(len(t1)):
    t3.append(t2[i])
    t3.append(t1[i])

print(t3)