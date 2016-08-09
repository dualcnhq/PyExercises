for x in range(0, 6, 1):
  print "*" * x

for x in range(5, 0, -1):
  print "*" * x


print '\nusing function\n'

def ascendingCount(n):
  for x in range(0, n, 1):
    print "*" * x

def descendingCount(n):
  for x in range(n, 0, -1):
    print "*" * x

ascendingCount(6)
descendingCount(5)


print '\none-liner code'


def ascendingOneLinerCount(n):
  print "\n".join("*" * x for x in range(0, n, 1))

def descendingOneLinerCount(n):
  print "\n".join("*" * x for x in range(n, 0, -1))

ascendingOneLinerCount(6)
descendingOneLinerCount(5)


