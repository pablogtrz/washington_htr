class WordInput:
  def __init__(self, line):
    self.belongs_to = line.split(' ')[0].replace('\n', '')
    self.word = line.split(' ')[1].replace('\n', '')
    self.raw_word = self.word.replace('\n', '').replace('s_pt', '.').replace('s_0', '0').replace('s_1', '1').replace('s_2', '2').replace('s_3', '3').replace('s_4', '4').replace('s_5', '5').replace('s_6', '6').replace('s_7', '7').replace('s_8', '8').replace('s_9', '9').replace('s_sq', ';').replace('s_qo', ':').replace('s_mi', '_').replace('s_GW', 'GW').replace('s_cm', ',').replace('s_lb', '&').replace('s_bl', '(').replace('s_br', ')').replace('-', '')
    self.original_length = len(self.raw_word)
  
class WordInputSet:
  def __init__(self, words=[]):
    self.words = words

  def append(self, word_input):
    self.words.append(word_input)
  
  def getListOfWords(self):
    return map(lambda wordInput: wordInput.word, self.words)
  
  def getMaxLength(self):
    max_length = 0
    for word_input in self.words:
      if word_input.original_length > max_length:
        max_length = word_input.original_length
    return max_length

  def set_words_length_to_max(self):
    max_length = self.getMaxLength()
    for word_input in self.words:
      length_to_fill = max_length - word_input.original_length
      word_input.word = word_input.word + ('-#' * length_to_fill)

  def set_words_to_numbers(self, vocabulary):
    for word_input in self.words:
      numbers = self.char_to_num(word_input.word, vocabulary)
      word_input.word_as_nums = numbers

  def getWordInputFromImage(self, belongs_to):
    results = list(filter(lambda w: w.belongs_to == belongs_to, self.words))
    if len(results) > 0:
      return results[0] 
    else:
      return ''
    # return next(word_input for word_input in self.words if word_input.belongs_to == belongs_to)

  def getSetOfChars(self):
    words = list(map(lambda wordInput: wordInput.word, self.words))
    words.append('#')
    letters = '-'.join(words).split('-')
    vocabulary = list(dict.fromkeys(letters))
    return vocabulary
    
  def char_to_num(self, word, vocabulary):
     letters = word.split('-')
     numbers = list(map(lambda letter: vocabulary.index(letter), letters))
     return numbers

  def num_to_char(self, numbers, vocabulary):
    letters = list(map(lambda num: vocabulary[num], numbers))
    return letters