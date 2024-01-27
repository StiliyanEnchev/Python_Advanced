def func_executor(*funcs_data):
  result = []

  for func, data in funcs_data:
    result.append(f'{func.__name__} - {func(*data)}')

  return '\n'.join(result)