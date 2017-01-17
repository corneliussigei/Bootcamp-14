def data_type(argEntered):
  if isinstance(argEntered, str):
    return len(argEntered)
  elif argEntered is None:
    return 'no value'
  elif isinstance(argEntered, bool):
    return argEntered
  elif isinstance(argEntered, int):
    if argEntered < 100:
      return 'less than 100'
    elif argEntered == 100:
      return 'equal to 100'
    elif argEntered > 100:
      return 'more than 100'
  elif isinstance(argEntered, list):
    return argEntered[2] if len(argEntered) > 2 else None