def listify_word_file(filename):
  word_list = []
  with open(filename, 'r') as file_obj:
    word_list = file_obj.read()
  word_list = word_list.split()
  return word_list