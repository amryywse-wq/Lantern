import shlex

class Parser :
    def __init__(self):
        self.tokens = None
        self.flags = None
        self.arg = None

    def parse_command(self, user_input):
        self.tokens = shlex.split(user_input)

        self.flags = []
        self.arg = []

        
        for token in self.tokens :
            if token.startswith('-'):
                self.flags.append(token)
            else :
                self.arg.append(token)
  
        return self.flags, self.arg





    