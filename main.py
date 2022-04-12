from subprocess import call
from tkinter import *
from time import sleep
from platform import node

# import tkinter as tk

root = Tk()


# back-end
class Fuc():
    def mostra(self, msg):
        self.log = print("-" * 30, msg, "-" * 30, sep='\n')

    def chama(self, code):
        _ = call(code)
        self.mostra("Inseriu um código")
        sleep(0.5)

    #         self.path = 'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\
    # # \Themes\Personalize" /v'

    #         if code == 'dark':
    #             _ = call('{} "SystemUsesLightTheme" /t REG_DWORD /d "0" /f'.format(self.path))
    #             _ = call('{} "AppsUseLightTheme" /t REG_DWORD /d "0" /f'.format(self.path))
    #             self.mostra("Mudou para para o tema escuro")

    #         elif code == 'light':
    #             _ = call(f'{self.path} "SystemUsesLightTheme" /t REG_DWORD /d "1" /f')
    #             sleep(1)
    #             _ = call(f'{self.path} "AppsUseLightTheme" /t REG_DWORD /d "1" /f')
    #             self.mostra("Mudou para para o tema claro")
    #         elif code == 'transparencia':
    #             _ = call(f'{self.path}"EnableTransparency" /t REG_DWORD /d "1" /f')
    #             self.mostra("Ativou transparência ao tema")
    #         elif code == 'sem transparencia':
    #             _ = call(f'{self.path}"EnableTransparency" /t REG_DWORD /d "0" /f')
    #             self.mostra("Desativou transparência ao tema")
    #         elif code == 'transparencia barra':
    #             _ = call(f'{self.path}"EnableTransparency" /t REG_DWORD /d "0" /f')
    #             _ = call(f'{self.path}"EnableTransparency" /t REG_DWORD /d "2" /f')
    #             self.mostra("Ativou transparência à barra de tarefas")
    #         else:
    #             _ = call(code)
    #             self.mostra("Inseriu um código")
    #         sleep(1)
    def bt_dark(self):
        # self.chama('dark')
        self.chama(
            'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v "SystemUsesLightTheme" /t REG_DWORD /d "0" /f')
        self.chama(
            'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v "AppsUseLightTheme" /t REG_DWORD /d "0" /f')
        self.mostra("Mudou para para o tema escuro")

    def bt_light(self):
        # self.chama('light')
        self.chama(
            'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v "SystemUsesLightTheme" /t REG_DWORD /d "1" /f')
        self.chama(
            'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v "AppsUseLightTheme" /t REG_DWORD /d "1" /f')
        self.mostra("Mudou para para o tema claro")

    def bt_transparencia(self):
        # self.chama('transparencia')
        self.chama(
            'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v "EnableTransparency" /t REG_DWORD /d "1" /f')
        self.mostra("Ativou transparência ao tema")

    def bt_sem_transparencia(self):
        # self.chama('sem transparencia')
        self.chama(
            'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v "EnableTransparency" /t REG_DWORD /d "0" /f')
        self.mostra("Desativou transparência ao tema")

    def btTransparenciaBarraDeTarefas(self):
        # self.chama('transparencia barra')
        self.chama(
            'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v "EnableTransparency" /t REG_DWORD /d "0" /f')
        sleep(1)
        self.chama(
            'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v "EnableTransparency" /t REG_DWORD /d "2" /f')
        self.mostra("Ativou transparência à barra de tarefas")

    def bt_ColorPrevalence(self):
        self.chama(
            'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v "ColorPrevalence" /t REG_DWORD /d "1" /f')
        self.mostra("Ativou prevalência de cor ao tema")

    def bt_SemColorPrevalence(self):
        self.chama(
            'Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v "ColorPrevalence" /t REG_DWORD /d "0" /f')
        self.mostra("Desativou prevalência de cor ao tema")

    def bt_salvar(self):
        host = node()
        hora = self.hora_entry.get()
        self.hora_entry = 'ok'
        # self.chama('schtasks.exe')
        self.chama('schtasks /delete /tn "Tema" /f')
        self.chama(f'schtasks /create /sc daily /tn "Tema" /tr "Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v "SystemUsesLightTheme" /t REG_DWORD /d "0" /st {hora} /f')
        self.chama(f'schtasks /create /sc daily /tn "Tema" /tr "Reg.exe add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v "AppsUseLightTheme" /t REG_DWORD /d "0" /st {hora} /f')
        self.mostra("Agendou um horário")

    def bt_limpar(self):
        self.chama('schtasks.exe')
        self.chama('schtasks /delete /tn "Tema" /f')
        self.hora_entry = ''
        self.mostra('Deletou o angendamento')

