def trycode(codes,error_do):
  try:
    eval(codes)
  except as error:  
    eval(error_do)
def codelook(codes):
    try:
      eval(codes)
      print("Success Executed")
    except as error:
      print(f"ERROR:{error}\nPlease modify it!")
