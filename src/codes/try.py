def trycode(codes,error_handling):
  if codes == null:
    print("Error:not codes!")
  elif error_handling == null:
    return "not error_handing!"
  else:
    try:
      eval(codes)
    except as error:  
      eval(error_handling)
  
