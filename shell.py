import cosmic

while True:
    text = input('cosmic > ')
    result, error = cosmic.run('<stdin>', text)
    
    if error: print(error.as_string())
    else: print(result)