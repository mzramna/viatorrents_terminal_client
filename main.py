from bs4 import BeautifulSoup
import requests

rooturl = "https://viatorrents.com/"


def get_magnets(url):
    source = requests.get(url).text
    bs = BeautifulSoup(source, "lxml")
    teste = bs.find(id="lista_download")
    bs = BeautifulSoup(teste.prettify(), "lxml")
    teste = bs.find_all('a')
    for i in teste:
        print(i['title'])
        print(i['href'])
    return teste


def get_categories():
    source = requests.get(rooturl).text
    bs = BeautifulSoup(source, "lxml")
    teste = bs.find_all("a", class_="nav-link")
    # for i in teste:
    #     print(i)
    return teste


def selecionar_categoria():
    categorias = get_categories()
    print("selecione a categoria")
    for i in categorias:
        print(str(categorias.index(i)) + " " + str(i["title"]))
    categoria_selecionada = int(input("digite o index: "))
    print(categorias[categoria_selecionada]["title"])
    return categorias[categoria_selecionada]


def listar_elementos_pagina(categoria, pagina=0):
    if pagina == 0:
        url = rooturl + categoria["href"]
    else:
        url = rooturl + categoria["href"] + str(pagina) + "/"
    print(url)
    source = requests.get(url).text
    bs = BeautifulSoup(source, "lxml")
    testes = bs.find_all(class_="capa_larga")
    resultados = []
    for teste in testes:
        bs = BeautifulSoup(teste.prettify(), "lxml")
        teste = bs.find_all('a')
        print(teste)
        resultados.append(teste[0])
    return resultados


def selecionar_pagina(categoria):
    pagina = 1
    selecao = ""
    while (not selecao.isdecimal()) or selecao == "":
        elementos = listar_elementos_pagina(categoria, pagina)
        for elemento in elementos:
            print(str(elementos.index(elemento) + 1) + "  " + elemento["title"])
        print("<  volta pagina")
        print(">  avanca pagina")
        selecao = input("selecione o elemento: ")
        while not selecao.isdecimal() and not (selecao == "<" or selecao == ">") and not (
                selecao == "<" and pagina == 0):
            print("valor inválido")
            selecao = input("selecione o elemento: ")

        if selecao.isdecimal():
            print(selecao)
            return elementos[int(selecao)-1]
        if selecao == "<":
            pagina -= 1
        if selecao == ">":
            pagina += 1


categoria_selecionada = selecionar_categoria()
selecionado=selecionar_pagina(categoria_selecionada)
get_magnets(selecionado["href"])