from database.dao import DAO
d=2

risultato=DAO.get_all_nodes(d)
print(risultato)

a=DAO.get_mappa_collegamenti()
print(a)