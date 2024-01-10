from tatoeba_ckb import TatoebaCKB


t_ckb = TatoebaCKB()


data = t_ckb.get_data()

print(data.head())
