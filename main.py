def trial_division(n):
  L = [] # is the list that we shall add all the divisors of n
  while n % 2 == 0:
    L.append(2)
    n //= 2
  f = 3 # a possible divisor of n, also called trial divisor.
  while f ** 2 <= n:
    if n % f == 0:
      L.append(f)
      n //= f
    else:
      f += 2
  if n != 1:
    L.append(n)
  return L

# function to find φ(Ν) 
def fn_function(p, q):
  return (p - 1) * (q - 1)

n = 11413
print("n=", n)
e = 19
print("e=", e)

# function trial_division to find the factors of n (p and q)
# to calculate the φ(Ν)
pq = trial_division(n)
p = pq[0]
q = pq[1]
print("p=", p, ",q=", q)

fn = fn_function(p, q)
print("φ(Ν)=", fn)

# using fn and e (encryption key) to find the decryption key
d = 0
for i in range(1, fn, e):
  if (i * e) % fn == 1:
    d = i
print("d=", d)

# cipher message
C = [3203, 909, 3143, 5255, 5343, 3609, 909, 9958, 5278, 
     5343, 9958, 5278, 4674, 909, 9958, 792, 909, 4132, 
     3143, 9958, 3203, 5343, 792, 3143, 4443]

# decryption block-by-block the cipher message
# decryption method: c[i]**d % n
message = ''
for i in range(len(C)):
  message += chr(C[i] ** d % n)

print("Message:", message)

