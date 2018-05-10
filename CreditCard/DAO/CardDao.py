from DAO.DBTable import Card
from DAO.DBConnect import DBSession


def add_card(u, s, a, p, f):
    session = DBSession()
    card = Card(uid=u, name=s, A_day=a, P_day=p, num=f)
    session.add(card)
    session.commit()
    session.close()


def delete_card(c):
    session = DBSession()
    query = session.query(Card.cid)
    query.filter(Card.cid == c).delete()
    session.commit()
    session.close()


def find_card(u):
    session = DBSession()
    query = session.query(Card.cid, Card.name, Card.A_day, Card.P_day, Card.num)
    re = query.filter(Card.uid == u).all()
    session.close()
    return re