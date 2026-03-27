import pytest
from sqlalchemy import insert, select, delete, update
from conftest import Session, students


@pytest.fixture(scope="function")
def db_session():
    """Фикстура для сессии БД"""
    session = Session()
    yield session
    session.rollback()  # Откатываем изменения после теста
    session.close()


@pytest.fixture
def created_student(db_session):
    """
    Фикстура, которая создает студента и возвращает его ID.
    После теста данные очищаются автоматически.
    """
    ins = insert(students).values(name='John Doe', age=20).returning(students.c.id)
    result = db_session.execute(ins)
    db_session.commit()
    student_id = result.scalar_one()

    yield student_id

    # Очистка: удаляем созданного студента
    dele = delete(students).where(students.c.id == student_id)
    db_session.execute(dele)
    db_session.commit()


# Тест добавления студента
def test_add_student(db_session):
    # Добавляем нового студента
    ins = insert(students).values(name='John Doe', age=20)
    db_session.execute(ins)
    db_session.commit()

    # Проверка, что студент добавлен
    sel = select(students).where(students.c.name == 'John Doe')
    result = db_session.execute(sel).fetchone()
    assert result is not None
    assert result['name'] == 'John Doe'
    assert result['age'] == 20


# Тест обновления студента
def test_update_student(db_session, created_student):
    student_id = created_student
    # Обновляем возраст студента
    upd = update(students).where(students.c.id == student_id).values(age=21)
    db_session.execute(upd)
    db_session.commit()

    # Проверка обновления
    sel = select(students).where(students.c.id == student_id)
    result = db_session.execute(sel).fetchone()
    assert result is not None
    assert result['age'] == 21


# Тест удаления студента
def test_delete_student(db_session, created_student):
    student_id = created_student

    # Удаляем студента
    dele = delete(students).where(students.c.id == student_id)
    db_session.execute(dele)
    db_session.commit()

    # Проверка удаления
    sel = select(students).where(students.c.id == student_id)
    result = db_session.execute(sel).fetchone()
    assert result is None
