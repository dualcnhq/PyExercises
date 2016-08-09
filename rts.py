# Remote Toggle Switch Python code

print 'Remote Toggle Switch Python code'
print '\nTest Case Input'

t = input('Input a desired number of test cases: ')
N = []
K = []

print ''
for x in range(0, t, 1):
  n, k = map(int, raw_input('Input two integers: ').split())

  # Collecting test case inputs to list
  N.insert(x, n)
  K.insert(x, k)

print '\nTest Case Output:'

for y in range(0, t, 1):
  if ((((1 << N[y]) -1) & K[y]) == ((1 << N[y]) -1)):
    # Display test case # and indicate the state of the light bulb
    print 'Case #%d: ON' % (y+1)

  else:
    print 'Case #%d: OFF' % (y+1)



