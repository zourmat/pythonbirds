class Pessoa:
    def cumprimentar(self):
        return 'Olá'
if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(Pessoa()))
    print(p.cumprimentar())

