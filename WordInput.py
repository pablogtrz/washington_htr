class WordInput:
  def __init__(self, line):
    self.belongs_to = line.split(' ')[0].replace('\n', '')
    self.word = line.split(' ')[1].replace('\n', '')
    # self.word = line.split(' ')[1].replace('\n', '').replace('s_pt', '.').replace('s_0', '0').replace('s_1', '1').replace('s_2', '2').replace('s_3', '3').replace('s_4', '4').replace('s_5', '5').replace('s_6', '6').replace('s_7', '7').replace('s_8', '8').replace('s_9', '9').replace('s_sq', ';').replace('s_qo', ':').replace('s_mi', '_').replace('s_GW', 'GW').replace('s_cm', ',').replace('s_lb', '&').replace('s_bl', '(').replace('s_br', ')').replace('-', '')

class WordInputSet:
  def __init__(self, list=[]):
    self.list = list

  def append(self, word_input):
    self.list.append(word_input)
  
  def getListOfWords(self):
    return map(lambda wordInput: wordInput.word, self.list)
    
  def getWordInputFromImage(self, belongs_to):
    results = list(filter(lambda w: w.belongs_to == belongs_to, self.list))
    if len(results) > 0:
      return results[0] 
    else:
      return ''
    # return next(word_input for word_input in self.list if word_input.belongs_to == belongs_to)

  def getSetOfChars(self):
    words = list(map(lambda wordInput: wordInput.word, self.list))
    letters = '-'.join(words).split('-')
    vocabulary = list(dict.fromkeys(letters))
    return vocabulary
    # return {character for label in self.list for character in label.word}
    