# front-end
class Aplicação(Fuc):

    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frama_1()
        root.tk.mainloop()

    def tela(self):
        self.root.title("Tema do Windows")
        self.root.configure()  # (background="beige")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        self.root.minsize(width=140, height=100)
        self.root.maxsize(width=520, height=400)

    def frames_da_tela(self):
        self.frame_2 = Frame(self.root, bd=1,
                             highlightbackground="#759fe6", highlightthickness=1)
        self.frame_2.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        self.frame_1 = Frame(self.root, bd=1,
                             highlightbackground="#759fe6", highlightthickness=1)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.90)

    def widgets_frama_1(self):
        ### Criação do botão limpar
        self.bt_limpar = Button(self.frame_1, text="Deletar", command=self.bt_limpar)
        self.bt_limpar.place(relx=0.15, rely=0.25, relwidth=0.1, relheight=0.1)
        ### Criação do botão salvar
        self.bt_limpar = Button(self.frame_1, text="Agendar", command=self.bt_salvar)
        self.bt_limpar.place(relx=0.25, rely=0.25, relwidth=0.1, relheight=0.1)

        ## Criação do label e entrada
        self.lb_hora = Label(self.frame_1, text="Troca automática:")
        self.lb_hora.place(relx=0.05, rely=0.05)

        self.lb_hora = Label(self.frame_1, text="Horário formato 24h (HH:MM)")
        self.lb_hora.place(relx=0.05, rely=0.15)

        self.hora_entry = Entry(self.frame_1)
        self.hora_entry.place(relx=0.3, rely=0.05, relwidth=0.08)

        ## Criação do label do tema
        self.lb_tema = Label(self.frame_1, text="Escolha o tema:", font='bold, 13')
        self.lb_tema.place(relx=0.55, rely=0.05)

        ### Criação do botão dark
        self.bt_dark = Button(self.frame_1, text="Modo Noturno",
                              bd=2, command=self.bt_dark)
        self.bt_dark.place(relx=0.45, rely=0.20, relwidth=0.5, relheight=0.3)

        ### Criação do botão light
        self.bt_light = Button(self.frame_1, text="Claro", command=self.bt_light)
        self.bt_light.place(relx=0.45, rely=0.50, relwidth=0.5, relheight=0.3)

        ### Criação do botão transparencia
        self.bt_transparencia = Button(self.frame_1, text="Ativar Transparência",
                                       command=self.bt_transparencia)
        self.bt_transparencia.place(relx=0.1, rely=0.40, relwidth=0.25, relheight=0.1)

        ### Criação do botão transparencia barra de tarefas
        self.bt_transparencia = Button(self.frame_1, text="Ativar Transparência\
\nBarra de Tarefas",
                                       command=self.btTransparenciaBarraDeTarefas)
        self.bt_transparencia.place(relx=0.1, rely=0.50, relwidth=0.25, relheight=0.2)

        ### Criação do botão sem transparencia
        self.bt_transparencia = Button(self.frame_1, text="sem Transparência",
                                       command=self.bt_sem_transparencia)
        self.bt_transparencia.place(relx=0.1, rely=0.70, relwidth=0.25, relheight=0.1)

        self.bt_transparencia = Button(self.frame_1, text="Prevalência de cor",
                                       command=self.bt_ColorPrevalence)
        self.bt_transparencia.place(relx=0.25, rely=0.85, relwidth=0.25, relheight=0.1)

        self.bt_transparencia = Button(self.frame_1, text="Sem prevalência",
                                       command=self.bt_SemColorPrevalence)
        self.bt_transparencia.place(relx=0.5, rely=0.85, relwidth=0.25, relheight=0.1)

        ### Criação de do log
        # self.lb_log = Label(self.frame_2, text="log")
        # self.lb_log.place(relx=0.5, rely=0.5)

        ### Criação da Lable versão e CopyRight
        self.lb_hora = Label(self.frame_2, text="Alpha 1.0", font=("verdana", 7, "italic"))
        self.lb_hora.place(relx=0.86, rely=0.94)

        self.lb_hora = Label(self.frame_2, text="Desenvolvedor Felipe Corrêa Carneiro",
                             fg="#107db2", font=("verdana", 8, "italic"))
        self.lb_hora.place(relx=0.05, rely=0.94)


Aplicação()

# if __name__ == '__main__':
#     root = tk.Tk()
#     root.title('Tema do Windows')
#     root.geometry("300x50")
#     linha_1 = tk.Label(root, text="Mude o aspecto para:")
#     linha_1.grid(column=0, row=1, padx=5, pady=10)
#     B_Dark = tk.Button(root, text='Dark Theme', command=black)
#     B_Dark.grid(column=1, row=1, padx=5, pady=10)
#     B_Light = tk.Button(root, text='Light Theme', command=white)
#     B_Light.grid(column=2, row=1, padx=5, pady=10)

#     root.mainloop()
