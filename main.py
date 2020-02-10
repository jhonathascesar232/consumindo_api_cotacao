from tkinter import *
from functools import partial
from time import sleep

import cotacao
import conexao

class Cotacao:
    '''
    Recebe os dados sobre a cotaçao
    '''

    def getDolar(self):
        dados = cotacao.reqs(url = cotacao.urls['dolar'], n = cotacao.nomes[0])
        preco = float(dados['preco'])
        return preco

    def getEuro(self):
        dados = cotacao.reqs(url = cotacao.urls['euro'], n = cotacao.nomes[1])
        preco = float(dados['preco'])
        return preco

class Win():
    '''
Inicia a janela principal
    '''
    def __init__(self, dolar = False):
        if not dolar:
            self.dolar = 0
        else:
            self.dolar = dolar

        self.cotacao = dolar
        # print(f"** {self.cotacao.getDolar()}")
        
        self.usd_euro = ['USD', 'EUR']

        self.win = Tk()
        self.win.title('Cotação do Dolar(Py)')
        self.win.geometry('400x400+200+100')
        
        self.valor_dolar = StringVar()
        self.valor_real = StringVar()

        
    def frame_header(self):
        frame = Frame(self.win)
        frame.pack()

        lb = Label(frame,
                        textvar = self.valor_dolar,
                        )
        lb['font'] = ('Helvetica','16')
        lb['height'] = 7
        lb['width'] = 50
        lb.pack()

        lb_vazio = Label(frame)
        lb_vazio['height'] = 2
        lb_vazio.pack(side = 'bottom')

        self.btn_ys = Button(frame)
        self.btn_ys['text'] = 'EUR'
        self.btn_ys['width'] = 15
        self.btn_ys['command'] = partial(self.switch_moeda, self.usd_euro)
        self.btn_ys.pack(side = 'bottom')

    def frame_mid(self):
        frame = Frame(self.win)
        frame.pack()

        frame_esq = Frame(frame)
        frame_esq.pack(side='left', expand=1)

        frame_dir = Frame(frame)
        frame_dir.pack(side='right', expand=1)

        lb_real = Label(frame_esq, text='R$: ')
        lb_real.pack(side = 'left')

        self.campo_dinheiro = Entry(frame_esq)
        self.campo_dinheiro['width'] = 15
        self.campo_dinheiro.bind('<Return>', partial(self.converter_moeda,))
        self.campo_dinheiro.pack(side='left')

        lb_vazio = Label(frame_esq)
        lb_vazio['width']=5
        lb_vazio.pack()
        
        btn = Button(frame_dir)
        btn['text'] = 'Converter'
        btn['relief'] = 'groove'
        btn['width'] = 10
        btn['command'] = partial(self.converter_moeda)
        btn.pack(side='left')

    def frame_bot(self):
        frame = Frame(self.win)
        frame.pack(expand = 1)

        lb_b = Label(frame,
                     textvar = self.valor_real
                     )
        lb_b['font'] = 'Arial','16','italic'
        lb_b.pack()   

    def set_cotacao(self, preco):
        self.valor_dolar.set(preco)

    def converter_moeda(self, e = None):
        '''
        Faz a conversão da moeda
        '''
        dolar = self.cotacao.getDolar()
        euro = self.cotacao.getEuro()

        real = self.campo_dinheiro.get()
        if real == '':
            self.valor_real.set('Valor inválido')
        elif real == 0 or dolar == 0 or euro == 0:
            self.valor_real.set('Valor inválido')
        else:
            real = float(real)
           
            if not self.btn_ys['text'] == 'USD':
                moeda = real / dolar
                moeda = round(moeda, 2)
    
                self.valor_real.set('Você tem:\nUSD: %.2f' % (moeda))
            elif not self.btn_ys['text'] == 'EUR':
                moeda = real / euro
                moeda = round(moeda, 2)
                
                self.valor_real.set('Você tem:\nEUR: %.2f' % (moeda))
            print(f'** Moeda: {moeda}')

    def switch_moeda(self, moeda):
        '''
        Troca as opções de Moeda
        '''
        if self.btn_ys['text'] == 'EUR':
            euro = self.cotacao.getEuro()
            self.btn_ys['text'] = 'USD'
            self.set_cotacao("Cotação do Euro\nR$ %.2f" % (euro))
            self.preco = euro
        else:
            dolar = self.cotacao.getDolar()
            self.btn_ys['text'] = 'EUR'
            self.set_cotacao("Cotação do Dolar\nR$ %.2f" % (dolar))
            self.preco = dolar
        
#
# Programa principal
#
def main():   
    status = conexao.check_host()
    if status:
        dolar = Cotacao()
        win = Win(dolar)
        win.preco = dolar.getDolar()
        win.set_cotacao(win.preco)
    else:
        win = Win()

    win.frame_header()
    win.frame_mid()
    win.frame_bot()

    if status:
        win.set_cotacao(f"Cotação do Dolar\nR$ {dolar.getDolar():.3}")
    else: 
        win.set_cotacao(f"Falha na conexão com a internet!") 

    mainloop()


if __name__ == '__main__':
    main()
