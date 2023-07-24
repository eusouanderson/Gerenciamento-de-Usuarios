from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///:usuarios.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

Base.metadata.create_all(engine)    

def save_user(name, email, password):
    new_user = User(name=name, email=email, password=password)
    session = Session()

    try:
        session.add(new_user)

        session.commit()
        print("Usuario salvo com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao salvar usuário: {e}, {name}")
    finally:
        session.close()

def read_users():
    session = Session()
    try:
        users = session.query(User).all()
        user_data = []

        for user in users:
            user_dict = {
                "id":user.id,
                "name":user.name,
                "email":user.email,
                "password":user.password
            }
            user_data.append(user_dict)
        
        return user_data
    except Exception as e:
        print(f"Erro ao ler usuarios: {e}")
    finally:
        session.close()

def delete_users(user_id):
    session = Session()

    if user_id != 0:
    
        try:
            user_to_delete = session.query(User).get(user_id)
            if user_to_delete:
                session.delete(user_to_delete)
                session.commit()
                print(f"Usuario com id {user_id} apagado com sucesso!")
            else:
                print(f"Usuario com Id {user_id} não encontrado.")
        except Exception as e:
            session.rollback()
            print(f"Erro ao apagar usuários: {e}")
        finally:
            session.close()
    else:
        session.query(User).delete()
        print("Todos usuarios deletados")

if __name__ == "__main__":
    users = read_users()
    for user in users:
        print(user)
