# coding=utf8

from data import Datas

def main():
    datas=Datas("data/")
    datas["gdp"].Print()

if __name__=='__main__':
    main()